import taipy.gui.builder as tgb
from taipy.gui import Gui, notify


def on_button_action(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

if __name__ == "__main__":
    text = "Original text"

    # Definition of the page
    with tgb.Page() as page:
        tgb.text("# Getting started with Taipy GUI", mode="md")
        tgb.text("My text: {text}")

        tgb.input("{text}")
        tgb.button("Run local", on_action=on_button_action)

    Gui(page).run(debug=True)
