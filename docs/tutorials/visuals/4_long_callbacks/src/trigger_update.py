from taipy.gui import Gui, invoke_long_callback, get_state_id, invoke_callback
import taipy.gui.builder as tgb
import time 

logs = ""
result = "No response yet"

def status_fct(state, status, result):
    state.logs = ""
    state.result = result

def user_status(state, info):
    state.logs = state.logs + "\n" + info

def heavy_function(gui, state_id):
    invoke_callback(gui, state_id, user_status, ["Searching documents"])
    time.sleep(5)
    invoke_callback(gui, state_id, user_status, ["Responding to user"])
    time.sleep(5)
    invoke_callback(gui, state_id, user_status, ["Fact Checking"])
    return "Here is the answer"


def respond(state):
    invoke_long_callback(state=state,
                         user_function=heavy_function, user_function_args=[gui, get_state_id(state)],
                         user_status_function=status_fct, user_status_function_args=[])

with tgb.Page() as main_page:
    tgb.button("Respond", on_action=respond)
    with tgb.part("card"):
        tgb.text("{logs}", mode="pre")
    
    tgb.text("# Result", mode="md")
    tgb.text("{result}")


gui = Gui(main_page)
gui.run()