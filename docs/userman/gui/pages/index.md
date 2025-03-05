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

# Multi-page applications

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

# Page modules {data-source="gui/examples/grocery_store"}

In Taipy, a Page represents a specific part of the whole web interface. While it is possible to
define a single-page application directly within the main script, real-world applications typically
require multiple pages to structure different views and functionalities.

To improve maintainability and modularity, it is a good practice to define each page in a specific
Python module where each individual page is defined. We call such a module a **Page Module**,
because it is an actual Python module and because it defines... a page.<br/>
Modules are typically grouped within a dedicated directory (e.g., `pages/`) and imported into the
main script. This approach enhances code organization, making it easier to manage, update, and
scale an application.

Page Modules provide benefits in different areas:

- **Code Organization**: Keeping page definitions in separate files avoids clutter in the main
  script.
- **Scalability**: Applications can easily add, remove, and manage multiple pages as they grow.
- **Reusability**: Page definitions can be reused across different projects or parts of the
  application.
- **Maintainability**: Changes to a specific page can be made without affecting unrelated parts of
  the application.

To demonstrate how to structure a Taipy application using Page Modules, here is a simplified version
of an application showcasing how to define, organize, and import pages efficiently.<br/>
Our example application provides a user interface for analyzing sales performance and stock status
in a grocery store. The dataset behind this application contains key business metrics for some
items.<br/>
The dataset used in this example is as follows:
```python
data = {
    "Items": ["Apples", "Bananas", "Oranges", "Grapes", "Strawberries"],
    "Purchase": [1.36, 0.73, 1.09, 2.27, 2.73],
    "Price $": [1.50, 0.80, 1.20, 2.50, 3.00],
    "Price €": [1.38, 0.74, 1.10, 2.30, 2.76],
    "Sales Q1": [120, 200, 90, 50, 75],
    "Sales Q2": [140, 180, 110, 60, 85],
    "Sales Q3": [100, 190, 95, 55, 80],
    "Stock":  [500, 600, 400, 300, 250]
}
```
This dataset contains inventory and sales data for five different fruit items. It includes
information on:

- Purchase Prices: The cost of acquiring each item.
- Selling Prices: Prices in both USD ($) and EUR (€).
- Quarterly Sales Data: Sales volumes for Q1, Q2, and Q3.
- Stock Levels: The current stock count for each item.

This dataset enables analysis of sales performance across quarters and the valuation of remaining
stock based on purchase prices.

The application consists of two main pages: "Stock" and "Sales." Each page is independent, making
them well-suited for implementation as separate Page Modules.<br/>
For our example, the two pages are defined in two distinct module files, in the same directory
called "grocery_store".

This example demonstrates how pages can be defined in module, and how variables that are declared
locally can be bound to those pages' visual element properties, keeping the scope of the variable
local to their actual usage. The principle is that pages defined in a Page Module can reference
variables defined within the same module without needing to export them. Pages defined in a page
module can also reference variables from the main script.

## Defining a page in a module

The 'Stock' page provides an overview of the store's stock, and is implemented in its own
module (see the [full source code](http://TAIPY_REPO/doc/gui/examples/grocery_store/stock.py)).

The page contains two main elements:

- A [`text`](../../../refmans/gui/viselements/generic/text.md) control displays the total stock
  value.
- A table displays the "Items" and "Stock" columns. This table is placed inside an
  [`expandable`](../../../refmans/gui/viselements/generic/expandable.md) block, allowing it to be
  shown or hidden.

Here is a slightly simplified code for the Stock page module:
```python linenums="1" title="stock.py"
from taipy.gui import Markdown

show_details = False

def compute_stock_value(data: dict[str, list[float]]) -> float:
    return sum([v * n for v, n in zip(data["Purchase"], data["Stock"])])

page = Markdown("""
Stock value: $<|{compute_stock_value(data)}|>

<|Stock details|expandable|expanded={show_details}|
<|{data}|table|columns=Items;Stock|>
|>""")
```

Code breakdown:

- On line 3, we define the variable *show_details* that controls the visibility of the expandable's
  content.<br/>
  This variable is bound to the *expanded* property of the `expandable` block on line 11
- On line 5 and 6, we define the function that is referred to as the expression in the `text`
  control declared in line 9. This function computes the total value of the stock by multiplying
  each item's stock quantity by its purchase price, then sums the values.
- On line 8 to 13, we define the page.<br/>

Note that the variable *data*, referenced by the text element on line 9, is defined in the
[main script](http://TAIPY_REPO/doc/gui/examples/grocery_store.py#L24): as stated above, pages
defined in page modules can reference all global variables.<br/>
*show_details*, on the other hand, is a local variable for that module. It is handy to be able to
define it at the module level since no other module in the application has any use of this variable.

The page is imported and registered in the main script with the following lines:
```python title="grocery_store.py"
from grocery_store.stock import page as StockPage
...
Gui(pages={ "stock": StockPage }).run()
```

## Defining a page as a class

If you prefer an object-oriented approach, you can store page-specific variables inside a dedicated
class. This allows for better encapsulation and organization.<br/>
The 'Sales' page displays the total sales for a selected quarter. Users can choose a quarter and a
currency, and the page dynamically computes the total sales and displays a table of sales
figures.<br/>
The full source code for this page can be downloaded from
[this link](http://TAIPY_REPO/doc/gui/examples/grocery_store/sales.py).

The page contains four main elements:

- A [`selector`](../../../refmans/gui/viselements/generic/selector.md) control to choose the quarter
  for which sales are computed (Q1, Q2, or Q3);
- A [`text`](../../../refmans/gui/viselements/generic/text.md) element that displays the total sales
  for the selected quarter;
- A [`toggle`](../../../refmans/gui/viselements/generic/toggle.md) button that allows users to
  switch between USD ($) and EUR (€) for currency selection;
- A [`table`](../../../refmans/gui/viselements/generic/table.md) that displays items and their
  respective revenue for Q1, Q2, and Q3

Since the selected quarter and currency are not used by other pages in the application, it is best
to define them within a tight scope.</br>
Encapsulating these page-specific variables inside a class is a way to ensure they remain
self-contained and easy to manage.

Here is a slightly simplified version of the 'Sales' page class, defined in its own module:
```python linenums="1" title="sales.py"
class SalesPage(Page):
    def __init__(self) -> None:
        self.quarter = "Q1"  # Default selected quarter
        self.currency = "$"  # Default currency
        super().__init__()

    @staticmethod
    def compute_total(quarter: str, currency: str, data: dict[str, list[float]]) -> float:
        sold = data[f"Sales {quarter}"]
        price = data[f"Price {currency}"]
        return sum(s * p for s, p in zip(sold, price))

    def create_page(self):
        return """
Select quarter: <|{quarter}|selector|lov=Q1;Q2;Q3|>

Total: <|{SalesPage.compute_total(quarter, currency, data)}|format=%.02f|><br/>
Currency: <|{currency}|toggle|lov=$;€|>

<|{data}|table|columns=Items;Sales Q1;Sales Q2;Sales Q3|>
"""
```

Code breakdown:

- Line 1: The class *SalesPage* is a subclass of `taipy.gui.Page^`.
- Lines 2 to 5: The class constructor initializes two instance variables:
    - *quarter* (initial value: "Q1") – The selected quarter.
    - *currency* (initial value: "$") – The selected currency.
  These instance variables can be bound to visual elements, as shown below.
- Lines 7–11: The *compute_total()* function calculates the total sales for the given quarter and
  currency by multiplying the sales volume by the corresponding price.<br/>
  This function is declared as static because Taipy applications support multiple users
  simultaneously. If *compute_total(*) were an instance method, all users would share the same class
  instance, which could cause incorrect values when different users select different quarters or
  currencies. Instead, variable binding ensures that the function is invoked with the correct
  state-dependent variables.
- Lines 13 to 21: The `Page.create_page()^` method is overridden to define the page content.<br/>
  Since this method returns a string, it is automatically interpreted as a `Markdown^` page.<br/>
  On line 17, the text element displays the formatted return value of *compute_total()*. This
  function is invoked with the instance variables *quarter* and *currency*, and also the *data*
  variable, which is defined in the main module.

A key advantage of this approach is that page-specific variables (*quarter* and *currency*) are
encapsulated within the class:

- These variables are not exposed globally, keeping them isolated from the rest of the application.
- This ensures that changes to one page do not affect other parts of the application, improving
  modularity and maintainability.

The page is imported and registered in the main script with the following lines:
```python title="grocery_store.py"
from grocery_store.sales import SalesPage
...
Gui(pages={ "sales": SalesPage() }).run()
```
