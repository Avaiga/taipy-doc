By installing Taipy, you will have access to the `taipy` command. You can check your current
version of Taipy by running the `taipy --version` command in a terminal (Linux, macOS) or command
prompt (Windows).

```console
$ taipy --version
Taipy 2.3.0
```

If you don't see a supported version of Taipy, you'll need to either upgrade Taipy or perform a
fresh install, as described in the [Installation page](../installation.md).

A list of available commands provided by Taipy is shown by running the `taipy`, or `taipy help`,
or `taipy --help` command.

```console
$ taipy
usage: taipy [-v] {manage-versions,create,help} ...

positional arguments:
  {manage-versions,create,help}
    manage-versions     Taipy version control system.
    create              Create a new Taipy application.
    help                Show the Taipy help message.

options:
  -v, --version         Print the current Taipy version and exit.
```

## Create a Taipy application from a template

Taipy provides a comfortable environment for getting started with Taipy via the create command,
and is the best way to start building a new application with Taipy.

To create a simple Taipy application, you can run `taipy create`, then answer a few questions to
customize your application.
```console
$ taipy create
application_name [taipy_application]: new_application
application_main_file [main.py]: app.py
application_title [Default title]: App Title
$ cd ./new_application
$ python app.py
```
In this example, we create a new application using the default Taipy template, which is a simple
Taipy GUI single-page application. Here, we define the application name as "new_application", the
main Python file of the application as "app.py", and the title of the web page as "App Title". Then
we change directory (`cd`) to our newly created folder and start the application by running
`python app.py`.

!!! Info

    If there is no answer provided, the default value in the square brackets will be applied.

Taipy also provides several templates for you to choose from with the `--template` option. You can
see the list of supported templates by running `taipy help create` command. Alternatively, you can
run `taipy create` with the `--help` or `-h` option.
```console
$ taipy help create
usage: taipy create [-h] [--template {default, ...}]

options:
  -h, --help            show this help message and exit
  --template {default, ...}  The Taipy template to create new application.
```

## Manage versions

The `taipy manage-versions` command allows a Taipy user to track and manage various versions of
a Taipy Core application. Please refer to the [Manage versions](./core/versioning/version-mgt.md)
documentation page for more information.
