!!! note "Available in Taipy Enterprise edition"

    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise).

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

In a Taipy application, it's essential for the user to manage data nodes effectively. During the
development process of a Taipy application, adding a page to manage data nodes is a common
requirement.

To reduce the development time, Taipy provides a data management page template, which is designed
as a best practice page for managing data nodes in a Taipy application.

<figure>
  <img src="../img/dmp_template_dark.jpeg" class="visible-dark" />
  <img src="../img/dmp_template_light.jpeg" class="visible-light"/>
  <figcaption>Out-of-the-box Taipy data node management page</figcaption>
</figure>

Out-of-the-box, the data management page allows the user to perform various operations on the data
nodes, including:
- filtering, sorting, searching for data nodes
- selecting data nodes
- uploading and editing the data of the selected data node
- visualizing the content of the selected data node

# How to create a page

To create the page from the data management page template, change to the folder of the application in
which you want to create the page and run `taipy create --page data_management` from the CLI. Then
answer a few questions to customize your page.

```console
$ taipy create --page data_management
[1/3] Page name (data_node_management_page):
[2/3] Page folder (pages):
[3/3] If the following variable needs to be bound to an existing variable,
please specify the module and the variable name separated by a space
(for example, ".root selected_data_node"):
selected_data_node ():

The new Taipy page has been created at pages/data_node_management_page

The "selected_data_node" variable has been created for the page.
Please import the new page in your main application to use it.
```

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the page. The following sections
describe each question in detail.

1. Page name

- Specifies the name of the page.
- The default value is "data_node_management_page".

2. Page folder

- Specifies the path of the folder that contains the generated page.
- The path is relative to the current working directory. The folder will be created if not exist.
- The default value is "pages".

3. Bind the *selected_data_node* variable

- The *selected_data_node* variable stores the data node selected by the user in the page.
- By default, the variable is defined in the page. You can import this variable to another page to
    share the data node selected by the user. For more information, please refer to
    [Binding variables](../../userman/gui/binding.md).
- If there is already an existing variable with the same purpose from a different page, please
    specify the module and the variable name separated by a space. It will be imported automatically
    to the data node management page. For example, if there is a *selected_dn* variable in the root
    page and you want to bind that to the data controls, you can specify ".root selected_dn".

# Page description

The generated page has the following folder structure:

```plaintext
pages/
├──── data_node_management_page/
│   ├──── __init__.py
│   └──── data_node_management_page.py
│
└──── __init__.py
```

Your page's folder structure may vary depending on the answers you provided during the
creation process. Here is a brief overview of the page structure:

- `pages/`: The folder that contains the page specified in the second question.
    - `data_node_management_page/data_node_management_page.py` contains the layout and content of
    the page. It includes a sidebar holding a
    [data_node_selector](../../refmans/gui/viselements/corelements/data_node_selector.md)
    visual element, and a main content area showing a
    [data_node](../../refmans/gui/viselements/corelements/data_node.md) visual element.
    - `\_\_init\_\_.py` is the file that exports the page from the `pages` package.

# Customizing the page

Everything in the generated page can be updated to precisely fit your specific requirements.

The grid layout of the page can be customized via a
[layout](../../refmans/gui/viselements/generic/layout.md) block.

You can also customize the
[data_node_selector](../../refmans/gui/viselements/corelements/data_node_selector.md)
and [data_node](../../refmans/gui/viselements/corelements/data_node.md) controls which
allow the user to select and manage the data nodes respectively.

You can also add more content to the page such as descriptions, or other
[visual elements](../../refmans/gui/viselements/index.md) provided by Taipy to enrich the
user experience.

# How to use the page

To use the page in your application, import the page in the main application file along with other
pages and add it to the page list given to the `Gui^` service.

```python title="main.py"
from taipy import Gui
from pages import root_page, data_node_management_page

pages = {
    "/": root_page,
    "data": data_node_management_page,
}

if __name__ == "__main__":
    gui = Gui(pages=pages)
    gui.run()
```

You can also explicitly import the variable *selected_data_node* from the newly created page to a
different page to share the data node selected by the user.
