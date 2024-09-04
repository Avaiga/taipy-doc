Taipy GUI pages can be defined using the [HTML](https://en.wikipedia.org/wiki/HTML)
markup language.

If you are somehow experienced in developing web user interfaces, you may want to use raw HTML
to describe pages, so you have all the power of the HTML grammar to organize your page content.

You do not need to create the header and body parts, as Taipy takes care of this for you.

Creating a page that displays HTML content needs the application to create an instance of the
`Html^` class:
```python
from taipy.gui import Html

if __name__ == "__main__":
    html_page = Html("""
<h1>Page title</h1>

Any <a href="https://en.wikipedia.org/wiki/HTML"><i>HTML</i></a>
content can be used here.

<taipy:button>Press</taipy:button>
    """)

    Gui(page).run()
```

The *html_page* variable holds a page whose content is defined from HTML text.

Taipy identifies visual element definitions by finding tags that belong to the `taipy` namespace.
You can find details on how to create visual elements using HTML in the
[HTML Syntax](../../gui/viselements/introduction.md#html) section about Visual Elements definition.

# XHTML is required

When Taipy GUI renders the page, it parses the text content to locate the potential visual element
tags and convert them into new HTML code.<br/>
This process requires the HTML content to be expressed as [XHTML](https://www.w3.org/TR/xhtml1/).
XHTML (which stands for "Extensible Hypertext Markup Language") is a markup language that mirrors
HTML but adheres to the stricter syntax rules of XML (Extensible Markup Language).

Here are the rules that the page definition must follow:
- The HTML content must be a well-formed XML document (although it does not need a root
  element).<br/>
    - Every opening tag must be explicitly closed.<br/>
      For example, although HTML accepts the tag `<img src="...">`, XHTML does not. You must
      indicate where the `img` tag ends.<br/>
      That can be `<img src="..."/>` or `<img src="..."></img>`.
    -
- Strict adherence to syntax rules is required. All elements must be properly nested, closed, and in
  lowercase.
    - All the tag names must be lowercase.
    - All the attribute names must be lowercase, and all values must be quoted.<br/>
      Note that the XHTML syntax parsed by Taipy GUI in the context of a visual element allows for
      leaving an attribute valueless. The value for the property is then set to True.

# Event handlers

You cannot declare event handlers explicitly in HTML elements because Taipy GUI cannot use the event
handlers' attribute value.

Here is an example of HTML content in this situation. A Taipy application creates a page entirely
defined in HTML as follows:
```python linenums="1"
from taipy.gui import Gui, Html

if __name__ == "__main__":
    page = Html("""
<!DOCTYPE html>
<html>
<head>
    <title>Invoking JavaScript</title>
    <script type="text/javascript">
        function send_alert() {
            alert("Just got an alert!")
        }
    </script>
</head>
<body>
    <h1>Sending an alert</h1>
    <button id="alert_button" onclick="send_alert();">Send alert</button>
</body>
</html>
    """)

    Gui(page).run()
```

In line 16, you can spot where the HTML button is created, along with its event handler: the
function *send_the_alert()*, defined in line 9, should be called when the user presses the button.

But if you run this application and press the button, you will *not* observe the invocation of the
function. That is because when Taipy converts the HTML input into the page sent to the browser, it
removes the event handlers of the HTML elements.

To fix this problem, you must set the event handler by code when the JavaScript code runs on the
client.<br/>
Here is a version of the variable *page* that fixes the problem:

```python linenums="4"
    page = Html("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Invoking JavaScript</title>
        <script type="text/javascript">
            function send_the_alert() {
                alert("Just got an alert!")
            };
            const alert_button = document.getElementById("alert_button");
            alert_button.addEventListener("click", send_the_alert);
        </script>
    </head>
    <body>
        <h1>Sending an alert</h1>
        <button id="alert_button">Send alert</button>
    </body>
    </html>
    """)
```

Notice that, in line 18, where the button element is defined, the setting of the event handler has
disappeared. Instead, in lines 12 and 13, we indicate that the function should be invoked when the
button emits the "click" event.
