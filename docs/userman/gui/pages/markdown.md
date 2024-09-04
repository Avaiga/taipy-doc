Taipy GUI pages can be defined using the [Markdown](https://en.wikipedia.org/wiki/Markdown)
markup language.

Markdown is a lightweight markup language widely used for creating documentation pages. This would
be the ideal format if you are not familiar with web page definition or would like to create a good
visual rendering quickly.<br/>
Taipy has an augmented implementation of Markdown that makes it simple to organize the page content
in sections or grids.

!!! note "Markdown extensions"
    Taipy uses [Python Markdown](https://python-markdown.github.io/) to translate Markdown
    text to web pages. Many language extensions are used to make it easier to create
    nice looking pages that users can enjoy. Specifically, Taipy uses the following
    [Markdown extensions](https://python-markdown.github.io/extensions/):

    - [*Admonition*](https://python-markdown.github.io/extensions/admonition/),
    - [*Attribute Lists*](https://python-markdown.github.io/extensions/attr_list/),
    - [*Fenced Code Blocks*](https://python-markdown.github.io/extensions/fenced_code_blocks/),
    - [*Meta-Data*](https://python-markdown.github.io/extensions/meta_data/),
    - [*Markdown in HTML*](https://python-markdown.github.io/extensions/md_in_html/),
    - [*Sane Lists*](https://python-markdown.github.io/extensions/sane_lists/),
    - [*Tables*](https://python-markdown.github.io/extensions/tables/).

    Please refer to the Python Markdown package documentation to get information on how to use
    these.

Creating a page that displays Markdown content is very straightforward:

```python
from taipy.gui import Markdown

md_page = Markdown("""
# Page title

Any [*Markdown*](https://en.wikipedia.org/wiki/Markdown) content can be used here.
""")
```

The *md_page* variable contains the definition of a page whose content is defined by Markdown text.

!!! note "Markdown link syntax"
    You can use Markdown's native *link* syntax to easily create links
    from one page to another.

    If, for example, your application has two pages (see in the [section on Page](index.md) how to
    create such an application, where pages would be called "page1" and "page2"), you can create a
    link to "page2" from "page1" by adding the following Markdown fragment in the definition of
    "page1":
    ```
    ...
    Go to [Second Page](/page2) for more information.
    ...
    ```

Besides the extensions listed above, Taipy adds its own extension that can parse
Taipy-specific constructs that allow for defining visual elements (and all the properties
they need). The details on how visual elements are located and interpreted with Markdown
content can be found in the [Markdown Syntax](../../gui/viselements/introduction.md#markdown) section
about Visual Elements definition.

!!! tip "Commenting Markdown"
    The Markdown syntax does not explicitly indicate how to insert comments in the text.
    However, you can use a link-like construct as a new line in the Markdown body:<br/>
    Both:
    ```
    [//]: <> (This is a comment.)
    ```
    and
    ```
    [//]: # (This is another comment.)
    ```
    will be ignored as long as they appear as a single line in the Markdown content.
