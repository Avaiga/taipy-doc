# Create a Taipy application from a template

Taipy provides a comfortable environment for getting started with Taipy via the create command,
and is the best way to start building a new application with Taipy.

To create a simple Taipy application, you can run `taipy create` from the CLI, then answer a few
questions to customize your application.
```console
$ taipy create
```
By default, the `taipy create` command helps scaffolding a new Taipy application using the
default Taipy application template.

You can specify creating a new application from another application template using the
*--application* option.

```console
$ taipy create --application sdm
```

Taipy currently supports the following application templates:

- [Default application template](../../../tp_templates/applications/default_app.md)
- [Scenario management application template](../../../tp_templates/applications/sdm_app.md)

# Create a Taipy page from a template

Taipy also provides page templates, which can be used to create new pages on top of the existing
application. Once generated, the pages can be easily customized and plugged into the application.

!!! note "Available in Taipy Enterprise edition"

    The page templates are only available in the [Taipy Enterprise Edition](https://taipy.io/enterprise).

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

To create a new Taipy page from a page template, you can run `taipy create --page {page-template}`
from the CLI, then answer a few questions to customize your page.
```console
$ taipy create --page default
```

Taipy currently supports the following page templates:

- [Default page template](../../../tp_templates/pages/default_page.md)
- [Root page template](../../../tp_templates/pages/root_page.md),
- [Data management page template](../../../tp_templates/pages/data_management_page.md),
- [Scenario management page template](../../../tp_templates/pages/sdm_page.md),
- [Job management page template](../../../tp_templates/pages/job_management_page.md),
- [Login page template](../../../tp_templates/pages/login_page.md),


# Application templates list

From the CLI, you can list the available application templates by running `taipy help create`
command. Alternatively, you can use the *--help* or *-h* options by running `taipy create --help`
or `taipy create -h`.

```console
$ taipy help create
usage: taipy create [-h] [--application {default,sdm,...}]

options:
  -h, --help            show this help message and exit
  --application {default,sdm,...}
                        The application template name to create a new Taipy application.
```
