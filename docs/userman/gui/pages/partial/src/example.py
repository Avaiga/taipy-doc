import taipy.gui.builder as tgb
from taipy.gui import Gui


# Function to refresh the links partial
def refresh_links(state):
    with tgb.Page() as link_part:
        with tgb.layout("1 1 1"):
            for link in state.links:
                link_name, link_url = link
                with tgb.part("card"):
                    tgb.text(link_name, class_name="h2")
                    tgb.text("Quick description here if you like")
                    tgb.html("a", f"Click here to go to {link_name}", href=link_url)
                    # You could use any visual element you like
    state.link_partial.update_content(state, link_part)


# Function to simulate adding more links
def simulate_adding_more_links(state):
    state.links = [
        ("Taipy", "http://taipy.io"),
        ("Taipy Doc", "http://docs.taipy.io"),
        ("Wikipedia", "http://wikipedia.org"),
        (
            "Article",
            "https://betterprogramming.pub/discovering-taipy-and-taipy-gui-e1b664765017",
        ),
    ]
    refresh_links(state)


# Initialize the application state
def on_init(state):
    refresh_links(state)


if __name__ == "__main__":
    # Initial links
    links = [("Taipy", "http://taipy.io")]

    # Define the main page layout
    with tgb.Page() as main_page:
        tgb.button("Add links", on_action=simulate_adding_more_links)
        tgb.part(partial="{link_partial}")

    # Create and run the Taipy GUI
    gui = Gui(main_page)
    link_partial = gui.add_partial("")
    gui.run()
