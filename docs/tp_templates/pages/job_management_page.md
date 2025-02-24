!!! note "Available in Taipy Enterprise edition"

    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise).

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

During the development process of a Taipy application, adding a job management page is a common
practice to allow users to manage submitted jobs in the application.

To reduce the development time, Taipy provides a job monitoring page template, which is designed
as a best practice page for monitoring and managing jobs in a Taipy application by leveraging
Taipy visual elements.

<figure>
  <img src="../img/job_template_dark.jpeg" class="visible-dark" />
  <img src="../img/job_template_light.jpeg" class="visible-light"/>
  <figcaption>Out-of-the-box Taipy job monitoring page</figcaption>
</figure>

Out-of-the-box, the job monitoring page allows the user to perform various operations on jobs,
including:
- filtering jobs
- monitoring job status
- select a job
- view the detail of the selected job
- delete the selected job

# How to create a page

To create the page from the scenario page template, change to the folder of the application in
which you want to create the page and run `taipy create --page job_monitoring` from the CLI. Then
answer a few questions to customize your page.

```console
$ taipy create --page job_monitoring
  [1/3] Page name (job_monitoring_page):
  [2/3] Page folder (pages):
  [3/3] If the following variable needs to be bound to an existing variable,
please specify the module and the variable name separated by a space
(for example, ".root selected_job"):
selected_job ():

The new Taipy page has been created at pages/job_monitoring_page

The "selected_job" variable has been created for the page.
Please import the new page in your main application to use it.
```

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the page. The following
sections describe each question in detail.

1. Page name

- Specifies the name of the page.
- The default value is "scenario_management_page".

2. Page folder

- Specifies the path of the folder that contains the generated page.
- The path is relative to the current working directory. The folder will be created if not exist.
- The default value is "pages".

3. Bind the *selected_job* variable

- The *selected_job* variable stores the job selected by the user in the page. For more information,
please refer to [Binding variables](../../userman/gui/binding.md).
- By default, the variable is defined in the page. You can import this variable to another page to
    share the job selected by the user.
- If there is already an existing variable with the same purpose from a different page, please
    specify the module and the variable name separated by a space. It will be imported automatically
    by the job monitoring page. For example, if there is a *selected_job* variable in the root
    page and you want to bind that to the *job_selector* control, you can specify ".root selected_job".

# Page description

The generated page has the following folder structure:

```plaintext
pages/
├──── job_monitoring_page/
│   ├──── __init__.py
│   └──── job_monitoring_page.py
│
└──── __init__.py
```

Your page's folder structure may vary depending on the answers you provided during the
creation process. Here is a brief overview of the key components:

- `pages/`: The folder that contains the page specified in the second question.
    - `job_monitoring_page/job_monitoring_page.py` contains the content of the page.
    - `\_\_init\_\_.py` is the file that exports the newly created page from the `pages` package.

# Customizing the page

Everything in the generated page can be updated to precisely fit your specific requirements.

For monitoring jobs, you can customize the
[job_selector](../../refmans/gui/viselements/corelements/job_selector.md) control which
allows the user to monitor, select, and manage the Taipy jobs of the application.

You can also add more content to the page such as descriptions, or other
[visual elements](../../refmans/gui/viselements/index.md) provided by Taipy to enrich the
user experience.

# How to use the page

To use the page in your application, import the page in the main application file along with other
pages and add it to the page list given to the `Gui^` service.

```python title="main.py"
from taipy import Gui
from pages import root_page, job_monitoring_page

pages = {
    "/": root_page,
    "job_monitoring": job_monitoring_page,
}

if __name__ == "__main__":
    gui = Gui(pages=pages)
    gui.run()
```

You can also explicitly import the `selected_job` variable from the newly created page to
a different page to share the job selected by the user.
