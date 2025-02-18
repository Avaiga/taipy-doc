!!! note "Available in Taipy Enterprise edition"

    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise).

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

In a Taipy application, the root page defines the overall layout of the application. During the
development process of a Taipy application, adding a root page is a common practice to provide an
entry point for the application.

To reduce the development time, Taipy provides a root page template, which is designed as a best
practice page for a Taipy root page.

Out-of-the-box, the root page defines the overall layout of the application, including the title,
navigation bar, and the content area.

This page template offers several key benefits:

- **Ease of Use**: The page template is designed to be user-friendly, with a simple CLI
    interface that guides developers through the page creation process on top of existing
    application. The pages then can be easily customized and plugged into the application.
- **Customization**: The template provides high flexibility and customization options on page
    creation, allowing developers to tailor the page to meet specific requirements and use cases.

# How to create a page

<!-- TODO: The root page should be the final page of the application. -->

To create the page from the root page template, change to the folder of the application in which
you want to create the page and run `taipy create --page root` from the CLI. Then answer a few
questions to customize your page.

```console
$ taipy create --page root
  [1/4] Page title (root):
  [2/4] The folder that contains the pages (pages):
  [3/4] Application title (Taipy Application):
  [4/4] Variable that contains the dictionary of application pages (pages):

New Taipy root page has been created at ./pages/root.py
To use the root page, please import it in your main application and make sure the main application contains the "pages" dictionary of the pages.

For more information, please refer to the Multi-page application tutorial at https://docs.taipy.io/en/latest/tutorials/visuals/3_multipage_application/
```

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the page. The following
sections describe each question in detail.

## 1. Page title

- Specifies the title of the page.
- The default value is "data_node_management_page".

## 2. The folder that contains the pages

- Specifies the path of the folder that contains the generated page.
- The path is relative to the current working directory. The folder will be created if not exist.
- The default value is "pages".

## 3. Application title

- Specifies the title of the application.
- The default value is "Taipy Application".

## 4. Variable that contains the dictionary of application pages

- Specifies the variable that contains the dictionary of application pages in the main application.
    - For a multi-page Taipy application, it is recommended to provide a dictionary of pages to the
       `Gui^` service.
    - This is used to build the navigation bar.
    - If the variable does not exist in the main application, an error will be raised when running
       the application.
- The default value is "pages".

# Page description

The generated page has the following folder structure:

```plaintext
pages/
├──── root.py
│
└──── __init__.py
```

Your page's folder structure may vary depending on the answers you provided during the
creation process. Here is a brief overview of the key components:

- *pages/*: The folder that contains the page specified in the second question.
    - *root.py* contains the content of the newly created root page.
    - *\_\_init\_\_.py* is the file that imports the newly created page in the `pages` package.

# Customizing the page

Everything in the generated page can be updated to precisely fit your specific requirements.

The grid layout of the page can be customized via the
[layout](../../refmans/gui/viselements/generic/layout.md) visual element.

You can also customize the you can customize the navigation bar of the application with the
[navbar](../../refmans//gui/viselements/generic/navbar.md) visual element and the `creates_pages()`
method which is used to create the items of the navigation bar.

There are also several content placeholders. You can edit the content of these placeholder or add
more content to the page such as descriptions, or other
[visual elements](../../refmans/gui/viselements/index.md) provided by Taipy to fit your specific
application requirements and enrich the user experience.

# How to use the page

To use the page in your application, import the page in the main application file along with other
pages and add it to the page list given to the `Gui^` service.

```python title="main.py"
from taipy import Gui
from pages import root_page

pages = { "/": root_page }

if __name__ == "__main__":
    gui = Gui(pages=pages)
    gui.run()
```
