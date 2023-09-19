from taipy.gui import Gui, notify

text = "Original text"

# Definition of the page
page = """
<|toggle|theme|>

# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>

<|Analyze|button|on_action=local_callback|>
"""

def local_callback(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    print(var_name, var_value, state.text)
    # be aware of 
    if var_name == "text" and len(var_value) > 8:
        notify(state, 'warning', 'Length of input superior to 8')


Gui(page).run()