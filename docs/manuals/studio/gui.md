# Support for Taipy GUI Markdown syntax

The Taipy Studio extension leverages the Visual Studio Code text edition functionality
to accelerate the definition of Taipy GUI pages with the
[Markdown syntax](../gui/pages.md#using-markdown):

- [IntelliSense](https://learn.microsoft.com/en-us/visualstudio/ide/using-intellisense)
  can be used in the context of page definition.<br/>
  This auto-completion feature gives you quick access to visual element types, their
  specific properties, and even code variables in certain situations.<br/>
  See the [Auto-completion](#auto-completion) section for details.
- Diagnostics are provided in the Problems panel and the code itself, showing syntactic
  problems in your page definition. Some of these problems can be quickly fixed using
  Quick Fixes.<br/>
  See the [Diagnostics](#diagnostics) section for details.
- [Snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets) are
  short pieces of code that can be inserted into your code with a few keystrokes.<br/>
  The Taipy Studio extension comes with a few code snippets detailed in
  the section on [Snippets](#snippets).
- A command is available to generate a complete visual element definition in the
  Markdown text.<br/>
  See the [Element Generation](#diagnostics) section for details.

The extension is activated when Visual Studio Code finds Markdown text:

- In a Markdown file (the filename extension must be `.md`) which is
  part of the currently opened project;
- In any string that appears in Python source code, part of the currently
  opened project, using the triple quote syntax (which allows a string to
  span multiple lines of text).

## Auto-completion

Auto-completion (or IntelliSense) is triggered when:

- the programmer enters the `<|` key sequence.
- the programmer presses the `Ctrl-<ENTER>` combination in the context of a visual
  element context (that is, after a "<|" fragment).<br/>

Taipy Studio proposes the list of available visual element types as well
as the specific list of properties for the element currently being defined.

Here is an example of how a control can be created in the Visual Studio Code
text editor for a Markdown file:

<p align="center">
  <img src="../images/autocomplete_element.gif" width=75%>
</p>

### Access to variable and function names

The auto-completion feature can also be used in the context of a property value
to provide quick access to variable and function names that would be valid
values for a given property. This works only if the Markdown content is entered as
a string value in a Python file (using the triple quote syntax) or as text in a
Markdown file with the same root name as a Python file sitting in the same
directory, both being part of the currently opened project.<br/>
Then Taipy Studio proposes relevant Python identifiers just after the user presses
the "`{`" key, opening a fragment to write a Python expression.

Here is what this looks like when referencing a variable name:

<p align="center">
  <img src="../images/autocomplete_variable.gif" width=75%>
</p>

And here is a similar example, where a function name is required for a
property that holds a callback. Candidate function names that could be
set to the property is proposed to the user:

<p align="center">
  <img src="../images/autocomplete_function.gif" width=75%>
</p>


## Diagnostics

Taipy Studio can detect issues in the definition of visual elements.
Those issues appear in the text body itself as well as in the Problems panel
(that can be displayed using the Visual Studio `Ctrl+Shift+M` key combination).<br/>
Some detected problems come with Quick Fixes that allow programmers to solve
them semi-automatically.

Here is a list of warnings and errors detected by Taipy Studio:

- Missing closing syntax on control elements (MSC).<br/>
  Quick fix available: add closing syntax.
  <p align="center">
    <img src="../images/diagnostics_mcs.png">
  </p>

- Missing opening tag on block elements (MOT).
  <p align="center">
    <img src="../images/diagnostics_mot.png">
  </p>

- Missing closing tag on block elements (MCT).
  <p align="center">
    <img src="../images/diagnostics_mct.png">
  </p>

- Missing opening tag with matching tag id (MOTI).
  <p align="center">
    <img src="../images/diagnostics_moti.png">
  </p>

- Missing closing tag with matching tag id (MCTI).
  <p align="center">
    <img src="../images/diagnostics_mcti.png">
  </p>

- Opening tag with unmatched tag id (UOTI).
  <p align="center">
    <img src="../images/diagnostics_uoti.png">
  </p>

- Closing tag with unmatched tag id (UCTI).
  <p align="center">
    <img src="../images/diagnostics_ucti.png">
  </p>    

- Invalid property format (PE01).

- Invalid property name (PE02).<br/>
    Property names are dependent on the visual element type. Quick fix is available.
    <p align="center">
      <img src="../images/diagnostics_pe02.png">
    </p>

- Ignore negated value (PE03).<br/>
    Quick fix available: remove negated value.
    <p align="center">
      <img src="../images/diagnostics_pe03.png">
    </p>

- Function not found (FNF).<br/>
    This error is detected only in the context of a Python source file.
    <p align="center">
      <img src="../images/diagnostics_fnf.png">
    </p>
    Quick fix available: generate a function with the correct signature into the
    Python file:
    <p align="center">
      <img src="../images/diagnostics_fnf_quickfix.gif">
    </p>

## Element Generation

Taipy Studio provides a command to generate the skeleton of a visual element
definition quickly.<br/>

- Open the
  [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
  (`Ctrl+Shift+P` on Windows or Unix, `Cmd+Shift+P` on MacOS);
- Search for the command `Generate Taipy GUI element` and execute
  it.

The command runs a step-by-step process that lets users indicate what
element needs to be generated and with what set of properties.<br/>
The definition for the new element will be inserted in the last active window.

<p align="center">
  <img src="../images/generation_viselement.gif">
</p>

Of course, you may want to bind this command to some key binding of your liking.

## Snippets

Code snippets are proposed when the programmer presses the `Ctrl-<ENTER>` key
combination outside a visual element context.<br/>
In a Markdown context, Taipy Studio proposes two snippets that let users insert
the skeleton for a control ("<|c" snippet) or a block ("<|b" snippet) where the
closing "|>" fragment is inserted as an additional line.

Here is how you can rapidly create a new control on your page:

<p align="center">
  <img src="../images/snippet_control.gif" width=75%>
</p>
