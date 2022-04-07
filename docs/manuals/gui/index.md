# Taipy's User Interface

The Taipy GUI library provides Python classes that make it easy to create
powerful Web apps in minutes.

## What is a graphical user interface

A graphical user interface (or GUI) displays and organizes graphic elements on
the user's device.
These elements represent application data and allow users to
interact with the application code.

There are mechanisms in place to install communication between the server, running
at the heart of the application, and the graphical interface presented to
end-users.

## Main concepts

In Taipy, GUIs are made of generated Web pages served by a Web server
hosted by the Taipy application itself (or on which the Taipy application
relies). Taipy provides the class `Gui^` that handles this server and its
settings.

The `Gui^` class holds any number of _pages_, where text and graphical elements can
be placed. These elements can reflect the state of your application variables
so the end-user can be presented with relevant information.<br/>
Users can also interact with some of those elements to trigger application code
that can change the displayed information, produce more data to visualize or move to a
completely different page.

The generated Web pages are built from a set of template text files that you
provide, where you would have planted placeholders that will display application
data. The application end users can then see and interact with the application. We call these representative and interactive objects: _visual elements_.

To describe the content of pages, Taipy comes the support for two template formats, handled by the classes `Markdown^` and `Html^`.

The basic principle is that you create pages as you need them, give them a name
so you can indicate to your browser how to access these pages, and provide these pages to
the `Gui^` instance used in your application.

When you invoke the `(Gui.)run()^` method of the `Gui^`, a Web server is
started and allows Web clients to connect to it then request pages. This is
when Taipy transforms the page you had created into some HTML
content sent back to the client so the user can see the application interface
and start using it.

!!! info "You can find more information on how pages are created and used in Taipy application in the [Pages](pages.md) section."
