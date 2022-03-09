# Pages

Pages are the base for your user interface. Pages hold text, images, or controls that
display information that the application needs to publish and interact with
the application data through visual elements.

## Page renderers

Taipy lets you create as many pages as you want, with whatever content you need.
Pages are created using _page renderers_, which convert some text (inside the application
code or from an external file) into HTML content sent and rendered onto the client
device.

!!! note
    A _page rendered_ is an instance of a Python class that reads some text (directly from a
    string or reading a text file) and converts it into a page that can be displayed in a browser.

There are different types of page renderers in Taipy, and all process their input text
with the following steps:

- The text is parsed to locate the Taipy-specific constructs. Those constructs let you
  insert _visual elements_ that can be _controls_ or _blocks_. Visual Elements result in
  the creation of potentially complex HTML components;
- Control (and block) properties are read, and all referenced application variables are
  bound.
- Potentially, _callbacks_ are located and connected from the rendered page back to the Python code
  if you want to watch user events (the notion of callbacks is detailed in the section [Callbacks](user_callbacks.md)).

### Registering the page

Once you have created an instance of a page renderer for a specified piece of
text, you can register that page to the `Gui^` instance used by your application.

### Viewing the page

When the user browser connects to the Web server, requesting the indicated page,
the rendering takes place (involving the retrieval of the application variable
values), so you can see your application's state and interact with it.

### Markdown processing

One of the page description formats is the [Markdown](https://en.wikipedia.org/wiki/Markdown)
markup language.

Taipy uses [Python Markdown](https://python-markdown.github.io/) to translate Markdown
text to elements used to create Web pages. It also uses many extensions that
make it easier to create nice-looking pages that users can enjoy. Specifically,
Taipy uses the following [Markdown extensions](https://python-markdown.github.io/extensions/):
[_Admonition_](https://python-markdown.github.io/extensions/admonition/),
[_Attribute Lists_](https://python-markdown.github.io/extensions/attr_list/),
[_Fenced Code Blocks_](https://python-markdown.github.io/extensions/fenced_code_blocks/),
[_Meta-Data_](https://python-markdown.github.io/extensions/meta_data/),
[_Markdown in HTML_](https://python-markdown.github.io/extensions/md_in_html/),
[_Sane Lists_](https://python-markdown.github.io/extensions/sane_lists/)
and [_Tables_](https://python-markdown.github.io/extensions/tables/).
Please refer to the Python Markdown package documentation to get information on how these are used.

Besides these extensions, Taipy adds its own extension that can parse Taipy-specific
constructs that allow for defining visual elements (and all the properties they need).

The basic syntax for creating Taipy constructs in Markdown is: `<|...|...|>` (opening with a
_less than_ character immediately followed by a vertical bar character &#151; sometimes called
_pipe_ &#151; followed a potentially empty series of vertical bar-separated fragments and closing
by a vertical bar character immediately followed by the _greater than_ character).<br/>Taipy
will interpret any text between the `<|` and the `|>` markers and try to make sense of it.

The most common use of this construct is to create controls. Taipy expects the control type
name to appear between the two first vertical bar characters (like in `<|control|...}>`.

!!! important
    If the first fragment text is not the name of a control type, Taipy will consider this
    fragment to be the default value for the default property of the control, whose type name
    must then appear as the second element.

Every following element will be interpreted as a property name-property value pair
using the syntax: _property\_name=property\_value_ (note that all space characters
are significative).  

!!! note "Shortcut for Boolean properties"
    Should the `=property_value` fragment be missing, the property value is interpreted as the
    Boolean value `True`.<br/>
    Furthermore if the property name is preceded by the text "_no&blank;_", "_not&blank;_",
    "_don't&blank;_" or "_dont&blank;_" (including the trailing space character) then no
    property value is expected, and the property value is set to `False`.

#### Some examples

!!! example "Multiple properties"
    You can have several properties defined in the same control fragment:
    ```
    <|button|label=Do something|active=False|>
    ```

!!! example "The _default property_ rule"
    The default property name for the control type [`button`](viselements/button.md) is _label_. In Taipy,
    the Markdown text
    ```
    <|button|label=Some text|>
    ```
    Is exactly equivalent to
    ```
    <|Some text|button|>
    ```
    which is slightly shorter.

!!! example "The _missing Boolean property value_ rules"
    ```
    <|button|active=True|>
    ```
    is equivalent to
    ```
    <|button|active|>
    ```
    And
    ```
    <|button|active=False|>
    ```
    is equivalent to
    ```
    <|button|not active|>
    ```

There are very few exceptions to the `<|control_type|...|>` syntax, and these exceptions
are described in their respective documentation section. The most obvious exception is the
[`text`](viselements/text.md) control, which can be created without even mentioning its
type.

### HTML specifics

!!! abstract "TODO: HTML specifics documentation"

## Root page

The _Root_ page is the page located at the top of the Web application.
The name of this page is `"/"`.

If your application uses only one page, this is typically where it would be created:
```py
  Gui(page="# Page Content")
```
creates a page from the Markdown content that you provide and adds this page to the new
`Gui` instance with the name `"/"`. This makes it straightforward to watch your application
run by pointing a Web browser to the root of the Web server address (by default, that would
be `http://127.0.0.1:5000/`).

### Single-page applications

If your application has several pages, you would usually create them with different names,
so the user can navigate from page to page (using the `navigate()^` function or the
[`navbar`](../viselements/navbar/) control).<br/>
However, you can still have a root page for your application (with the name: `"/"`).
In this situation, Taipy creates a
[single-page application (SPA)](https://en.wikipedia.org/wiki/Single-page_application)
for you.

Modern Web applications use this SPA technique: instead of reloading the entire page,
some processing is performed behind the scene to generate the page that should be
displayed, transforming the currently shown page. This allows for smoother
transitions from page to page and feels like the application was natively developed
for your runtime environment.<br/>
Although technically, every Taipy Web application *is* a SPA, this notion makes sense only
when using several pages.

If your Taipy application has defined a _root_ page, then the content of this page is
generated before the content of the page you need to display. This makes it very easy to
design an application with the same header (such as a banner and a navigation bar)
for all its pages.

!!! example

    Here is an example of a Taipy application that holds several pages:
    ``` py linenums="1"
       from taipy.gui import Gui

       root_md="# Multi-page application"
       page1_md="## This is page 1"
       page2_md="## This is page 2"

       pages = {
         "/": root_md,
         "page1": page1_md,
         "page1": page2_md
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

### The `<|content|>` pseudo-control

Your application may also need to hold a footer on all the pages it uses.<br/>
You can use the pseudo-control `<|content|>` to achieve the expected result: this
visual element is not _really_ a control: It is a placeholder for page content, used in the
root page of your application, and is replaced by the target page content when the application runs.

!!! example

    ``` py linenums="1"
       from taipy.gui import Gui

       root_md="""
       # Multi-page application

       <|content|>

       This application was created with [Taipy](http://taipy.avaiga.com).
       """
       page1_md="## This is page 1"
       page2_md="## This is page 2"

       pages = {
         "/": root_md,
         "page1": page1_md,
         "page1": page2_md
       }
       Gui(pages=pages).run()
    ```
    This application does the same as in the previous example, except that you now
    have the footer line (_'This application was created...'_) in all the pages of
    your application.

## Partials

There are page fragments that you may want to repeat on different pages. In that situation,
you will want to use the `Partials` concept described below. This prevents you from
having to repeat yourself when creating your user interfaces.

!!! abstract "TODO: partials documentation"

## Dialogs

Applications sometimes need to prompt the user to indicate a situation or request
input of some sort. This need is covered in Taipy using the [dialog](user_dialogs.md)
control demonstrated below.

!!! abstract "TODO: dialogs documentation"

## Panes

Modern user interfaces also provide small pages that pop out and be removed for
temporary use, such as providing specific parameters for the application. Taipy lets
you create such elements as described below.

!!! abstract "TODO: panes documentation"

## Local resources

!!! abstract "TODO: local resources documentation"
