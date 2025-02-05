This documentation page aims to help users, developers, architects, and DevOps
teams understand how to operate a typical Taipy application, covering its
architecture, required infrastructure, components, and communication between
components.

# What is a Taipy application?

A Taipy application is a user-defined Python module invoking some Taipy services.
In background, when running, the application starts a Flask web server and a few
processes.

# What is a standard architecture?

An application architecture is a logical description of the application processes
and services, how they interact with each other, and how they interact with the
external world.

For a Taipy application, multiple architectures are possible depending on the various
Taipy functionalities used, on how the application is configured, and on the other
functionalities from the user defined code or from third party libraries.

Several examples of standard architectures are available in the
[Architecture examples](architectures.md) page.

# How to run a Taipy application?

Running a Taipy application means running the user-defined main Python module.
Taipy provides the `taipy run` CLI command, which accepts the main Python file as
a parameter. For more details on how to run Taipy applications, please refer to the
[Running](running/index.md) page.

# How to deploy a Taipy application?

Deploying a Taipy application means running the user-defined main Python module
in a production environment so that it can be accessed by end users. Taipy provides
a comprehensive guide on how to deploy a Taipy application in various environments.
Please refer to the [Deploying](deploying/index.md) page.

# How to version a Taipy application?

Taipy provides a comprehensive versioning system that allows users to create and
manage various versions of their application. This versioning systems tracks the
Taipy configuration modifications and ensures backward compatibility on Taipy's
entities (scenarios, data nodes, etc. ) when deploying a new version in production.
Please refer to the [Versioning](versioning/index.md) page for more details.

# How to upgrade Taipy to a new version?
