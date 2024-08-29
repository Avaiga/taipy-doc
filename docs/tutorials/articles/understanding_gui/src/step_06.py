import pandas as pd
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from taipy.gui import Gui, notify

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
    notify(state, 'Info', f'The text is: {state.text}', True)
    temp = state.dataframe.copy()
    scores = analyze_text(state.text)
    temp.loc[len(temp)] = scores
    state.dataframe = temp
    state.text = ""

if __name__ == "__main__":
    text = "Original text"

    dataframe = pd.DataFrame({"Text":[''],
                            "Score Pos":[0.33],
                            "Score Neu":[0.33],
                            "Score Neg":[0.33],
                            "Overall":[0]})

    page = """
# Getting started with Taipy GUI

<|layout|columns=1 1|
<|
My text: <|{text}|>

Enter a word:
<|{text}|input|>
<|Analyze|button|on_action=local_callback|>
|>


<|Table|expandable|
<|{dataframe}|table|number_format=%.2f|>
|>
|>

<|layout|columns=1 1 1|
## Positive <|{float(np.mean(dataframe['Score Pos']))}|text|format=%.2f|raw|>%

## Neutral <|{float(np.mean(dataframe['Score Neu']))}|text|format=%.2f|raw|>%

## Negative <|{float(np.mean(dataframe['Score Neg']))}|text|format=%.2f|raw|>%
|>

<br/>

<|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|>
    """

    Gui(page).run(debug=True)
