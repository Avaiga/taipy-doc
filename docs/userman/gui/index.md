The Taipy GUI library provides Python classes that make it easy to create
powerful web applications in minutes.

# What is a graphical user interface?

A graphical user interface (or GUI) displays and organizes graphic elements on
the user's device.
These elements represent application data and allow users to
interact with the application code.

There are mechanisms in place to install communication between the server, running
at the heart of the application, and the graphical interface presented to
end-users.

# Main concepts

In Taipy, GUIs are made of generated web pages served by a web server
hosted by the Taipy application itself (or on which the Taipy application
relies). Taipy provides the class `Gui^` that handles this server and its
settings.

The `Gui^` class holds any number of *pages*, where text and graphical elements can
be placed. These elements can reflect the state of your application variables
so the end-user can be presented with relevant information.<br/>
Users can also interact with some of those elements to trigger application code
that can change the displayed information, produce more data to visualize or move to a
completely different page.

The generated web pages are built from a set of template text files that you provide, where you
would have planted placeholders that will display application data. The application end users can
then see and interact with the application. We call these representative and interactive objects:
*visual elements*.

To describe the content of pages, Taipy comes with support for three different mechanisms: there are
two template formats, handled by the classes `Markdown^` and `Html^`, and a pure Python way of
creating pages using the `(taipy.)gui.builder.Page^` class. This is described in the
[Pages](pages/index.md) section.

The basic principle is that you create pages as needed, give them a name to indicate to your browser
how to access these pages, and provide these pages to the `Gui^` instance used in your
application.

When you invoke the `(Gui.)run()^` method of the `Gui^`, a web server is
started and allows web clients to connect to it then request pages. This is
when Taipy transforms the page you had created into some HTML
content sent back to the client so the user can see the application interface
and start using it.

!!! info "More information"
    You can find more information on how pages are created and used in Taipy application in
    the [Pages](pages/index.md) section.

!!! info "Multiple services"
    To run the Taipy GUI service with some other Taipy services, please refer to the
    [Running Taipy services](../run-deploy/run/running_services.md) page.
