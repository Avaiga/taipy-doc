# Introduction to Visual Elements

_Visual Elements_ are user interface objects that are displayed on a given page.
Visual elements reflect some application data or give the page some structuring
or layout information. Most visual elements let users interact with the page content.

_Visual Elements_ are split into two categories:

   - _Controls_ typically represent user data that the user can interact with;

   - _Blocks_ let you organize controls (or blocks) in page to provide the best
    possible user experience.

If you are familiar with what _Visual Elements_ are and how they are declared, you
may want to jump directly to the list of the available visual elements:

[:material-arrow-right: List of available controls](../controls.md)

[:material-arrow-right: List of available blocks](../blocks.md)

## Properties

Every visual element you can use in a page has a type and a set of properties.
To add a visual component to your page, you have to use the appropriate syntax,
indicating what type of visual element you want to use in your page, and how to
set the properties of the element.

### Property name

Every control type has a default property name
If you want to set the value for this property,
you can use the short version of the control syntax.

### Property value

Every property value can be set to a given value that depends on the property type or a
formatted string literal, also known as an _f-string_. This string may reference variable
names defined in your code, and the property value becomes the evaluated string.

!!! note "Dynamic properties"
    When a property is listed as _dynamic_, this means that if the code changes the
    value of any variable in the expression, it will be sent automatically to the
    visual element that uses it.


## Syntax

You create visual elements using a specific Markdown syntax (see the
`Markdown^` class) or specific HTML tags (see the `Html^` class).

### Markdown

The basic syntax for creating Taipy constructs in Markdown is: `<|...|...|>` (opening with a
_less than_ character followed by a vertical bar character &#151; sometimes called
_pipe_ &#151; followed a potentially empty series of vertical bar-separated fragments and closing
by a vertical bar character immediately followed by the _greater than_ character).<br/>
Taipy interprets any text between the `<|` and the `|>` markers and tries to create visual
elements that are inserted in the resulting page.

The most common use of this construct is to create controls. Taipy expects the control type
name to appear between the two first vertical bar characters (like in `<|control|...}>`.

!!! important
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
    it would be the content of a [`text`](text.md) control, the label of a [`button`](button.md),
    or the data set displayed by a [`chart`](chart.md), for example.

Every following |-separated fragment is interpreted as a property name-property value
pair using the syntax: _property\_name=property\_value_ (note that _all_ space characters
are significative).  

So creating a visual element in Markdown text is just a matter of inserting a text
fragment similar to:

```
<|visual_element_type|property_name=property_value|...|>
```

!!! note
    You can have as many property name-property value pairs as needed, and all the space characters
    of the property value part _are_ significant:<br/>
    The fragment `<|Content |text|>` will be displayed as the string "Content" followed by a
    space character, because it is part the the propertly value (in this case, the _default_
    property value, which is the property called _value_ for the [`text`](text.md) control)

!!! note "Shortcut for Boolean properties"
    Should the `=property_value` fragment be missing, the property value is interpreted as the
    Boolean value `True`.<br/>
    Furthermore if the property name is preceded by the text "_no&blank;_", "_not&blank;_",
    "_don't&blank;_" or "_dont&blank;_" (including the trailing space character) then no
    property value is expected, and the property value is set to `False`.

#### Some examples

!!! example "Multiple properties"
    You can have several properties defined in the same control fragment:
    ```
    <|button|label=Do something|active=False|>
    ```

!!! example "The _default property_ rule"
    The default property name for the control type [`button`](button.md) is _label_. In Taipy,
    the Markdown text
    ```
    <|button|label=Some text|>
    ```
    Is exactly equivalent to
    ```
    <|Some text|button|>
    ```
    which is slightly shorter.

!!! example "The _missing Boolean property value_ rules"
    ```
    <|button|active=True|>
    ```
    is equivalent to
    ```
    <|button|active|>
    ```
    And
    ```
    <|button|active=False|>
    ```
    is equivalent to
    ```
    <|button|not active|>
    ```

There are very few exceptions to the `<|control_type|...|>` syntax, and these exceptions
are described in their respective documentation section. The most obvious exception is the
[`text`](text.md) control, which can be created without even mentioning its type.

### HTML

If you choose to embed Taipy visual elements into existing HTML pages, you can use the
following syntax:
```html
<taipy:visual_element_type property_name="property_value" ...> </visual_element_type>
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
    HTML. Instead, the page is transformed before it is rendered to HTML and delivered to
    the client. Therefore, Taipy was able to introduce a few changes to the pure HTML syntax
    that make it easier to use in the context of describing Taipy pages.

    - Attribute names that be array elements.
      Some visual elements (such as the [`chart`](chart.md) control) need
      indexed properties. An attribute name such as _y[1]_ is valid in the Taipy context,
      where it would not be in the raw HTML grammar.

    - Empty attribute value.
      In the HTML used by Taipy, you can mention an attribute with no value. It would
      be equivalent to setting it to `True`.

## Generic properties

Every visual element type has the following properties:

-   `id`: The identifier of the element, that gets generated in the HTML component.
-   `class_name`: An additional CSS class that is added to the generated HTML component.
    Note that all visual elements are generated with the "taipy-_visual_element_type_" CSS
    class set (ie. the `button` control generates an HTML element that has the
    _taipy-button_ CSS class).
-   `properties`: The name of a variable that holds a dictionary where all property name/value pairs will be used by a given visual element declaration.

All or most of the Taipy visual elements expose similar properties that can be used in a
generic manner across your pages.

### The `id` property

You can specify an identifier for a specific visual element.

This identifier is used as the `id` attribute of the generated HTML component so you
can use it in your CSS selectors.

!!! note
    This identifier is also sent to the _on_action_ function of the `Gui` instance, if this visual
    element can trigger actions.

### The `properties` property

There are situations where your visual element may need a lot of different properties.
This is typically the case for complex visual elements like the
[`chart`](chart.md) or the [`table`](table.md) controls.

When an element needs many properties and property values, the content may become
difficult to read. Something you can do about this is create a Python dictionary that
contains all the key-value pairs for your properties (name and value) then use the name
of the variable that holds that dictionary as the value of the `properties` property.

!!! Example

    Say your Markdown content needs the following control:
    `<|dialog|title=Dialog Title|open={show_dialog}|page_id=page|validate_action=validate_action|cancel_action=cancel_action||validate_action_text=Validate|cancel_action_text=Cancel|>`

    You can argue that this is pretty long and could be improved. In this situation, you might
    prefer to declare a simple Python dictionary in your code:

    ```py linenums="1"
    dialog_props = {
      "title":           "Dialog Title",
      "page_id":         "page",
      "validate_label":  "Validate",
      "validate_action": "validate_action",
      "cancel_label":    "Cancel",
      "cancel_action":   "cancel_action"
    }
    ```

    Then shorten your Markdown text with the following syntax:
    ```
    <{show_dialog}|dialog|properties=dialog_props|>
    ```

### The `propagate` property

If the `propagate` property is set to `True`, then the application variable bound to a
visual element is updated when the user modifies the value represented by the element.

!!! info
    Note that if there is a function called `on_change` declared on the `Gui` instance, it will be
    invoked no matter what the _propagate_ value is.

Besides those common properties, every visual element type has a specific set of properties that you
can use, listed in the documentation page for that visual element.
