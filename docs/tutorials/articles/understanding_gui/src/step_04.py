import pandas as pd

from taipy.gui import Gui, notify


def local_callback(state):
    notify(state, 'info', f'The text is: {state.text}')

    temp = state.dataframe.copy()
    temp.loc[len(temp)] = {"Text":state.text,
                            "Score Pos":0,
                            "Score Neu":0,
                            "Score Neg":0,
                            "Overall":0}
    state.dataframe = temp
    state.text = ""

if __name__ == "__main__":
    text = "Original text"

    page = """
<|toggle|theme|>

# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>

<|Analyze|button|on_action=local_callback|>

<|{dataframe}|table|number_format=%.2f|>

<|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|>
    """

    dataframe = pd.DataFrame({"Text":['Test', 'Other', 'Love'],
                            "Score Pos":[1, 1, 4],
                            "Score Neu":[2, 3, 1],
                            "Score Neg":[1, 2, 0],
                            "Overall":[0, -1, 4]})

    Gui(page).run(debug=True)
