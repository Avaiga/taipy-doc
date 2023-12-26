# Accessing the library assets

Say we want to display a small image next to the text. That would be useful in the
situation where we apply our *caption* control to represent a company name along with
its logo.

In HTML, you would create an `img` tag, where the source URL is set to the path of the
image. However, in order to protect the application from attacks, Taipy provides the
method `ElementLibrary.get_resource()` that let the application filter what resources
are requested, and return the actual files according to the application setting.



!!! warning "Work in Progress"
    This section still requires significant work, which is in progress.
    At this time, Taipy GUI provides a custom element library example
    with lengthy explanations on how to build it.<br/>
    Please look into the `doc/extension` directory where Taipy GUI is
    installed for more information.<br/>
    You can also look at this example directly on
    [GitHub](https://github.com/Avaiga/taipy/tree/[BRANCH]/doc/gui/extension).
