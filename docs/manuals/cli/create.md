# Create a Taipy application

Taipy provides a comfortable environment for getting started with Taipy via the create command,
and is the best way to start building a new application with Taipy.

## From the default template

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
In this example, we scaffold a new application using the default Taipy template, which is a simple
Taipy GUI single-page application. Here, we define the application name as "new_application", the
main Python file of the application as "app.py", and the title of the web page as "App Title". Then
we change the directory (`cd`) to our newly created folder and start the application by running
`python app.py`.

!!! Info

    If there is no answer provided, the default value in the square brackets will be applied.

## From a specific template

You can also specify another template using the `--template` option.

```console
$ taipy create --template multi-page-gui
application_name [taipy_application]: new_application
application_main_file [main.py]: app.py
application_title [Default title]: App Title
$ cd ./new_application
$ python app.py
```

In this example, we scaffold a new application using the "multi-page-gui" template, which is a
multi-page Taipy GUI application.

Please refer to the next section for a list of templates.

## List of templates

You can see the list of supported templates by running `taipy help create` command. Alternatively, you can
use the `--help` or `-h` options. Run `taipy create --help` or `taipy create -h`.

```console
$ taipy help create
usage: taipy create [-h] [--template {default,multi-page-gui,...}]

options:
  -h, --help            show this help message and exit
  --template {default,multi-page-gui,...}
                        The Taipy template to create new application.
```
