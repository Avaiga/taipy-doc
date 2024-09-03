Pages are the basis for the user interface. Pages hold text, images, or
controls that display information that the application needs to publish and
interact with the application data through visual elements.

# Defining pages

Taipy lets you create as many pages as you require with whatever content you need.

!!! tip "Choosing how to create pages"

    Choosing between the Markdown format, HTML content, or Python code depends on several
    parameters:

    - Use [Markdown](markdown.md) when:

        - You need to create a page in a few minutes;
        - You want to benefit from the [Taipy Studio preview](../../ecosystem/studio/gui.md#page-preview)
          feature;
        - You have no experience in UI development, especially on the web;
        - The text layout is close enough to your final presentation objectives.

    - Use [HTML](html.md) when:

        - You have experience in HTML;
        - You have a set of HTML files that you want to complement with Taipy GUI visual elements
          and connect to a Python backend application;
        - You need a precise page structure.

    - Use Python with the [Page Builder API](builder.md) when:

        - You are familiar with the Python language and Python libraries that help build web
          applications (like [gradio](https://www.gradio.app/));
        - You need to decide at runtime what elements should be created and how. This usually
          involves control of the code flow (using tests or loops), which is more difficult to
          achieve using text templates.

    === "Markdown"
        ```python
        from taipy import Gui

        if __name__ == "__main__":
            page = "# First page"

            Gui(page).run()
        ```
    === "Python"
        ```python
        from taipy import Gui
        import taipy.gui.builder as tgb

        if __name__ == "__main__":
            with tgb.Page() as page:
                tgb.text("# First Page", mode="md")

            Gui(page).run()
        ```

## Defining the page content

The definition of a page typically consists of:

- Adding visual elements to the page.
- Binding variables to these elements.
- Setting properties to these elements.
- Setting callbacks to these elements.

!!! example "Getting Started example"
    === "Markdown"
        ```python linenums="1"
        from taipy.gui import Gui
        from math import cos, exp

        def slider_moved(state):
            state.data = compute_data(state.value)

        def compute_data(decay:int)->list:
            return [cos(i/6) * exp(-i*decay/600) for i in range(100)]

        if __name__ == "__main__":
            value = 10

            page = """
        # Taipy *Getting Started*

        Value: <|{value}|text|>

        <|{value}|slider|on_change=slider_moved|>

        <|{data}|chart|>
            """

            data = compute_data(value)

            Gui(page).run(title="Dynamic chart")
        ```

    === "Python"
        ```python linenums="1"
        from taipy.gui import Gui
        import taipy.gui.builder as tgb
        from math import cos, exp

        def compute_data(decay:int)->list:
            return [cos(i/6) * exp(-i*decay/600) for i in range(100)]

        def slider_moved(state):
            state.data = compute_data(state.value)

        if __name__ == "__main__":
            value = 10

            with tgb.Page() as page:
                tgb.text(value="# Taipy Getting Started", mode="md")
                tgb.text(value="Value: {value}")
                tgb.slider(value="{value}", on_change=slider_moved)
                tgb.chart(data="{data}")

            data = compute_data(value)

            Gui(page).run(title="Dynamic chart")
        ```

## Registering a single page

Once you have created an instance of a page renderer for a specific piece of text or Python code,
you can register that page to the `Gui^` instance used by your application.

The `Gui^` constructor can accept the raw content of a page as Markdown text, a Page object and
create a new page for you. That would be the easier way to create applications that have a
single page. Here is how you can create and register a page in a
Taipy application:

=== "Markdown"
    ```python
    from taipy import Gui

    if __name__ == "__main__":
        page = "# First page"

        Gui(page).run()
    ```
=== "Python"
    ```python
    from taipy import Gui
    import taipy.gui.builder as tgb

    if __name__ == "__main__":
        with tgb.Page() as page:
            tgb.text("# First Page", mode="md")

        Gui(page).run()
    ```

If you run this Python script and connect a browser to the web server address
(usually *localhost:5000*), you can see your title displayed on an empty page.

# Multi-page application

If your application has several pages, you add your pages one by one
using `Gui.add_page()^`. To add multiple pages in a single call, you will
use `Gui.add_pages()^` or create the `Gui^` instance using the *pages*
argument. In those situations, you have to create a Python dictionary that
associates a page with its name:

=== "Markdown"
    ```python
    from taipy import Gui

    if __name__ == "__main__":
        root_md = "# Multi-page application"
        home_md = "# Home"
        about_md = "# About"

        pages = {
            "/": root_md,
            "home": home_md,
            "about": about_md
        }

        Gui(pages=pages).run()
        # or
        # gui = Gui()
        # gui.add_pages(pages)
        # gui.run()
    ```
=== "Python"
    ```python
    from taipy import Gui
    import taipy.gui.builder as tgb

    if __name__ == "__main__":
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
        # or
        # gui = Gui()
        # gui.add_pages(pages)
        # gui.run()
    ```

You could have also used the `(Gui.)add_page()` function.


In this situation, to see the pages in your browser, the address you will use
will be *localhost:5000/home* or *localhost:5000/about*. Learn how to natigate between pages [here](../pages/navigate/index.md).

Note that if pages are created in different modules, the variables that they can bind
to visual elements may have a scope limited to their origin module. See
[Page scopes](../binding.md#scope-for-variable-binding) for more details.

## Root page

The *Root* page is the page located at `"/"` (or the value of the
[*base_url*](../../advanced_features/configuration/gui-config.md#p-base_url) configuration setting).
The content of the page will be shown at the top of every page of your application.

## Application header and footer

Your application may also need to hold a footer on all the pages it uses.<br/>
You can use the pseudo-control `<|content|>` to achieve the expected result: this
visual element is not *really* a control: It is a placeholder for page content, used in the
root page of your application, and is replaced by the target page content when the application
runs.

!!! example

    ```python
    from taipy import Gui

    if __name__ == "__main__":
        root_md="""
    # Multi-page application

    <|content|>

    This application was created with [Taipy](https://www.taipy.io/).
        """
        home_md="## Home"
        about_md="## About"

        pages = {
            "/": root_md,
            "home": home_md,
            "about": about_md
        }
        Gui(pages=pages).run()
    ```

    This application does the same as in the previous example, except that you now
    have the footer line (*'This application was created...'*) in all the pages of
    your application.
