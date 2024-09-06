---
hide:
    - toc
---
The **Config Files** section holds the list of configuration files (`*.toml`) in your
project. You will select the one you want to edit from that list.<br/>
This list shows the base names of all the configuration files. If two configuration files
have the same name (but are located in two different directories), the path to the directory
where these files belong will be displayed next to the base file name to avoid
confusion.

Because the **Config Files** list is synchronized with the files included in your project,
adding a configuration file is simply a matter of creating it from the Visual Studio
Code Explorer panel:

<p align="center">
  <img src="../../images/config_init.gif" width="80%"/>
</p>

This animation demonstrates how to open the **Taipy Configs** pane, if necessary.

Similarly, if you remove or rename a configuration file from the **Explorer** panel of Visual
Studio Code, the change is immediately reflected in the Config Files section of the
Taipy Configs panel.

Note that if you right-click a configuration file, Taipy Studio displays a menu that
lets you choose one of two options:

- "Reveal file in explorer view": Visual Studio Code will select and focus on the file
    item in the project's files in the **Explorer** pane.
- "Show view": creates a view from the configuration file that represents all the
    configuration elements as a [global graph](graphview.md), so you can see
    all the configuration elements and how they relate to each other.
