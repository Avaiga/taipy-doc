Since the version management system has been added to Taipy in version 2.1, before running
an application created on Taipy version &#8804 2.0 with taipy 2.1 or later, we propose the
following migration path.

Indeed, before running the application with Taipy 2.1 or later, no version is created and
old entities are not attached to any version. The overall principle is to create a version
the first time the application runs with Taipy 2.1 or later and to assign all the old
entities to this version.

# Install Taipy 2.1

First you need to update Taipy to version 2.1 or greater.

``` console
$ pip install taipy==2.1
```

or

``` console
$ pip install --upgrade taipy
```

# Development mode

The first time you run the application with Taipy 2.1 or later, if you use the
_development_ mode, Taipy automatically creates an _experiment_ version with
the current configuration and assign all legacy entities to it. The version is
named "LEGACY-VERSION".

You can then manage your version using the version management system. Please
refer to the [Version management system](../versioning/index.md) documentation
page for more details.

# Experiment or production mode

The first time you run the application with Taipy 2.1 or later, if you use
_experiment_ or _production_ mode, you can simply provide a version name and
create a version. All legacy entities are automatically attached to this version.

```console
$ python main.py --experiment legacy
```

or

```console
$ python main.py --production legacy
```

You can then manage your version using the version management system. Please
refer to the [Version management system](../versioning/index.md) documentation
page for more details.
