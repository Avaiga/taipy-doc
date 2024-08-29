# Create a Taipy application

Taipy provides a comfortable environment for getting started with Taipy via the create command,
and is the best way to start building a new application with Taipy.

## From the default application template

To create a simple Taipy application, you can run `taipy create`, then answer a few questions to
customize your application.
```console
$ taipy create
Application root folder name [taipy_application]: new_application
Application main Python file [main.py]: app.py
Application title [Default title]: App Title
Page names in multi-page application? []: slide_1 slide_2 slide_3
Does the application use scenario management or version management? [No]: y
Does the application use Rest API? [No]:
$ cd ./new_application
$ taipy run app.py
```
In this example, we scaffold a new Taipy application using the default Taipy application template, which
lets us create a simple, minimal Taipy application.


!!! info

    In the prompt, we can see the question and the default value in the square brackets.
    We can provide an answer or press enter to use the default value.


- The first question defines the application root folder as "new_application"
- In the second and third questions, we set the main Python file of the application as "app.py"
    and the web page's title as "App Title".
- In the 4th question, we clarify that we want a Taipy multi-page GUI application with three
    pages, and the page names are "slide_1", "slide_2", and "slide_3". If there is no answer to
    this question, the application will be a single page application. Please note that the names
    must be valid Python identifiers.
- In the 5th question, we clarify that we want to use scenario management, so the application
    should include the Orchestrator service.
- In the 6th question, we chose the default answer is No, meaning we don't want to use Rest API,
    so the application should not include the Taipy Rest API service.

Finally, we changed the directory (`cd`) to our newly created folder and started the application
by running `taipy run app.py`.

## From a specific application template

You can specify creating a new application from another application template using the
*--application* option.

```console
$ taipy create --application scenario-management
Application root folder name [taipy_application]: new_application
Application main Python file [main.py]: app.py
Application title [Default title]: App Title
Does the application use TOML Config? [No]:
$ cd ./new_application
$ taipy run app.py
```

In this example, we scaffold a new Taipy application using the "scenario-management" template,
which utilizes [a scenario selector](./../../../refmans/gui/viselements/corelements/scenario_selector.md) to allow
creating, managing, and running scenarios directly from the GUI page.

Please refer to the next section for a list of application templates.

## List of application templates

You can see the list of supported application templates by running `taipy help create` command.
Alternatively, you can use the *--help* or *-h* options by running `taipy create --help` or
`taipy create -h`.

```console
$ taipy help create
usage: taipy create [-h] [--application {default,scenario-management,...}]

options:
  -h, --help            show this help message and exit
  --application {default,scenario-management,...}
                        The application template name to create a new Taipy application.
```
