Taipy applications are regular Python applications that can be run on any
machine that has a supported Python version installed.

Whether your application runs as a one-shot, or as a service, the standard
way to run it consists of running the main Python module using the Taipy
command-line interface (CLI) that is installed with the Taipy package.

Assuming the main module is named `main.py`, you can run it with the following:

````console
$ taipy run main.py
````

This command starts the application. If the main Python module calls the Taipy
`run()` function (or any other third party service), the application runs as a
service, and keeps running until it is stopped manually with a keyboard interrupt
(Ctrl+C). Otherwise, the application runs as a one-shot and then stop.
In both cases, the application is executed in the current terminal session.

# Run with options or arguments

For more details on how to use the command line and the available options,
please refer to the [taipy run](../../ecosystem/cli/run.md) documentation page.

# Prepare the main script

For more details on how to prepare your main Python module, please refer to
the documentation page about [the run() function](main-script.md).

# Protect your application
When a Taipy `Gui^` service runs, a web server is created, allowing malicious users
to potentially access some files if they know their paths. To protect your files,
please refer to the [Protect private files](protect-files.md) documentation page.

# Run with an external web server
If you already have a web server running and want to add Taipy capabilities to it,
please refer to the [External web server](external-web-server.md) documentation page.

# Run Taipy GUI in a Notebook
For more details on how to run Taipy GUI in a Notebook, please refer to the
[Notebooks](notebooks.md) documentation page.

!!! warning "Running in a Jupyter Notebook"

    Only the Taipy GUI service can run in a Notebook. The Orchestrator and REST
    services cannot run in a Notebook.
