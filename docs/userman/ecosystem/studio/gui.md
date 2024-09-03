# Support for Taipy GUI Markdown syntax

The Taipy Studio extension leverages the Visual Studio Code text edition functionality
to accelerate the definition of Taipy GUI pages with the
[Markdown syntax](../../gui/pages/markdown.md):

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
  <img src="../images/autocomplete_element.gif" width="75%"/>
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
  <img src="../images/autocomplete_variable.gif" width="75%"/>
</p>

And here is a similar example, where a function name is required for a
property that holds a callback. Candidate function names that could be
set to the property is proposed to the user:

<p align="center">
  <img src="../images/autocomplete_function.gif" width="75%"/>
</p>

## Page preview

If you are used to working with Markdown in Visual Studio Code, you certainly came across the
[Markdown preview](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview)
feature: pressing `Ctrl+Shift+V` (or `Cmd+Shift+V` on a Mac keyboard) in an editor that contains
Markdown content creates a window showing the representation of a Markdown file. If the text editor
and preview window are displayed next to each other, you are able to instantly see the changes done
in the active Markdown file.

This feature is leveraged by Taipy Studio so that Taipy visual elements are recognized and rendered
in the Markdown preview window. When a valid Taipy GUI visual element is inserted in the Markdown
file, it appears in the Preview section, and the properties that were set are reflected in a way
that is very similar to what you will achieve in the application itself.

Here is an animation showing how this works.

<p align="center">
  <img src="../images/preview_start.gif" width="100%"/>
</p>

A new Markdown file is created, then some basic Markdown content is added. The preview area
displays the result of interpreting the Markdown text.<br/>
If you add a Taipy visual element to the Markdown file, Taipy Studio assumes that this file
can be used as a page definition, and renders the Taipy element in the preview area.<br/>
Note that elements appear to be active (in the example above, the button can be pressed) but
that is only a visual effect. No action is really triggered.

### Non literal properties

Some Taipy GUI visual elements have properties that accept properties that do not have a literal
type, or can be interpreted.

<h5>List of values</h5>

Elements such as [`selector`](../../../refmans/gui/viselements/generic/selector.md) or
[`toggle`](../../../refmans/gui/viselements/generic/toggle.md) have a property called `lov`
that can be set to a series of strings. This would be properly handled by the Taipy Studio preview:

<p align="center">
  <img src="../images/preview_lov.png" width="80%"/>
</p>

<h5>Images</h5>

You can specify the image displayed by a
[`image`](../../../refmans/gui/viselements/generic/image.md) control in the
preview area by providing the path to the image file, relative to the root directory of the
project:

<p align="center">
  <img src="../images/preview_image.png" width="80%"/>
</p>

### Mock values

The Markdown preview pane of Taipy Studio supports the binding of a property to a value.<br/>

Because the Visual Studio Code preview is not connected to an actual application that could
provide values set to variables, Taipy Studio provides a means to mock the values of variables
bound to element properties.<br/>
You can create, in the project directory (where Visual Studio Code was launched), a file called
`taipy.mock.json`. This file must contain, in JSON format, the definition of a dictionary where
each key is a variable name, and each value defines the value to be assigned to the variable name.

Here is an example of how to use this feature:

<p align="center">
  <img src="../images/preview_data.png" width="80%"/>
</p>

The two controls defined in the Markdown file are bound to two variables (*text* and *value*). To
mock the connection to run-time variables, the `taipy.mock.json` file contains the definition of a
dictionary with two entries that are set to the values the controls should reflect for the preview
of the Markdown file.

!!! warning "No expression evaluation"
    Expressions are not evaluated: you can use "{value}" to evaluate the variable in the preview
    area, but expressions (such as "{value+1}") will **not** be replaced with their evaluation.

<!--TODO
    <br/>
    However, you can mock the expression evaluated value by added the expression itself as a
    value name in the `taipy.mock.json` file, as show here:
   <p align="center">
     <img src="../images/preview_data_eval.png" width="80%"/>
   </p>
-->

### Tabular values

The [`table`](../../../refmans/gui/viselements/generic/table.md) and
[`chart`](../../../refmans/gui/viselements/generic/chart.md) controls
can be previewed with relevant data, defined in the mock data file.

<h5>Table values</h5>

In the `taipy.mock.json` file, you can define an array that defines, for each row, the cell values
you want to preview. Each array element should be a dictionary that has to have an "id" property
that must be unique for each row.<br/>
The other properties can be set to the value you want to represent.<br/>
The column names referred to by the `table` control are the names of each row's property.

Here is an example of such a mock table data (source:
[Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population)):

<p align="center">
  <img src="../images/preview_tabledata.png" width="90%"/>
</p>

In `taipy.mock.json`, we have defined the value "world_pop", which is referenced in the table
control definition.<br/>
Each element of the "world_pop" defines an individual row in a dictionary that has the properties
"id", "Country", "Pop", and "World%". The table control definition explicitly references those
property names as the columns that must be shown.

<h5>Chart values</h5>

You can define a similar value in `taipy.mock.json` to feed charts. In the chart control
definition, you must set the *x* and *y* properties to the relevant property name in each
row's dictionary.

Here is how the dataset used above can be previewed as a chart:

<p align="center">
  <img src="../images/preview_chartdata.png" width="90%"/>
</p>

<h5>External data files</h5>

Taipy Studio can read external data files to provide tabular data to tables and charts. That makes
it possible to preview your own data without the burden of converting them.<br/>
You can create a CSV or a JSON file to hold the data you want to preview, then associate the
pathname of the data file to a value defined in `taipy.mock.json`.

The dataset that we have used above could have come from a CSV file:

```csv title="world_population.csv"
id,Country,Pop,World%
0,China,1411750000,17.5
1,India,1392329000,17.3
2,"United States",335065000,4.2
3,Indonesia,277749853,3.5
4,Pakistan,220425254,2.7
5,Nigeria,216783400,2.7
6,Brazil,203062512,2.5
7,Bangladesh,169828911,2.1
8,Russia,146424729,1.8
9,Mexico,129035733,1.6
10,Japan,124500000,1.5
11,Philippines,110886000,1.4
12,Ethiopia,105163988,1.3
13,Egypt,102060688,1.3
14,Vietnam,99460000,1.2
```

Then you can reference this data file from a value defined in `taipy.mock.json` and used as the
table's data source:

<p align="center">
  <img src="../images/preview_tabledatafile.png" width="90%"/>
</p>

This mechanism works the same way with JSON files, using the same format as if the data was
stored directly in `taipy.mock.json`.

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
    <img src="../images/diagnostics_mcs.png"/>
  </p>

- Missing opening tag on block elements (MOT).
  <p align="center">
    <img src="../images/diagnostics_mot.png"/>
  </p>

- Missing closing tag on block elements (MCT).
  <p align="center">
    <img src="../images/diagnostics_mct.png"/>
  </p>

- Missing opening tag with matching tag id (MOTI).
  <p align="center">
    <img src="../images/diagnostics_moti.png"/>
  </p>

- Missing closing tag with matching tag id (MCTI).
  <p align="center">
    <img src="../images/diagnostics_mcti.png"/>
  </p>

- Opening tag with unmatched tag id (UOTI).
  <p align="center">
    <img src="../images/diagnostics_uoti.png"/>
  </p>

- Closing tag with unmatched tag id (UCTI).
  <p align="center">
    <img src="../images/diagnostics_ucti.png"/>
  </p>

- Invalid property format (PE01).

- Invalid property name (PE02).<br/>
    Property names are dependent on the visual element type. Quick fix is available.
    <p align="center">
      <img src="../images/diagnostics_pe02.png"/>
    </p>

- Ignore negated value (PE03).<br/>
    Quick fix available: remove negated value.
    <p align="center">
      <img src="../images/diagnostics_pe03.png"/>
    </p>

- Function not found (FNF).<br/>
    This error is detected only in the context of a Python source file.
    <p align="center">
      <img src="../images/diagnostics_fnf.png"/>
    </p>
    Quick fix available: generate a function with the correct signature into the
    Python file:
    <p align="center">
      <img src="../images/diagnostics_fnf_quickfix.gif"/>
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
  <img src="../images/generation_viselement.gif"  width="90%"/>
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
  <img src="../images/snippet_control.gif" width="75%"/>
</p>
