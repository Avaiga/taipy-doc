!!! note "Available in Taipy Enterprise edition"

    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise).

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

In a Taipy application with complex scenarios, it's essential for the user to be able to manage
the scenarios and data nodes effectively. During the development process of such application, a
page to manage scenarios is essential.

To reduce the development time, Taipy provides a scenario management page template, which is
designed as a best practice page for managing scenarios and data nodes in a Taipy application by
leveraging Taipy visual elements.

<figure>
  <img src="../img/sdp_template_dark.jpeg" class="visible-dark" />
  <img src="../img/sdp_template_light.jpeg" class="visible-light"/>
  <figcaption>Out-of-the-box Taipy scenario management page</figcaption>
</figure>

Out-of-the-box, the scenario management page allows the user to perform various operations on
scenarios and data nodes, including:
- select a scenario
- view the directed acyclic graph (DAG) of the selected scenario
- manage and visualize selected scenario's data nodes
- submit the selected scenario for execution

# How to create a page

To create the page from the scenario page template, change to the folder of the application in
which you want to create the page and run `taipy create --page sdm` from the CLI. Then answer a few
questions to customize your page.

```console
$ taipy create --page sdm
  [1/4] Page title (scenario_management_page):
  [2/4] Page folder (pages):
  [3/4] If the following variables need to be bound to an existing variables,
please specify the module and the variable name separated by a space
(e.g. .root selected_scenario):
selected_scenario ():
  [4/4] selected_data_node ():

The new Taipy page has been created at pages/scenario_management_page

The following variables have been created for the page: selected_scenario, selected_data_node.
Please import the new page in your main application to use it.
```

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the page. The following
sections describe each question in detail.

1. Page title

- Specifies the title of the page.
- The default value is "scenario_management_page".

2. Page folder

- Specifies the path of the folder that contains the generated page.
- The path is relative to the current working directory. The folder will be created if not exist.
- The default value is "pages".

3. Bind the *selected_scenario* variable

- The *selected_scenario* stores the scenario selected by the
user in the page.
- By default, the *selected_scenario* variable is defined in the page. You can import this variable to another
    page to share the scenario selected by the user. For more information, please refer to
[Binding variables](../../userman/gui/binding.md).
- If there is already an existing variable with the same purpose from a different page, please
    specify the module and the variable name separated by a space. It will be imported automatically
    to the scenario management page. For example, if there is a *selected_sc* variable in the root
    page and you want to bind that to the data controls, you can specify ".root selected_sc".

4. Bind the *selected_data_node* variable

- The *selected_data_node* variable stores the data node selected by the
user in the page. You can import this variable to another
    page to share the data node selected by the user.

# Page description

The generated page has the following folder structure:

```plaintext
pages/
├──── scenario_management_page/
│   ├──── __init__.py
│   └──── scenario_management_page.py
│
└──── __init__.py
```

Your page's folder structure may vary depending on the answers you provided during the
creation process. Here is a brief overview of the page structure:

- `pages/`: The folder that contains the page specified in the second question.
    - `scenario_management_page/scenario_management_page.py` contains the layout and the content
    of the page.
    - `\_\_init\_\_.py` is the file that imports the newly created page in the `pages` package.

# Customizing the page

Everything in the generated page can be updated to precisely fit your specific requirements.

The grid layout of the page can be customized via the
[layout](../../refmans/gui/viselements/generic/layout.md) block.

For managing scenarios, you can customize the
[scenario_selector](../../refmans/gui/viselements/corelements/scenario_selector.md)
and [scenario](../../refmans/gui/viselements/corelements/scenario.md) controls which
allow the user to select and manage the scenarios respectively. The DAG of the scenario is shown
by a [scenario_dag](../../refmans/gui/viselements/corelements/scenario_dag.md) control.

You can also modify the *notify_on_submission()* function to handle the notification of a scenario's
submission.

For managing data nodes, you can customize the
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
from pages import root_page, scenario_management_page

pages = {
    "/": root_page,
    "scenario": scenario_management_page,
}

if __name__ == "__main__":
    gui = Gui(pages=pages)
    gui.run()
```

You can also explicitly import the *selected_scenario* and *selected_data_node* variables
from the newly created page to a different page to share the scenario and data node selected by
the user.
