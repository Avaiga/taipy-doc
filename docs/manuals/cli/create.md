# Create a Taipy application

Taipy provides a comfortable environment for getting started with Taipy via the create command,
and is the best way to start building a new application with Taipy.

## From the default template

To create a simple Taipy application, you can run `taipy create`, then answer a few questions to
customize your application.
```console
$ taipy create
Application root folder name [taipy_application]: new_application
Application main Python file [main.py]: app.py
Application title [Default title]: App Title
How many pages and the name of the pages? [1]: 3 slide_1 slide_2 slide_3
Does the application use scenario management or version management? [No]: y
Does the application use Rest API? [No]:
$ cd ./new_application
$ python app.py
```
In this example, we scaffold a new application using the default Taipy template, which let us create a simple
minimalized Taipy application.


!!! Info

  In the prompt, we can see the question along with the default value in the square brackets.
  We can either provide an answer or just press enter to use the default value.


- In the first question, we define the application root folder as "new_application"
- In the second and third questions, we set the main Python file of the application as "app.py" and the title of the web page as "App Title".
- In the 4th question, we clarify that we want a Taipy multi-page GUI application, with the page names "slide_1", "slide_2", and "slide_3". Please note that if the names are not clarified, the default name will be "page_1", "page_2", and so on.
- In the 5th question, we clarify that we want to use scenario management, so the application should include the Taipy Core service.
- In the 6th question, we choose the default answer is No, which means that we don't want to use Rest API, so the application should not include the Taipy Rest API service.

Finally, we change the directory (`cd`) to our newly created folder and start the application by running `python app.py`.

## From a specific template

You can also specify another template using the `--template` option.

```console
$ taipy create --template multi-page-gui
Application root folder name [taipy_application]: new_application
Application main Python file [main.py]: app.py
Application title [Default title]: App Title
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
