from taipy.gui import Gui

if __name__ == "__main__":
    text = "Original text"

    page = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>
    """

    Gui(page).run(debug=True)
