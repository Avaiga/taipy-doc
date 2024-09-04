import pandas as pd
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification, AutoTokenizer

import taipy.gui.builder as tgb
from taipy.gui import Gui, notify

# Model setup
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def analyze_text(text):
    # Run for Roberta Model
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    return {"Text":text,
            "Score Pos":scores[2],
            "Score Neu":scores[1],
            "Score Neg":scores[0],
            "Overall":scores[2]-scores[0]}

def local_callback(state):
    notify(state, 'info', f'The text is: {state.text}')
    scores = analyze_text(state.text)
    temp = state.dataframe.copy()
    temp.loc[len(temp)] = scores
    state.dataframe = temp
    state.text = ""

if __name__ == "__main__":
    text = "Original text"

    # Initial dataframe
    dataframe = pd.DataFrame({"Text":[''],
                            "Score Pos":[0.33],
                            "Score Neu":[0.33],
                            "Score Neg":[0.33],
                            "Overall":[0]})

    # Definition of the page with tgb
    with tgb.Page() as page:
        tgb.toggle(theme=True)

        tgb.text("# Getting started with Taipy GUI", mode="md")
        tgb.text("My text: {text}")

        tgb.input("{text}")
        tgb.button("Analyze", on_action=local_callback)

        # Displaying sentiment scores and overall sentiment
        tgb.text("## Positive", mode="md")
        tgb.text("{np.mean(dataframe['Score Pos'])}", format="%.2f")

        tgb.text("## Neutral", mode="md")
        tgb.text("{np.mean(dataframe['Score Neu'])}", format="%.2f")

        tgb.text("## Negative", mode="md")
        tgb.text("{np.mean(dataframe['Score Neg'])}", format="%.2f")

        tgb.table("{dataframe}", number_format="%.2f")
        tgb.chart("{dataframe}", type="bar", x="Text",
                y__1="Score Pos", y__2="Score Neu", y__3="Score Neg", y__4="Overall",
                color__1="green", color__2="grey", color__3="red", type__4="line")

    # Initialize the GUI with the updated dataframe
    Gui(page).run(debug=True)
