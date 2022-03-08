# About

Taipy can generate a graphical user interface for you, if you need one.

## What is a graphical user interface

A graphical user interface (or GUI) displays graphical elements on the user's device.
These elements provide a representation of the application data, and allow users to
interact with the application code.

In Taipy, GUIs are made of generated Web pages that are served by a Web server
hosted by the Taipy application itself (or on which the Taipy application relies). This
server and its settings are handled by the [`Gui object`](user_gui.md).

## How is the Graphical User Interface generated

The generated Web pages are built from a set of template text files that you provide,
where you would have planted placeholders that will display application data, in different
ways, and let final users of the application interact with it. We call these representative
and interactive objects: _controls_.

In order to describe the content of pages, Taipy comes the support for two template formats,
handled by the classes `Markdown^` and `Html^`.

The basic principle is that you create pages as you need them, give them a name
so you can indicate to your browser how to access these pages and provide these pages to a `Gui` instance used in your
application.

When the `(Gui.)run()^` method of the `Gui^` instance is invoked, a Web client can connect to the underlying Web
server and request for a given page. At this time, Taipy transforms the page that you had created into some HTML
content that is sent to the client so the user can see the application interface.

!!! info "You can find more information on how pages are created and used in Taipy application in the [Pages](user_pages.md) section."
