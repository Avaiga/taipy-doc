# Support for Taipy GUI Markdown syntax

The Taipy Studio extension provides a specific kind of support for
[IntelliSense](https://learn.microsoft.com/en-us/visualstudio/ide/using-intellisense)
in the context of writing
[Markdown text for Taipy GUI](../gui/pages.md#using-markdown).<br/>
Taipy Studio will help you complete constructs needed to define visual elements
and even propose code elements (such as variable or function names) that the
element might use. In this regard, Taipy Studio provides a kind of code
completion service, for the Taipy GUI Markdown syntax.

Beside the auto-completion service, Taipy Studio also reports, in the *Problems*
view, warnings and errors it finds in the Markdown content it watches.

This feature is activated when you enter Markdown content:

- In a Markdown file (the filename extension must be `.md`) which is
  part of the current opened project;
- In any string that appears in Python source code, part of the current opened
  project.

## Auto-completion in Markdown 



<p align="center">
  <img src="../images/viselement_autocomplete.gif" width=75%>
</p>





[TODO]

