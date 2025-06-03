!!! note "Available in Taipy Enterprise edition"

    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise).

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

The default page template is a simple and minimal page template which let you create a custom
Taipy page with a few questions. This default template offers an easy way to create a new Taipy
page with a best practice for code organization.

# How to create a page

As its name suggests, the default page template is used if no template name is provided. To create
the page from the default template, change to the folder of the application in which you want to
create the page and run `taipy create --page default` from the CLI. Then answer a few questions to
customize your page.

```console
$ taipy create --page default
[1/2] Page name (page_example):
[2/2] Page folder (pages):

The new Taipy page has been created at pages/page_example
Please import the new page in your main application to use it.
```

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the page. The following sections
describe each question in detail.

1. Page name

- Specifies the name of the page.
- The default value is "page_example".

2. Page folder

- Specifies the path of the folder that contains the generated page.
- The path is relative to the current working directory. The folder will be created if not exist.
- The default value is "pages".

# Page description

The generated page has the following folder structure:

```plaintext
pages/
├──── page_example/
│   ├──── __init__.py
│   └──── page_example.py
│
└──── __init__.py
```

Your page's folder structure may vary depending on the answers you provided during the creation
process. Here is a brief overview of the page structure:

- `pages/`: The folder that contains the page specified in the second question.
    - `page_example/page_example.py` contains the content of the page.
    - `\_\_init\_\_.py` is the file that imports the newly created page in the `pages` package.

# Customizing the page

The default page template is designed to be a minimal starting point for your page. You can
edit the entire content of the page to fit your specific application requirements.

# How to use the page

To use the page in your application, import the page in the main application file along with other
pages and add it to the page list given to the `Gui^` service.

```python title="main.py"
from taipy import Gui
from pages import root_page, page_example

pages = {
    "/": root_page,
    "example": page_example,
}

if __name__ == "__main__":
    gui = Gui(pages=pages)
    gui.run()
```
