Depending on the task that the application is addressing, there are several execution
use cases that can be considered for running a Taipy application.

A Taipy application is just a Python script that relies on the Taipy packages
to perform the tasks to be executed.<br/>
Running a Taipy application can be as simple as invoking the Python interpreter,
providing the path to the script you need to run.

The application may however have a few requirements that Taipy can address:

- [Running Taipy services](running_services.md): some Taipy functionality can be
  run as services. That is typically the case for [Taipy GUI](../../gui/index.md),
  [Taipy REST](../../scenario_features/rest/index.md), or
  [Taipy Orchestrator](../../scenario_features/task-orchestration/index.md).
- [Rely on an external web server](external_web_server.md): although
  [Taipy GUI](../../gui/index.md) and [Taipy REST](../../scenario_features/rest/index.md) provide
  an internal web server, you may need to host your application in a web server that is already
  installed in your infrastructure.
- [Protect private files](protect_files.md): because the hosting of an application by a web
  server poses risks of exposing files that you want to keep secret, Taipy provides means
  to set up file access security.

## [Running Taipy services](running_services.md)

## [External web servers](external_web_server.md)

## [Protecting private files](protect_files.md)
