---
title: Migration from Taipy 3.X to 4.Y
---

Taipy’s package structure in version 4 as changed. The `taipy-config` package
does not exist anymore. Depending on your dependency management system, the previous
version of the `taipy-config` package may not be automatically removed when upgrading
Taipy from version 3.X to 4.Y. This could lead to runtime issues as the system may
attempt to reference outdated dependencies.

To ensure a clean installation, please manually uninstall Taipy 3.X manually and then install a
fresh Taipy 4.Y.
