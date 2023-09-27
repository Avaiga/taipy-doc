from taipy.gui import Gui

text = "Original text"

page = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>
"""

Gui(page).run()