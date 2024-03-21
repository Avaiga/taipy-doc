from taipy.gui import Gui, Markdown, invoke_long_callback, notify
import numpy as np


status = 0
num_iterations = 10_000_000
pi_list = []


def pi_approx(num_iterations):
    k, s = 3.0, 1.0
    pi_list = []
    for i in range(num_iterations):
        s = s-((1/k) * (-1)**i)
        k += 2
        if (i+1)%(int(num_iterations/1_000)+1) == 0:
            pi_list += [np.abs(4*s-np.pi)]

    return pi_list

    
def heavy_status(state, status, pi_list):
    notify(state, 'i', f"Status parameter: {status}")
    if isinstance(status, bool):
        if status:
            notify(state, 'success', "Finished")
            state.pi_list = pi_list
        else:
            notify(state, 'error', f"An error was raised")
    else:
        state.status += 1
    
def on_action(state):
    invoke_long_callback(state,
                         pi_approx, [int(state.num_iterations)],
                         heavy_status, [],
                         2000)  

       
page = Markdown("""
How many times was the status function called? <|{status}|>

## Number of approximation

<|{num_iterations}|number|label=# of approximation|>

<|Approximate pie|button|on_action=on_action|>

## Evolution of approximation
<|{pi_list}|chart|layout={layout}|>
""")


layout = {
    "yaxis": {
    "type": 'log',
    "autorange": True
    }
  }


Gui(page).run()
