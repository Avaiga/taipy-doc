Pages are the basis for the user interface. Pages hold text, images, or
controls that display information that the application needs to publish and
interact with the application data through visual elements.

# Defining pages

Taipy lets you create as many pages as you require with whatever content you need.

## Defining the page content

Pages can be defined using two different techniques:

- Text templates:<br/>
  You can create textual descriptions of pages (inside the application code or from an external
  file) that will get transformed into HTML content sent and rendered on the client device.<br/>
  This technique comes in two flavors: [Markdown](markdown.md) and [HTML](html.md). You can pick the
  type you feel more comfortable with and create page templates using that type (see note below).
- Python code:<br/>
  you can create pages using Python code exclusively using the APIs provided by the
  [Page Builder](builder.md) package.<br/>
  This package makes it possible to create any visual element, organize them within blocks, and
  create pages to hold them, entirely using the Python language.

!!! tip "Choosing how to create pages"

    Choosing between the Markdown format, HTML content, or Python code depends on several
    parameters:

    - Use [Markdown](markdown.md) when:

        - You need to create a page in a few minutes;
        - You want to benefit from the [Taipy Studio preview](../../../studio/gui.md#page-preview)
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


When the rendering of a page occurs, the following steps take place:

- If the page is text-based (Markdown or HTML), the text is parsed to locate the Taipy-specific
  constructs. These constructs designate [*visual elements*](../viselements/index.md) that can
  represent data and be interacted with by the user. Visual Elements result in the creation of
  potentially complex HTML code;

- The properties of the Visual element are read, and Taipy binds the application variables that are
  used, if any. See the [section about Binding](../binding.md) for details;

- Potentially, *callbacks* are searched in the visual element properties and connected from the
  rendered page back to the Python code in order to watch user events (the notion of callbacks is
  detailed in the [section about Callbacks](../callbacks.md)).

## Registering the page

Once you have created an instance of a page renderer for a specific piece of text or Python code,
you can register that page to the `Gui^` instance used by your application.

The `Gui^` constructor can accept the raw content of a page as Markdown text and create a new page
for you. That would be the easier way to create applications that have a single page. Here is how
you can create and register a page, defined as Markdown content, in a Taipy application:
```python
from taipy import Gui

Gui("# This is my page title")
```
If you run this Python script and connect a browser to the web server address
(usually *localhost:5000*), you can see your title displayed in a blank page.

Of course, the text can be stored in a Python variable and used in the `Gui^`
constructor:
```python
...
md = "# This is my page title"
Gui(md)
```

If your application has several pages, you add your pages one by one
using `Gui.add_page()^`. To add multiple pages in a single call, you will
use `Gui.add_pages()^` or create the `Gui^` instance using the *pages*
argument. In those situations, you have to create a Python dictionary that
associates a page with its name:
```python
...
pages = {
  "page1": Markdown("# My first page"),
  "page2": Markdown("# My second page")
}
Gui(pages=pages)
```

In this situation, to see the pages in your browser, the address you will use
will be *localhost:5000/page1* or *localhost:5000/page2*.

Note that if pages are created in different modules, the variables that they can bind
to visual elements may have a scope limited to their origin module. See
[Page scopes](../binding.md#scope-for-variable-binding) for more details.

## Viewing the page

When the user browser connects to the web server, requesting the indicated page,
the rendering takes place (involving the retrieval of the application variable
values), so you can see your application's state and interact with it.

# Root page

The *Root* page is the page located at the top of the web application.
The name of this page is `"/"` (or the value of the
[*base_url*](../../configuration/gui-config.md#p-base_url) configuration setting).

If your application uses only one page, this is typically where it would be created:
```python
  Gui(page="# Page Content")
```
creates a page from the Markdown content that you provide and adds this page to the new
`Gui` instance with the name `"/"`. This makes it straightforward to watch your application
run by pointing a web browser to the root of the web server address (by default, that would
be `http://127.0.0.1:5000/`).

## Single-page applications

If your application has several pages, you would usually create them with different names,
so the user can navigate from page to page (using the `navigate()^` function or the
[`navbar`](../viselements/standard-and-blocks/navbar.md) control).<br/>
However, you can still have a root page for your application (with the name: `"/"`).
In this situation, Taipy creates a
[single-page application (SPA)](https://en.wikipedia.org/wiki/Single-page_application)
for you.

Modern web applications use this SPA technique: instead of reloading the entire page,
some processing is performed behind the scene to generate the page that should be
displayed, transforming the currently shown page. This allows for smoother
transitions from page to page and feels like the application was natively developed
for your runtime environment.<br/>
Although technically, every Taipy web application *is* a SPA, this notion makes sense only
when using several pages.

If your Taipy application has defined a *root* page, then the content of this page is
generated before the content of the page you need to display. This makes it very easy to
design an application with the same header (such as a banner and a navigation bar)
for all its pages.

!!! example

    Here is an example of a Taipy application that holds several pages:
    ```python
       from taipy import Gui

       root_md="# Multi-page application"
       page1_md="## This is page 1"
       page2_md="## This is page 2"

       pages = {
         "/": root_md,
         "page1": page1_md,
         "page2": page2_md
       }
       Gui(pages=pages).run()
    ```
    When you run this application and display the page at `http://127.0.0.1:5000/`,
    you will notice that the browser navigates to the page `/page1`, and that the
    final result is a page that contains the content of the root page, followed by
    what is defined in the page `"page1"`.<br/>
    In this example, you will see both the main title ('Multi-page application') and
    the sub-title ('This is page 1').

    If you navigate to '/page2', the main title remains on the page, and the sub-title
    is replaced by the text 'This is page 2'

!!! tip "Running multiple services"

    If you need to run the Taipy GUI service with other Taipy services, you may need
    to refer to the [Running Taipy services](../../../run-deploy/run/running_services.md)
    section.

## The `<|content|>` pseudo-control

Your application may also need to hold a footer on all the pages it uses.<br/>
You can use the pseudo-control `<|content|>` to achieve the expected result: this
visual element is not *really* a control: It is a placeholder for page content, used in the
root page of your application, and is replaced by the target page content when the application
runs.

!!! example

    ```python
       from taipy import Gui

       root_md="""
       # Multi-page application

       <|content|>

       This application was created with [Taipy](https://www.taipy.io/).
       """
       page1_md="## This is page 1"
       page2_md="## This is page 2"

       pages = {
         "/": root_md,
         "page1": page1_md,
         "page2": page2_md
       }
       Gui(pages=pages).run()
    ```
    This application does the same as in the previous example, except that you now
    have the footer line (*'This application was created...'*) in all the pages of
    your application.

# Dialogs

Applications sometimes need to prompt the user to indicate a situation or request
input of some sort. Dialogs are forms that can be displayed on top of the page
the user is looking at, prompting for some input.

To create a dialog, you will use a [`dialog`](../viselements/standard-and-blocks/dialog.md) control in your
page. The dialog holds a page content or a *Partial* (see [Partials](#partials)).

You can control whether the dialog is visible or not, and what to do when the end-user
presses the *Validate* or *Cancel* button, so your application can deal with the
user's response.

!!! example

    Here is an example of how you would create a dialog, directly in your Markdown
    content:

    ```python
       ...
       page="""
       ...
       <|{dialog_is_visible}|dialog|
       Enter a name:

       <|{name}|input|>
       |>
       ...
       """

       Gui(page).run()
    ```

Please refer to the documentation page on the [`dialog`](../viselements/standard-and-blocks/dialog.md)
control for more details and examples.

# Partials

There are page fragments that you may want to repeat on different pages. In that situation,
you will want to use the *Partial* concept: a *Partial* is similar to a page (and built
in a very similar way) that can be used multiple times in different visual elements.
This prevents you from having to repeat yourself when creating your user interfaces.

To create a *Partial*, you must call the method `(Gui.)add_partial()^` on the *Gui*
instance of your application. You must give this function a page definition (a string or
an instance of `Markdown^` or `Html^`), and it returns an instance of `Partial^` that can
be used in visual elements that use them.

!!! example

    Here is an example of how you would create a `Partial^`, in the situation where the
    dialog created in the [example above](#dialogs) would be needed in different pages:

    ```python
       ...
       gui = Gui()
       prompt_user = gui.add_partial(
         """
         Enter a name:

         <|{name}|input|>
         """
       )
       gui.run()
    ```

You can take a look at the documentation of the [`dialog`](../viselements/standard-and-blocks/dialog.md) or
[`pane`](../viselements/standard-and-blocks/pane.md) to see how these *Partials* can be used in pages.

# Panes

Modern user interfaces also provide small pages that pop out and be removed for
temporary use, such as providing specific parameters for the application. Taipy lets
you create such elements using the [pane](../viselements/standard-and-blocks/pane.md) block.

A pane can appear from any border of your page, next to or on top of the page, and
disappears when the user clicks outside its area.

A pane can be defined using the `Partial^` class, or directly in the page
definition.

# Local resources

Pages sometimes need to access local resources from a page. That is the case for
example if an image needs to be inserted: the path to the image must be provided.

You can indicate, using the parameter *path_mapping* of the
`Gui.__init__^`(`Gui` constructor), where those resources are located on the file
system.

# Status page

The *Status* page is a special page that the user can access by requesting the page at
"/taipy.status.json".

This returns a customizable JSON representation of the state of the application as a dictionary
where the key "gui" is set to a dictionary containing the information you might need to dig into
the state of the application without changing the definition of the pages.

The "user_status" key of the "gui" entry is set to a dictionary that is initialized by
the user-defined *on_status()* global function. This function is invoked when the end-user
requests the "/taipy.status.json" page; it receives a single argument: the current application
*state* (an instance of the `State^` class).<br/>
This function should return a dictionary where you can define any key or value of your choice.

Here is a short example to demonstrate the status page customization:

```python
from taipy.gui import Gui, State

x = 1234

def on_status(state: State):
    return {
        "x": state.x,
        "info": "Some information..."
    }

Gui(page="""
# Status page

Value of x: <|{x}|>
""").run()
```

When this application is running, the "/taipy.status.json" page shows a JSON representation of
a dictionary with a single key, "gui". The value associated with this key is another dictionary
with the single key, "user_status". And the value associated with that key is the dictionary
returned by *on_status()*.<br/>
In this example, *gui.user_status.x* is set to 1234 (as initialized in the application), and
*gui.user_status.info* is the string defined in the *on_status()* function.

!!! note "Extended status"

    If the [*extended_status*](../../configuration/gui-config.md#p-extended_status) parameter
    is set to True, the dictionary associated with the *gui* key is augmented with runtime
    information of the application, such as the version of the Taipy GUI package that is running,
    the version of the Python interpreter that is running the application, the list of the extension
    libraries that the application has loaded and a few more details.
