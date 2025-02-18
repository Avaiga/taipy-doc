!!! note "Available in Taipy Enterprise edition"

    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise).

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

During the development process of a Taipy application, adding a job management page is a common
practice to allow users to manage submitted jobs in the application.

To reduce the development time, Taipy provides a job monitoring page template, which is designed
as a best practice page for monitoring and managing jobs in a Taipy application by leveraging
Taipy visual elements.

Out-of-the-box, the job monitoring page allows the user to perform various operations on jobs,
such as filtering jobs, monitoring job status, select a job, view the job details, and delete the
job.

<figure>
  <img src="../img/job_template_dark.jpeg" class="visible-dark" />
  <img src="../img/job_template_light.jpeg" class="visible-light"/>
  <figcaption>Taipy job monitoring page created by the job monitoring page template
  out-of-the-box.</figcaption>
</figure>

This page template offers several key benefits:

- **Accelerated Development**: By leveraging job selector visual element, developers can quickly
    bootstrap a standard page, saving significant development time to focus on delivering business
    value more efficiently.
- **Ease of Use**: The page template is designed to be user-friendly, with a simple CLI
    interface that guides developers through the page creation process on top of existing
    application. The pages then can be easily customized and plugged into the application.
- **Comprehensive Features**: The template provides a best-practice page scaffold for a
    job monitoring page, which supports a wide range of functionalities, providing a
    comprehensive solution for various use cases.
- **Customization**: The template provides high flexibility and customization options on page
    creation, allowing developers to tailor the page to meet specific requirements and use cases.

# How to create a page

To create the page from the scenario page template, change to the folder of the application in
which you want to create the page and run `taipy create --page job_monitoring` from the CLI. Then
answer a few questions to customize your page.

```console
$ taipy create --page job_monitoring
  [1/3] Page title (job_monitoring_page):
  [2/3] The folder that contains the pages (pages):
  [3/3] There are binding variables in the page.
If the variables need to be imported from a different page,
please specify the module and the variable name separated by a space
(e.g. ..main selected_job):
selected_job ():

New Taipy page has been created at ./pages/job_monitoring_page

The "selected_job" binding variables have been created for the page.
You can replace the binding variables with your own variables in the page content.
Please import the new page in your main application to use it.

For more information, please refer to the Multi-page application tutorial at https://docs.taipy.io/en/latest/tutorials/visuals/3_multipage_application/
```

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the page. The following
sections describe each question in detail.

## 1. Page title

- Specifies the title of the page.
- The default value is "scenario_management_page".

## 2. The folder that contains the pages

- Specifies the path of the folder that contains the generated page.
- The path is relative to the current working directory. The folder will be created if not exist.
- The default value is "pages".

## 3. Binding variable for "selected_job"

- Specifies the binding variable for the "selected_job" in the page content.
- The binding variable for the "selected_job" is used to store the job selected by the
user in the page. For more information, please refer to
[Binding variables](../../userman/gui/binding.md).
- By default, the binding variable is created in the page. You can import this variable to another
    page to share the job selected by the user.
- If there is already a binding variable with the same purpose from a different page, please
    specify the module and the variable name separated by a space. It will be imported automatically
    to the job monitoring page.

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

- *pages/*: The folder that contains the page specified in the second question.
    - *job_monitoring_page/job_monitoring_page.py* contains the content of the page.
    - *\_\_init\_\_.py* is the file that imports the newly created page in the `pages` package.

# Customizing the page

Everything in the generated page can be updated to precisely fit your specific requirements.

For monitoring jobs, you can customize the
[job_selector](../../refmans/gui/viselements/corelements/job_selector.md) visual element which
allow the user to monitor, select, and manage Taipy jobs of the application.

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

You can also explicitly import the `selected_job` binding variable from the newly created page to
a different page to share the job selected by the user.
