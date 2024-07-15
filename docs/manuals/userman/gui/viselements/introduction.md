---
title: Introduction to Visual Elements
---

# Properties

Each visual element has a type and a set of properties.
To add a visual component to a page, appropriate syntax must be used,
indicating the type of visual element and the properties of the element.

## Property name

Every element type has a default property name that holds its 'main'
representation: a string for a text element, an array for a selector, or
a numerical value for a slider.

To set the value for this property, the short syntax for the visual element
syntax can be used.

## Property value

Every property value can be set to a value that depends on the property type or a
formatted string literal, also known as an *f-string*. This string may reference variable
names defined in the code, and the value of the property is set to the evaluated string.

!!! note "Dynamic properties"
    When a property is listed as *dynamic*, changing the value of any variable in its expression's
    value will immediately update the visual element that uses it. All properties are *not*
    dynamic, though, for performance reasons: when a Python variable bound to an element's property
    is modified, it can tremendously impact the rendering of the graphical component on the page
    displayed by the user's browser. The component may have to be entirely rebuilt to reflect the
    new variable value, which might be slow and hit the user experience.<br/>
    Visual Elements that are costly to render on the browser provide a property called *rebuild*
    that allows one to explicitly request the render of the component. Please check the relevant
    sections for the [`chart`](standard-and-blocks/chart.md#the-rebuild-property) and
    [`table`](standard-and-blocks/table.md#the-rebuild-property) controls for more information.

# Syntax

Depending on the technique you have used to create your application pages (see the section on
[Page](../pages/index.md)), visual elements are created with specific syntaxes:

## Markdown

This applies when the page is defined using [Markdown](../pages/markdown.md).

The basic syntax for creating Taipy constructs in Markdown is: `<|...|...|>` (opening with a
*less than* character followed by a vertical bar character &#151; sometimes called
*pipe* &#151; followed by a potentially empty series of vertical bar-separated fragments and
closing with a vertical bar character immediately followed by the *greater than* character).<br/>
Taipy interprets any text between the `<|` and the `|>` markers and tries to create visual
elements to be inserted in the resulting page.

The most common use of this construct is to create controls. Taipy expects the control type
name to appear between the two first vertical bar characters (as in `<|control|...}>`).

!!! note "Shortcut for the default property"
    If the first fragment text is not the name of a control type, Taipy will consider this
    fragment to be the default value for the default property of the control, whose type name
    must then appear as the second element.

    ```
    <|visual_element_type|default_property_name=default_property_value|>
    ```
    Is equivalent to
    ```
    <|default_property_value|visual_element_type|>
    ```

    Every visual element has a default property, and using the default property syntax
    (where the default property value appears as the first `||` fragment) underscore,
    but placing it first, the most important property value for this visual element:
    it would be the content of a [`text`](standard-and-blocks/text.md) control, the
    label of a [`button`](standard-and-blocks/button.md),
    or the data set displayed by a [`chart`](standard-and-blocks/chart.md), for example.

Every following |-separated fragment is interpreted as a property name-property value
pair using the syntax: *property\_name=property\_value* (note that *all* space characters
are significant).

So creating a visual element in Markdown text is just a matter of inserting a text
fragment similar to:

```
<|visual_element_type|property_name=property_value|...|>
```

!!! note "Multiple properties"
    You can have as many property name-property value pairs as needed and all the space
    characters of the property value part *are* significant:<br/>
    The fragment `<|Content |text|>` will be displayed as the string "Content" followed by a
    space character because it is part of the property value (in this case, the *default*
    property value, which is the property called *value* for the [`text`](standard-and-blocks/text.md) control)

!!! note "Shortcut for Boolean properties"
    Should the `=property_value` fragment be missing, the property value is interpreted as the
    Boolean value `True`.<br/>
    Furthermore, if the property name is preceded by the text "no&blank;", "not&blank;",
    "don't&blank;" or "dont&blank;" (including the trailing space character), then no
    property value is expected, and the property value is set to `False`.

!!! note "Unknown properties"
    If you set a property that a visual element does not recognize, it is
    ignored without any warning.

!!! note "Indentation and block elements: element tag identifiers"
    Markdown depends heavily on text indentation to decide whether a new paragraph or
    section should be created.<br/>
    When dealing with block elements to create sections on your page, you might be
    tempted to indent the opening element tags, so the Markdown text is easier to read.

    The following Markdown content:
    ```
    <|
    The part content
    <|
    First sub-part content.
    |>
    <|
    Second sub-part content.
    |>
    |>
    ```
    would be easier to read if indented, as shown here:
    ```
    <|
      The part content
      <|
      First sub-part content.
      |>
      <|
      Second sub-part content.
      |>
    |>
    ```
    Finding the opening '<|' when looking at a '|>' fragment is far easier, and you have a hint of
    the elements' structure.<br/>
    Unfortunately, this indentation may break the Markdown parsing, and your page will not look
    how you expected.

    Taipy GUI provides a way for you to simplify the match of a closing element tag with its
    opening element tag.<br/>
    You can use, instead of the '<|...|>' sequence, the '<*id*|...|*id*>' where *id* must be a
    valid Python identifier. Then the parsing of the Markdown content will indicate structural
    problems (like element tags that don't match), and you can find matching element tags easier.

    The example above could use this feature:
    ```
    <main_section|
    The part content
    <sub_section1|
    First sub-part content.
    |sub_section1>
    <sub_section2|
    Second sub-part content.
    |sub_section2>
    |main_section>
    ```

### Some examples

!!! example "Multiple properties"
    You can have several properties defined in the same control fragment:
    ```
    <|button|label=Do something|active=False|>
    ```

!!! example "The *default property* shortcut"
    The default property name for the control type [`button`](standard-and-blocks/button.md)
    is *label*. In Taipy, the Markdown text
    ```
    <|button|label=Some text|>
    ```
    Is exactly equivalent to
    ```
    <|Some text|button|>
    ```
    which is slightly shorter.

!!! example "The *missing Boolean property value* shortcuts"
    Defining a Boolean property with no value is equivalent to setting that property to True:
    ```
    <|button|active=True|>
    ```
    is equivalent to
    ```
    <|button|active|>
    ```

    Prefixing a Boolean property name with "no&blank;", "not&blank;", "don't&blank;" or
    "dont&blank;" and not setting the property value is equivalent to setting that property to
    False:
    ```
    <|button|active=False|>
    ```
    is equivalent to
    ```
    <|button|not active|>
    ```

There are very few exceptions to the `<|control_type|...|>` syntax, which
are described in their respective documentation section. The most obvious exception is the
[`text`](standard-and-blocks/text.md) control, which can be created without even mentioning its type.

## HTML

This applies when the page is defined using [HTML](../pages/html.md).

If you choose to embed Taipy visual elements into existing HTML pages, you can use the
following syntax:
```html
<taipy:visual_element_type property_name="property_value" ...> </taipy:visual_element_type>
```

The text element of the visual element tag can be used to indicate the default property
value for this visual element:
```html
<taipy:visual_element_type default_property_name="default_property_value" ... />
```
is equivalent to
```html
<taipy:visual_element_type>default_property_value</taipy:visual_element_type>
```

!!! info "HTML syntax extensions"

    The HTML text that is given to the `Html^` page renderer is **not** parsed as pure
    HTML. Rather, the page is transformed before it is rendered to HTML and delivered to
    the client. Therefore, Taipy was able to introduce a few changes to the pure HTML syntax
    that make it easier to use in the context of describing Taipy pages.

    - Attribute names that be array elements.
      Some visual elements (such as the [`chart`](standard-and-blocks/chart.md) control)
      need *indexed* properties. An attribute name such as *y[1]* is valid in the Taipy
      context, where it would not be in the raw HTML grammar.

    - Empty attribute value.
      In the HTML used by Taipy, you can mention an attribute with no value. It would
      be equivalent to setting it to `True`.

    - Boolean attribute value.
      The [HTML specification](http://www.w3.org/TR/html5/) indicates that if a Boolean attribute
      is omitted in the tag definition, its value defaults to 'false'. This is not the case
      for Taipy's visual elements: some Boolean property values default to 'true'.<br/>
      To set an element property to 'false', you must explicitly indicate it:
      `<taipy:e bool_attr="false"/>`.<br/>
      Note that the paragraph above indicates that one can specify no value for a property,
      resulting in setting it to 'true', which does respect the HTML specification:
      `<taipy:e bool_attr/>` is equivalent to `<taipy:e bool_attr="true"/>`.

## Page Builder API

If you use Python code to create pages, the
[Page Builder](../../../refmans/reference/pkg_taipy.gui.builder.md) package provides the API for all the
available visual elements.

To set a property to a value, you will use the property name as a named parameter to the element's
API.<br/>
Note that to bind variables to an element's property, you must set that property to a string
defining an expression referencing the variables.

# Generic properties

Every visual element type has the following properties:

-   `id`: The identifier of the element. This identifier is generated in the HTML component
    and can be used for [styling](../styling/index.md).
-   `class_name`: An additional CSS class that is added to the generated HTML component.
    Note that all visual elements are generated with the "taipy-*visual\_element\_type*" CSS
    class set (e.g. the `button` control generates an HTML element that has the
    *taipy-button* CSS class).
-   `properties`: The name of a variable that holds a dictionary where all property name/value
    pairs will be used by a given visual element declaration.

All or most Taipy visual elements expose similar properties that can be used generically
across your pages.

## The `id` property

You can specify an identifier for a specific visual element.

This identifier is used as the `id` attribute of the generated HTML component, so you
can use it in your CSS selectors. You can look at the [Styling](../styling/index.md)
section for more information.

!!! note
    This identifier is also sent to the `on_action` callback if this visual
    element can trigger actions (see [Actions](../callbacks.md#actions)
    for details).

## The `properties` property

There are situations where your visual element may need a lot of different properties.
This is typically the case for complex visual elements like the
[`chart`](standard-and-blocks/chart.md) or the [`table`](standard-and-blocks/table.md) controls.

When an element needs many properties and property values, the content may become
difficult to read. Something you can do about this is creating a Python dictionary that
contains all the key-value pairs for your properties (name and value), then use the name
of the variable that holds that dictionary as the value of the `properties` property.

!!! example

    Say your Markdown content needs the following control:
    `<|dialog|title=Select an item in the list|open={show_dialog}|labels=Cancel;Validate|page_id=page|close_label=Cancel|>`

    As this syntax can be cumbersome, you might prefer to define a simple Python dictionary:

    ```python linenums="1"
    dialog_props = {
      "title":       "Select an item in the list",
      "labels":      "Cancel;Validate",
      "page_id":     "page",
      "close_label": "Cancel"
    }
    ```

    Then shorten your Markdown text with the following syntax:
    ```
    <|{show_dialog}|dialog|properties=dialog_props|>
    ```

## The `propagate` property

There are situations where you don't want a variable bound to a control value (such
as the knob location of a slider) to be updated immediately when the user manipulates
the control. You may for example want to check the received value in the `on_change`
callback and decide to use this new value or not.<br/>
This is the purpose of the *propagate* property.

When the *propagate* property is set to True, then the application variable bound to a
control is updated when the user modifies the value represented by the control.

!!! info
    Note that if there is a function called `on_change()` accessible to the `Gui` instance
    (see the section on [Variable Value Change](../callbacks.md#variable-value-change) for
    details), it will be invoked no matter what the *propagate* value is. The variable
    value that this function receives is the new requested value, but this value is
    **not** set to the variable bound to the control.

Besides those common properties, every visual element type has a specific set of properties that
you can use, listed in the documentation page for each visual element.
