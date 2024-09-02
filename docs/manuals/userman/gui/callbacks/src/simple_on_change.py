from taipy.gui import Gui
import taipy.gui.builder as tgb


def on_change(state, var, val):
    if var == "x":
        print(f"'{val}' was changed to: {val}")


if __name__ == "__main__":
    x = 50

    with tgb.Page() as page:
        tgb.slider("{x}")

    Gui(page).run()
