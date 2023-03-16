# Taipy Core

The Taipy Core package is a Python library designed to build powerful and customized data-driven back-end applications.
It provides the necessary tools to help Python developers transform their algorithms into a complete
back-end application. It brings algorithm management to another level: algorithms are now connected to the end-user
through user-defined scenarios, powerful scenario management and comparison, interactive data, smart scheduling, etc.

Taipy Core provides the key concept of _Scenario_. Among other functionalities, a _Scenario_ represents an instance
of a data science problem with its datasets (modeled as _Data nodes_ in Taipy Core) and the algorithms to run to solve
the problem. The algorithms are modeled as an execution graph (a Directed Acyclic Graph or DAG) that can be seen as a
succession of functions (or _Tasks_ in Taipy Core) that exchange data. With Taipy Core, one can model simple as
well as very complex algorithms.

[:material-arrow-right: Basic example](basic_examples/index.md),

[:material-arrow-right: Definition of Taipy Core concepts](concepts/index.md),

[:material-arrow-right: Documentation on the Python configuration](config/index.md),

[:material-arrow-right: Description of Taipy Core entities](entities/index.md)

[:material-arrow-right: Documentation on user application version management](versioning/index.md)
