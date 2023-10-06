---
title: Migration
hide:
  - navigation
---

This documentation page lists the migration paths of Taipy releases as they
were published.

# From 2.0 to 2.1

In Taipy version 2.1, the version management system has been introduced. For
applications created with a Taipy Core version &#8804 2.0, the first time it
runs with version 2.1 or later, no version exists, and so legacy entities are not
attached to any version. The overall principle is to create a version the first
time the application runs with Taipy 2.1 or later and to assign all the old entities
to this version. Depending on the mode used to run the application,
(Refer to [versioning documentation](manuals/core/versioning/index.md)
for details) we propose the following migration paths:

## Using default or development mode

Please refer to the [Development mode](manuals/core/versioning/development_mode.md)
documentation page for more details on how to run Taipy in development mode.

The first time you run the application with Taipy 2.1 or later, if you use the
_development_ mode which is the default mode, Taipy automatically creates an
_experiment_ version with the current configuration and assigns all legacy
entities to it. The version is named "LEGACY-VERSION". Depending on how you
want to handle legacy entities, you can now manage your newly created version
using the version management system. Please refer to the
[Version management system](manuals/core/versioning/index.md) documentation page
for more details.

## Using experiment or production mode

Please refer to the [Experiment mode](manuals/core/versioning/experiment_mode.md) or
[Production mode](manuals/core/versioning/experiment_mode.md) documentation pages
for more details on how to run Taipy in experiment or production mode.

The first time you run the application with Taipy 2.1 or later, if you use
_experiment_ or _production_ mode, you can simply provide a version name to create
a new version. All legacy entities are automatically attached to this version.
You can now manage your newly created version using the version management system.
Please refer to the [Version management system](manuals/core/versioning/index.md)
documentation page for more details.
