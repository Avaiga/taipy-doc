Here are some more indepth examples of Taipy pages.

## Single-page applications

If your application has several pages, you would usually create them with different names,
so the user can navigate from page to page (using the `navigate()^` function or the
[`navbar`](../../../../refmans/gui/viselements/generic/navbar.md) control).<br/>
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

    root_md = "# Multi-page application"
    page1_md = "## This is page 1"
    page2_md = "## This is page 2"

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

## Local resources

Pages sometimes need to access local resources from a page. That is the case for
example if an image needs to be inserted: the path to the image must be provided.

You can indicate, using the parameter *path_mapping* of the
`Gui.__init__^`(`Gui` constructor), where those resources are located on the file
system.

## Status page

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

    If the [*extended_status*](../../../advanced_features/configuration/gui-config.md#p-extended_status) parameter
    is set to True, the dictionary associated with the *gui* key is augmented with runtime
    information of the application, such as the version of the Taipy GUI package that is running,
    the version of the Python interpreter that is running the application, the list of the extension
    libraries that the application has loaded and a few more details.

## How Taipy renders pages

When the rendering of a page occurs, the following steps take place:

- If the page is text-based (Markdown or HTML), the text is parsed to locate the Taipy-specific
  constructs. These constructs designate [*visual elements*](../../../../refmans/gui/viselements/index.md) that can
  represent data and be interacted with by the user. Visual Elements result in the creation of
  potentially complex HTML code;

- The properties of the Visual element are read, and Taipy binds the application variables that are
  used, if any. See the [section about Binding](../../binding.md) for details;

- Potentially, *callbacks* are searched in the visual element properties and connected from the
  rendered page back to the Python code in order to watch user events (the notion of callbacks is
  detailed in the [section about Callbacks](../../callbacks.md)).
