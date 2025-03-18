import taipy as tp

if __name__ == "__main__":
    orchestrator = tp.Orchestrator()
    gui = tp.Gui(page="# Getting started with *Taipy*")

    tp.run(gui, orchestrator, title="Taipy application")
