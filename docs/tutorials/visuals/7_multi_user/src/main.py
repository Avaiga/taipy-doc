from taipy.gui import Gui, State
import pandas as pd


def on_init(state: State):
    global client_index
    if client_index == 1:
        state.user_name = "Alex"
    else:
        state.user_name = "Doppler"
    client_index += 1


# Start or stop the timer when the button is pressed
def send_message(state):
    state.broadcast("new_message", state.current_message)
    state.broadcast("new_sender", state.user_name)
    state.current_message = ""


def on_change(state, var_name, value):
    if var_name == "new_message":
        # Check if the last row is not already the user's message
        if (
            state.conversation.iloc[-1]["User"] != state.user_name
            or state.conversation.iloc[-1]["Message"] != state.new_message
        ):
            state.conversation = pd.concat(
                [
                    state.conversation,
                    pd.DataFrame(
                        {"User": [state.user_name], "Message": [state.new_message]}
                    ),
                ],
                ignore_index=True,
            )
        state.selected_row = [len(state.conversation["User"]) + 1]


if __name__ == "__main__":
    timer_status = "Timer stopped"

    client_index = 1
    user_name = ""
    conversation = pd.DataFrame(
        {"User": ["Alex", "Doppler"], "Message": ["Hey!", "Whats'up?"]}
    )
    current_message = ""
    new_message = ""
    new_sender = ""
    selected_row = [2]

    page = """
# Multi-User **Chat**{: .color-primary}

Username: <|{user_name}|input|active=false|>

<|{conversation}|table|rebuild|show_all|class_name=table|selected={selected_row}|>

<|{current_message}|input|label=Write your message here...|on_action=send_message|class_name=fullwidth|change_delay=-1|>
    """

    gui = Gui(page)
    gui.add_shared_variable("conversation")
    gui.run(dark_mode=True)
