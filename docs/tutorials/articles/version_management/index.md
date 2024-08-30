---
title: Application versions with Git
category: scenario_management
data-keywords: scenario configuration versioning
short-description: Leverage version management and Git branches to deal with multiple application versions.
order: 19
img: images/icon-code.svg
---
When developing and deploying a Taipy application, it is straightforward to manage Taipy entities
(scenarios, tasks, data nodes, etc.) and keep them up-to-date when the configuration changes.

In the following, we will use a basic Taipy application example defined in `main.py`.

```python linenums="1" title="main.py"
{%
include-markdown "../../../userman/advanced_features/versioning/code-example/main.py"
comments=false
%}
```

Basic knowledge of Git is required to follow this tutorial.

# Set up the Taipy application as a Git repository

Your application directory must be initialized for Git. From the application directory run:

```console
$ git init
...
Initialized empty Git repository in ~/your_taipy_application/.git/
```

We then need to create a `.gitignore` file to ignore the `.data` directory that contains Taipy
entities: we don't want entities to be managed by Git. You can create the `.gitignore` file manually
or by running the following command:

```console
$ echo ".data" > .gitignore
```
Then we can commit the `.gitignore` file to Git:

```console
$ git add .gitignore
$ git commit -m "Initialize .gitignore to ignore Taipy entities"
```

Now you're ready to manage your Taipy application with Git and Taipy version management.

# Create a Taipy application version

By default, a Taipy application runs in development mode, which means entities from previous
development run are deleted before running the application. To save the entities of a run, you
can create a new experiment version of your application by running your Taipy application with the
`--experiment` option to the `taipy` command. After running the application to make sure that it
works, let's name the experiment version `1.0` and commit the version to Git.

```console
$ taipy run main.py --experiment 1.0
$ git add main.py
$ git commit -m "Create experiment version 1.0"
```

# Switching between versions

A commonly used Git workflow is to use `git checkout` to switch to a different branch and work on
a new application version. Let's create a new Git branch called `1.1` and switch to it:

```console
$ git checkout -b 1.1
Switched to a new branch '1.1'
```

After modifying the application code (to experiment with a new algorithm for example), we can run
the application in experiment mode and name the experiment version `1.1` in the new branch. This
run will create and use entities of version `1.1` only.

```console
$ taipy run main.py --experiment 1.1
```

We then can commit the new version to Git.

```console
$ git add .
$ git commit -m "create experiment version 1.1"
```

Similarly, we can create a new branch `1.2` and create a new application version in it:

```console
$ git checkout -b 1.2
Switched to a new branch '1.2'
...
# modify the application code and run the application
...
$ git add .
$ git commit -m "create experiment version 1.2"
```

The entities of all three versions 1.0, 1.1, and 1.2 are still stored in the `.data` directory.
We can switch back to the version 1.1 of the application and run it again:

```console
$ git checkout 1.1
$ taipy run main.py --experiment 1.1
```

!!! warning

    You need to run provide the correct version number when running the application in experiment mode.
    Otherwise, the configuration maybe incompatible with the entities of the version you want to run
    and an error will be raised.
