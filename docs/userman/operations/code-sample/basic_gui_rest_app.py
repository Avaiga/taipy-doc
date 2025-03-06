import taipy as tp

if __name__ == "__main__":
    gui = tp.Gui(page="# Getting started with *Taipy*")
    rest = tp.Rest()

    tp.run(gui, rest, title="Taipy application")
