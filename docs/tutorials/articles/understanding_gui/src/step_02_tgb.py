import taipy.gui.builder as tgb
from taipy.gui import Gui

if __name__ == "__main__":
    text = "Original text"

    with tgb.Page() as page:
        tgb.text("# Getting started with Taipy GUI", mode="md")
        tgb.text("My text: {text}")

        tgb.input("{text}")

    Gui(page).run(debug=True)
