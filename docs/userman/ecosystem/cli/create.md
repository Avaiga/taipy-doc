# Create a Taipy application from a template

Taipy provides a comfortable environment for getting started with Taipy via the create command,
and is the best way to start building a new application with Taipy.

To create a simple Taipy application, you can run `taipy create` from the CLI, then answer a few
questions to customize your application.
```console
$ taipy create
```
By default, the `taipy create` command helps a new Taipy application using the default Taipy application template.

You can specify creating a new application from another application template using the
*--application* option.

```console
$ taipy create --application sdm
```

Taipy currently supports the following application templates:

- [Default application template](../templates/applications/default_app.md)
- [Scenario management application template](../templates/applications/sdm_app.md)


# List of application templates

From the CLI, you can list all supported application templates by running `taipy help create`
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
