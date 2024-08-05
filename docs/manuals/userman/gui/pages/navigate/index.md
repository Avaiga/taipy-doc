This documentation page will walk you through creating a multi-page application, using the navbar and menu for navigation, the `navigate` function, and the `on_navigate` function for controlling page transitions.

=== "Markdown"
    ```python
    from taipy import Gui

    root_md = "# Multi-page application"
    home_md = "# Home"
    about_md = "# About"

    pages = {
        "/": root_md,
        "home": home_md,
        "about": about_md
    }

    Gui(pages=pages).run()
    ```
=== "Python"
    ```python
    from taipy import Gui
    import taipy.gui.builder as tgb

    with tgb.Page() as root_page:
        tgb.text("# Multi-page application", mode="md")

    with tgb.Page() as home_page:
        tgb.text("# Home", mode="md")

    with tgb.Page() as about_page:
        tgb.text("# About", mode="md")

    pages = {
        "/": root_page,
        "home": home_page,
        "about": about_page
    }

    Gui(pages=pages).run()
    ```

# Using Navbar

[Navbar](../../viselements/generic/navbar.md) is a visual element which by default lets you navigate between pages. You can customize the navbar with properties like the list of pages you are able to navigate to. 

=== "Markdown"
    ```python
    from taipy import Gui

    root_md = """
    <|navbar|>
    # Multi-page application
    """
    home_md = "# Home"
    about_md = "# About"

    pages = {
        "/": root_md,
        "home": home_md,
        "about": about_md
    }

    Gui(pages=pages).run()
    ```
=== "Python"
    ```python
    from taipy import Gui
    import taipy.gui.builder as tgb

    with tgb.Page() as root_page:
        tgb.navbar()
        tgb.text("# Multi-page application", mode="md")

    with tgb.Page() as home_page:
        tgb.text("# Home", mode="md")

    with tgb.Page() as about_page:
        tgb.text("# About", mode="md")

    pages = {
        "/": root_page,
        "home": home_page,
        "about": about_page
    }

    Gui(pages=pages).run()
    ```

# Using Menu

[Menu](../../viselements/generic/menu.md) creates a menu on the left to
navigate through the pages.

=== "Markdown"
    ```
    <|menu|label=Menu|lov={lov_pages}|on_action=on_menu|>`
    ```
=== "Python"
    ```python
    tgb.menu(label="Menu", lov=[...], on_action=on_menu)
    ```

![Menu](images/menu.png){ width=40% : .tp-image-border }

For example, this code creates a menu with two options:

=== "Markdown"
    ```python
    from taipy import Gui, navigate

    root_md = """
    <|menu|label=Menu|lov={[('home', 'Home'), ('about', 'About')]}|on_action=on_menu|>
    # Multi-page application
    """

    home_md = "# Home"
    about_md = "# About"

    def on_menu(state, action, info):
        page = info["args"][0]
        navigate(state, to=page)

    pages = {
        "/": root_md,
        "home": home_md,
        "about": about_md
    }

    Gui(pages=pages).run()
    ```
=== "Python"
    ```python
    from taipy import Gui, navigate
    import taipy.gui.builder as tgb

    def on_menu(state, action, info):
        page = info["args"][0]
        navigate(state, to=page)

    with tgb.Page() as root_page:
        tgb.menu(label="Menu",
                lov=[('home', 'Page 1'), ('about', 'Page 2')],
                on_action=on_menu)
        tgb.text("# Multi-page application", mode="md")

    with tgb.Page() as home_page:
        tgb.text("# Home", mode="md")

    with tgb.Page() as about_page:
        tgb.text("# About", mode="md")

    pages = {
        "/": root_page,
        "home": home_page,
        "about": about_page
    }

    Gui(pages=pages).run()
    ```

# Using the `navigate` function

The `navigate` function allows for programmatically controlling navigation within callback functions. You can navigate to a page of this application or an external page.

=== "Markdown"
    ```python
    from taipy import Gui, navigate

    root_md = """
    <|Click to go to Page 1|button|on_action=go_home|>
    # Multi-page application
    """

    home_md = "# Home"
    about_md = "# About"

    def go_home(state):
        navigate(state, "home")

    pages = {
        "/": root_md,
        "home": home_md,
        "about": about_md
    }

    Gui(pages=pages).run()
    ```
=== "Python"
    ```python
    from taipy import Gui, navigate
    import taipy.gui.builder as tgb

    def go_home(state):
        navigate(state, "home")

    with tgb.Page() as root_page:
        tgb.button(label="Click to go to Page 1", on_action=go_home)
        tgb.text("# Multi-page application", mode="md")

    with tgb.Page() as home_page:
        tgb.text("# Home", mode="md")

    with tgb.Page() as about_page:
        tgb.text("# About", mode="md")

    pages = {
        "/": root_page,
        "home": home_page,
        "about": about_page
    }

    Gui(pages=pages).run()
    ```


# Using the `on_navigate` function

The `on_navigate` function allows for custom control over navigation, such as redirecting users based on conditions. T

See more information for [*on_navigate*](../../callbacks.md#navigation-callback).


=== "Markdown"
    ```python
    from taipy import Gui, State

    results_ready = False

    def on_navigate(state: State, page_name: str):
        if page_name == "results" and not state.results_ready:
            return "no_results"
        return page_name

    root_md = "# Multi-page application"
    results_md = "# Results Page"
    no_results_md = "# No Results Available"

    pages = {
        "/": root_md,
        "results": results_md,
        "no_results": no_results_md
    }

    gui = Gui(pages=pages)
    gui.run()
    ```
=== "Python"
    ```python
    from taipy import Gui, State
    import taipy.gui.builder as tgb

    results_ready = False

    def on_navigate(state: State, page_name: str):
        if page_name == "results" and not state.results_ready:
            return "no_results"
        return page_name

    with tgb.Page() as root_page:
        tgb.text("# Multi-page application", mode="md")

    with tgb.Page() as results_page:
        tgb.text("# Results Page", mode="md")

    with tgb.Page() as no_results_page:
        tgb.text("# No Results Available", mode="md")

    pages = {
        "/": root_page,
        "results": results_page,
        "no_results": no_results_page
    }

    gui = Gui(pages=pages)
    gui.run()
    ```
