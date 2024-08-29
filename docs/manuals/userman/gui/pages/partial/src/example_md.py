from taipy.gui import Gui


# Function to refresh the links partial
def refresh_links(state):
    partial_md = "<|layout|columns=1 1 1|\n"
    for link in state.links:
        link_name, link_url = link
        partial_md += "<|card|\n"
        partial_md += f"## {link_name}\n"
        partial_md += "Quick description here if you like\n\n"
        partial_md += f"[Click here to go to {link_name}]({link_url})\n"
        partial_md += "|>\n"
    partial_md += "|>\n"
    state.link_partial.update_content(state, partial_md)


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
    main_page = """
<|Add links|button|on_action=simulate_adding_more_links|>
<|part|partial={link_partial}|>
    """

    # Create and run the Taipy GUI
    gui = Gui(main_page)
    link_partial = gui.add_partial("")
    gui.run()
