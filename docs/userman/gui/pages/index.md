Pages are the basis for the user interface. Pages hold text, images, or
controls that display information that the application needs to publish and
interact with the application data through visual elements.

# Defining pages

Taipy lets you create as many pages as you require with whatever content you need.

!!! tip "Choosing how to create pages"

    Choosing between Python code, the Markdown format, or HTML content, or  depends on several
    parameters:

    - Use Python with the [Page Builder API](builder.md) when:

        - You are familiar with the Python language and Python libraries that help build web
          applications (like [gradio](https://www.gradio.app/));
        - You need to decide at runtime what elements should be created and how. This usually
          involves control of the code flow (using tests or loops), which is more difficult to
          achieve using text templates.

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

    === "Python"
        ```python
        from taipy import Gui
        import taipy.gui.builder as tgb

        if __name__ == "__main__":
            with tgb.Page() as page:
                tgb.text("# First Page", mode="md")

            Gui(page).run()
        ```
    === "Markdown"
        ```python
        from taipy import Gui

        if __name__ == "__main__":
            page = "# First page"

            Gui(page).run()
        ```

## Defining the page content

The definition of a page typically consists of:

- Adding visual elements to the page.
- Binding variables to these elements.
- Setting properties to these elements.
- Setting callbacks to these elements.

!!! example "Getting Started example"
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

## Registering a single page

Once you have created an instance of a page renderer for a specific piece of text or Python code,
you can register that page to the `Gui^` instance used by your application.

The `Gui^` constructor can accept the raw content of a page as Markdown text, a Page object and
create a new page for you. That would be the easier way to create applications that have a
single page. Here is how you can create and register a page in a
Taipy application:

=== "Python"
    ```python
    from taipy import Gui
    import taipy.gui.builder as tgb

    if __name__ == "__main__":
        with tgb.Page() as page:
            tgb.text("# First Page", mode="md")

        Gui(page).run()
    ```
=== "Markdown"
    ```python
    from taipy import Gui

    if __name__ == "__main__":
        page = "# First page"

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

You could have also used the `(Gui.)add_page()^` function for each page.

In this situation, to see the pages in your browser, the address you will use will be
*localhost:5000/home* or *localhost:5000/about*. Learn how to navigate between pages
[here](../pages/navigate/index.md).<br/>
If you point the browser to the root of the server (*localhost:5000/*) then it will be redirected to
the first added page. In our situation, the *home* page at *localhost:5000/home*.

Note that if pages are created in different modules, the variables that they can bind
to visual elements may have a scope limited to their origin module. See
[Page scopes](../binding.md#scope-for-variable-binding) for more details.

## Root page

The *Root* page is the page located at `"/"`.

You may choose to expose you application pages to another top directory. To do this, you must
prefix each page name with the directory you wish to expose:
```python
pages = {
    "/": root_md,
    "my_application/home": home_md,
    "my_application/about": about_md
}
```

When opening a browser on the page located at *localhost:5000/*, it will be redirected to the
first declared page, at *localhost:5000/my_application/home*.

The content of the root page will be displayed at the top of every page of your application.

If you want to expose your application at a given root directory in a production environment, you
may want to set the value of the
[*base_url*](../../advanced_features/configuration/gui-config.md#p-base_url) configuration setting.
Please refer to the documentation for this setting for more information.

## Application header and footer

Your application may also need to hold a footer on all the pages it uses.<br/>
You can use the pseudo-control `content` to achieve the expected result: this
visual element is not *really* a control: It is a placeholder for page content, used in the
root page of your application, and is replaced by the target page content when the application
runs.

!!! example "Adding a page footer"
    ```python
    from taipy import Gui

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

    if __name__ == "__main__":
        Gui(pages=pages).run()
    ```

    This application does the same as in the previous example, except that you now
    have the footer line (*'This application was created...'*) in all the pages of
    your application.
