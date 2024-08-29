import pandas as pd
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification, AutoTokenizer

import taipy.gui.builder as tgb
from taipy.gui import Gui, notify

# Initialize model and tokenizer
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def analyze_text(text):
    # Run sentiment analysis model
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    return {
        "Text": text,
        "Score Pos": scores[2],
        "Score Neu": scores[1],
        "Score Neg": scores[0],
        "Overall": scores[2] - scores[0]
    }

def local_callback(state):
    notify(state, 'info', f'The text is: {state.text}')
    scores = analyze_text(state.text)
    temp = state.dataframe.copy()
    temp.loc[len(temp)] = scores
    state.dataframe = temp
    state.text = ""

def analyze_file(state):
    state.dataframe2 = dataframe2
    state.treatment = 0
    with open(state.path,"r", encoding="utf-8") as f:
        data = f.read()
        # split lines and eliminates duplicates
        file_list = list(dict.fromkeys(data.replace("\n", " ").split(".")[:-1]))

    for i in range(len(file_list)):
        text = file_list[i]
        state.treatment = int((i+1)*100/len(file_list))
        temp = state.dataframe2.copy()
        scores = analyze_text(text)
        temp.loc[len(temp)] = scores
        state.dataframe2 = temp

    state.path = None

if __name__ == "__main__":
    text = "Original text"

    # Initial dataframe setup
    dataframe = pd.DataFrame({
        "Text": [''],
        "Score Pos": [0.33],
        "Score Neu": [0.33],
        "Score Neg": [0.33],
        "Overall": [0]
    })

    # GUI layout with tgb
    with tgb.Page() as page:
        with tgb.layout(columns="1 1"):
            with tgb.part():
                tgb.text("My text: {text}")
                tgb.input("{text}")
                tgb.button("Analyze", on_action=local_callback)

            with tgb.expandable("Table"):
                tgb.table("{dataframe}", number_format="%.2f")

        with tgb.layout(columns="1 1 1"):
            with tgb.part():
                tgb.text("## Positive", mode="md")
                tgb.text("{np.mean(dataframe['Score Pos'])}", format="%.2f")
            with tgb.part():
                tgb.text("## Neutral", mode="md")
                tgb.text("{np.mean(dataframe['Score Neu'])}", format="%.2f")
            with tgb.part():
                tgb.text("## Negative", mode="md")
                tgb.text("{np.mean(dataframe['Score Neg'])}", format="%.2f")

        tgb.chart("{dataframe}", type="bar", x="Text", y__1="Score Pos", y__2="Score Neu", y__3="Score Neg", y__4="Overall",
                color__1="green", color__2="grey", color__3="red", type__4="line")

    # Second page
    dataframe2 = dataframe.copy()
    path = ""
    treatment = 0

    with tgb.Page() as page_file:
        tgb.file_selector("{path}", extensions=".txt", label="Upload .txt file",
                        on_action=analyze_file)
        tgb.text("Downloading {treatment}%...")

        with tgb.expandable("Table"):
            tgb.table("{dataframe2}")

        tgb.chart("{dataframe2}", type="bar", x="Text",
                y__1="Score Pos", y__2="Score Neu",  y__3="Score Neg", y__4="Overall",
                color__1="green", color__2="grey", color__3="red", type__4="line",
                height="800px")

    # Run the GUI
    # One root page for common content
    # The two pages that were created
    pages = {"/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
            "line":page,
            "text":page_file}

    Gui(pages=pages).run(debug=True)
