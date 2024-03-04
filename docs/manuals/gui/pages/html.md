Taipy GUI pages can be defined using the [HTML](https://en.wikipedia.org/wiki/HTML)
markup language.

If you are somehow experienced in developing web user interfaces, you may want to use raw HTML
to describe pages, so you have all the power of the HTML grammar to organize your page content.

You do not need to create the header and body parts, as Taipy takes care of this for you.

Creating a page that displays HTML content is simple:

```python
from taipy.gui import Html

html_page = Html("""
<h1>Page title</h1>

Any <a href="https://en.wikipedia.org/wiki/HTML"><i>HTML</i></a>
content can be used here.
""")
```

The *html_page* variable contains the definition of a page whose content is defined from HTML text.

Taipy identifies visual element definitions by finding tags that belong to the `taipy` namespace.
You can find details on how to create visual elements using HTML in the
[HTML Syntax](../viselements/index.md#html) section about Visual Elements definition.

