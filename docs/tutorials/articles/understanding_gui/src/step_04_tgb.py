import pandas as pd

import taipy.gui.builder as tgb
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

    dataframe = pd.DataFrame({"Text":['Test', 'Other', 'Love'],
                            "Score Pos":[1, 1, 4],
                            "Score Neu":[2, 3, 1],
                            "Score Neg":[1, 2, 0],
                            "Overall":[0, -1, 4]})

    # Definition of the page
    with tgb.Page() as page:
        tgb.toggle(theme=True)

        tgb.text("# Getting started with Taipy GUI", mode="md")
        tgb.text("My text: {text}")

        tgb.input("{text}")
        tgb.button("Analyze", on_action=local_callback)

        tgb.table("{dataframe}")
        tgb.chart("{dataframe}", type="bar", x="Text",
                y__1="Score Pos", y__2="Score Neu", y__3="Score Neg", y__4="Overall",
                color__1="green", color__2="grey", color__3="red", type__4="line")

    Gui(page).run(debug=True)
