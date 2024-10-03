Taipy GUI comes with predefined cascading stylesheets that solidify your application's
general look and feel. Those stylesheets also make it far easier to customize styles.</br>
All those stylesheets are grouped in what is called the *Stylekit*.

The Stylekit provides a few useful features:

- Predefined styles for Taipy GUI visual elements so they align better on the page;
- CSS variables that are used all over the stylesheets so that you can modify those
  variables and witness the propagation of graphical attributes such as color or
  spacing values;
- Utility CSS classes that can be used to make some elements appear with appealing
  attributes.

# Using the Stylekit

The Stylekit can apply to your pages if you choose and you can customize most of its properties.

## Enabling or disabling the Stylekit

By default, the Stylekit is enabled: the Stylekit stylesheets are loaded with your application
and impact all your application's page rendering.

In order *not* to use the Stylekit, you must specify the
[*stylekit*](../../advanced_features/configuration/gui-config.md#p-stylekit) configuration setting to False, or set it
to False in the call to `Gui.run()^`:
```py
gui.run(stylekit=False)
```

Note that setting [*stylekit*](../../advanced_features/configuration/gui-config.md#p-stylekit) to True is equivalent to using the
default variable values of the Stylekit.

## Customizing the Stylekit

The Stylekit defines a set of [variables](#variables) with default values. Those variables can be
overloaded by setting the [*stylekit*](../../advanced_features/configuration/gui-config.md#p-stylekit) parameter of the `Gui.run()^`
method to a dictionary: each key of this dictionary represents a Stylekit variable name, and you
would associate the new value for this variable to that key.

Here is how you can change the primary and secondary colors for your application:

```py
stylekit = {
  "color_primary": "#BADA55",
  "color_secondary": "#C0FFE",
}
gui.run(stylekit=stylekit)
```

The exhaustive list of all the Stylekit variables can be found in the
[Variables](#variables) section below.

# Variables

The Stylekit defines several variables that impact the overall style of your Taipy GUI
application pages. The values for these variables can be overloaded by providing a dictionary
to the [*stylekit*](../../advanced_features/configuration/gui-config.md#p-stylekit) parameter of the `Gui.run()^` method.

Each variable initializes a CSS custom property that you can use in your own stylesheets.<br/>
Details on the Stylekit's CSS custom properties can be found in the
[CSS custom properties](#css-custom-properties) section.

Here is the list of the variables that the Stylekit uses:

| Variable name   | Default value | CSS custom property | Comments |
| --------------- | ------------- | ------------------- | -------- |
| <a name="v-color-primary"></a>*color_primary*   | "#FF462B"     | [*--color-primary*](#p-color-primary) | Primary color used in elements. |
| <a name="v-color-secondary"></a>*color_secondary* | "#283282"     | [*--color-secondary*](#p-color-secondary)| Accent color used to make elements stand out from others. |
| <a name="v-color-error"></a>*color_error*     |	"#FF595E"	    | [*--color-error*](#p-color-error) | Color to indicate immediate danger or negative feedback. |
| <a name="v-color-warning"></a>*color_warning*   |	"#FAA916"	    | [*--color-warning*](#p-color-warning) | Color to indicate a potential risk or mixed feedback. |
| <a name="v-color-success"></a>*color_success*   |	"#96E6B3"     | [*--color-success*](#p-color-success) | Color to indicate success and positive feedback.
| <a name="v-color-background-light"></a>*color_background_light* | "#F0F5F7" | [*--color-background-light*](#p-color-background-light) | Background color for the light theme. |
| <a name="v-color-background-dark"></a>*color_background_dark*  | "#152335" | [*--color-background-dark*](#p-color-background-dark) | Background color for the dark theme.	|
| <a name="v-color-paper-light"></a>*color_paper_light*      | "#FFFFFF" | [*--color-paper-light*](#p-color-paper-light) | Elevated elements (i.e. *card*, *header*, *sidebar*…) background color for the light theme. |
| <a name="v-color-paper-dark"></a>*color_paper_dark*       | "#1F2F44" | [*--color-paper-dark*](#p-color-paper-dark) | Elevated elements (i.e. *card*, *header*, *sidebar*…) background color for the dark theme. |
| <a name="v-font-family"></a>*font_family*     | "Lato, Arial, sans-serif" | [*--font-family*](#p-font-family) | Font family. |
| <a name="v-border-radius"></a>*border_radius*   | 8 | *--border-radius* | Rounded corners radius. |
| <a name="v-input-button-height"></a>*input_button_height*    | "48px"    | *--input-button-height* | Matching buttons and inputs height. |

Notes:

- Color format: all CSS formats can be used, including the "#XXX" and "#XXXXXX" hexadecimal and "rgb(r,g,b)"
  formats.
- *border_radius* **must** be specified as an integer.
- *input_button_height* **must** be a string indicating an explicit unit (px, %, em, rem, or other).
- *font_family*: make sure, if you add a custom font to this variable, that it is properly imported
  by your stylesheets.<br/>
  For example, if you want to use the "Kanit" font from [Google Fonts](https://fonts.google.com/) in your application, you will need
  to add the directive:
  ```
  @import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,400;0,700;1,400');
  ```
  to one of your stylesheets.

# CSS custom properties

The Stylekit defines a set of custom properties used in style definitions to produce homogeneous
user interfaces, allowing one to change a single property and have it propagated in all the styles.

Besides the CSS custom properties derived from the [Stylekit variables](#variables), there are
a few more that the Stylekit styles rely on.

## Color

These properties are used to indicate what color to apply in styles.

| CSS custom property       | Default value | Comments |
| ------------------------- | ------------- | -------- |
| <a name="p-color-primary"></a>*--color-primary* | [*color_primary*](#v-color-primary) variable value (default: #FF462B) | Primary color to apply to elements. |
| <a name="p-color-secondary"></a>*--color-secondary* | [*color_secondary*](#v-color-secondary) variable value (default: #283282) | Accent color used to make elements stand out from others. |
| <a name="p-color-error"></a>*--color-error* | [*color_error*](#v-color-error) variable value (default: #FF595E) | Color to indicate immediate danger or negative feedback. |
| <a name="p-color-warning"></a>*--color-warning* | [*color_warning*](#v-color-warning) variable value (default: #FAA916) | Color to indicate a potential risk or mixed feedback. |
| <a name="p-color-success"></a>*--color-success* | [*color_success*](#v-color-success) variable value (default: #96E6B3) | Color to indicates success and positive feedback. |
| <a name="p-color-background-light"></a>*--color-background-light* | [*color_background_light*](#v-color-background-light) variable value (default: #F0F5F7) | Background color for the light theme. |
| <a name="p-color-background-dark"></a>*--color-background-dark* | [*color_background_dark*](#v-color-background-dark) variable value (default: #152335) | Background color for the dark theme.	|
| <a name="p-color-background"></a>*--color-background* | `var(--color-background-light)` or `var(--color-background-dark)`, depending on the current theme. | Theme-aware background color for pages. |
| <a name="p-color-paper-light"></a>*--color-paper-light* | [*color_paper_light*](#v-color-paper-light) variable value (default: #FFFFFF) | Elevated elements (i.e. card, header, sidebar…) background color for the light theme. |
| <a name="p-color-paper-dark"></a>*--color-paper-dark* | [*color_paper_dark*](#v-color-paper-dark) variable value (default: #1F2F44) | Elevated elements (i.e. card, header, sidebar…) background color for the dark theme. |
| <a name="p-color-paper"></a>*--color-paper*	          | `var(--color-paper-light)` or `var(--color-paper-dark)`, depending on the current theme. | Theme-aware background color for elevated elements. |
| <a name="p-color-contrast-light"></a>*--color-contrast-light*	| `rgba(0, 0, 0, 0.87)` | Contrasting elements (such as text) color for light backgrounds. |
| <a name="p-color-contrast-dark"></a>*--color-contrast-dark*	  | `rgba(255, 255, 255, 0.87)` | Contrasting elements (such as text) color for dark backgrounds. |
| <a name="p-color-contrast"></a>*--color-contrast*        | `var(--color-contrast-light)` or `var(--color-contrast-dark)`, depending on the current theme. | Theme-aware variable for contrasting elements such as text. |

Note that using [*--color-background*](#p-color-background), [*--color-paper*](#p-color-paper) or
[*--color-contrast*](#p-color-contrast) in your style definitions allows the Stylekit to automatically adapt
the setting of colors based on the theme the user has chosen.<br/>
That is not the case if you explicitly use *--color-background-light*, for example.

## Typography

These properties are used to indicate what text settings to apply in styles.

| CSS custom property     | Default value | Comments                       |
| ----------------------- | ------------- | ------------------------------ |
| <a name="p-font-family"></a>*--font_family* | [*font_family*](#v-font-family) variable value (default: Lato, Arial, sans-serif) | Font family used by elements. |
| *--font-size-h1*        | 2.5rem        | Font size for `h1` headings.   |
| *--font-size-h2*        | 2rem          | Font size for `h2` headings.   |
| *--font-size-h3*        | 1.75rem       | Font size for `h3` headings.   |
| *--font-size-h4*        | 1.5rem        | Font size for `h4` headings.   |
| *--font-size-h5*        | 1.25rem       | Font size for `h5` headings.   |
| *--font-size-h6*        | 1rem          | Font size for `h6` headings.   |
| *--font-weight-heading* | bold          | Font weight for headings.      |
| *--font-size-body*      | 1rem          | Base body font size.           |
| *--font-size-small*     | 0.875rem      | Smaller body font size.        |
| *--font-size-caption*   | 0.75rem       | Captions and hints font size.  |

For scalability and accessibility purposes, font sizes are set in the "rem" unit. This is a common
CSS best practice: "rem" is relative to the `<html>` element font size, so that if a user sets
an alternative text size using the browser settings, the "rem" reference value is impacted and
therefore, propagated to all text sizes.<br/>
If accessibility is not a concern in your application and you feel more comfortable setting the
font sizes in "px", you are, of course, free to do so.

## Spacing

These properties are used to add horizontal or vertical spacing between elements.<br/>
They all are multiple of the base *--spacing1* variable, ensuring a natural layout.

| CSS custom property                           | Default value                 | Comments                  |
| --------------------------------------------- | ----------------------------- | ------------------------- |
| <a name="p-spacing1"></a>*--spacing1*         | 1rem                          | Reference spacing value.  |
| <a name="p-spacing-half"></a>*--spacing-half* | `calc(var(--spacing1) * 0.5)` | Half of [*--spacing1*](#p-spacing1) |
| <a name="p-spacing2"></a>*--spacing2*         | `calc(var(--spacing1) * 2)`   | Double of [*--spacing1*](#p-spacing1) |
| <a name="p-spacing3"></a>*--spacing3*         | `calc(var(--spacing1) * 3)`   | Triple of [*--spacing1*](#p-spacing1) |
| <a name="p-spacing4"></a>*--spacing4*         | `calc(var(--spacing1) * 4)`   | Quadruple of [*--spacing1*](#p-spacing1) |
| <a name="p-spacing5"></a>*--spacing5*         | `calc(var(--spacing1) * 5)`   | Quintuple of [*--spacing1*](#p-spacing1) |
| <a name="p-spacing6"></a>*--spacing6*         | `calc(var(--spacing1) * 6)`   | Sixfold of [*--spacing1*](#p-spacing1) |

## Other properties

There are a few more CSS custom properties that the Stylekit relies on in classes that
can [style sections](#styled-sections):

| CSS custom property                           | Default value                 | Comments                  |
| --------------------------------------------- | ----------------------------- | ------------------------- |
| <a name="p-container-max-width"></a>*--container-max-width* | 75rem | The maximum width of section that use the [*container*](#container) CSS class. |
| <a name="p-element-padding"></a>*--element-padding* | `var(--spacing2)` | The inner margins of sections using the [*card*](#card) or [*sidebar*](#sidebar) classes. |
| <a name="p-sidebar-min-width"></a>*--sidebar-min-width* | 15rem | The minimum width of sections using the [*sidebar*](#sidebar) class. |

# CSS classes

The Stylekit defined several pre-defined CSS classes that are based on the
[CSS custom properties](#css-custom-properties) described above.

## Color

You can use the classes called *color_&lt;keyword&gt;* and *bg_&lt;keyword&gt;* to apply a text
or a background color to your elements.<br/>
Here is the list of available classes:

| CSS class                | Description |
| ------------------------ | ----------- |
| *color-primary*          | Uses [*--color-primary*](#p-color-primary) for the text color. |
| *bg-primary*             | Uses [*--color-primary*](#p-color-primary) for the background color. |
| *color-secondary*        | Uses [*--color-secondary*](#p-color-secondary) for the text color. |
| *bg-secondary*           | Uses [*--color-secondary*](#p-color-secondary) for the background color. |
| *color-error*            | Uses [*--color-error*](#p-color-error) for the text color. |
| *bg-error*               | Uses [*--color-error*](#p-color-error) for the background color. |
| *color-warning*          | Uses [*--color-warning*](#p-color-warning) for the text color. |
| *bg-warning*             | Uses [*--color-warning*](#p-color-warning) for the background color. |
| *color-success*          | Uses [*--color-success*](#p-color-success) for the text color. |
| *bg-success*             | Uses [*--color-success*](#p-color-success) for the background color. |
| *color-background*       | Uses [*--color-background*](#p-color-background) for the text color. |
| *bg-background*          | Uses [*--color-background*](#p-color-background) for the background color. |
| *color-background-light* | Uses [*--color-background-light*](#p-color-background-light) for the text color. |
| *bg-background-light*    | Uses [*--color-background-light*](#p-color-background-light) for the background color. |
| *color-background-dark*  | Uses [*--color-background-dark*](#p-color-background-dark) for the text color. |
| *bg-background-dark*     | Uses [*--color-background-dark*](#p-color-background-dark) for the background color. |
| *color-paper*            | Uses [*--color-paper*](#p-color-paper) for the text color. |
| *bg-paper*               | Uses [*--color-paper*](#p-color-paper) for the background color. |
| *color-paper-light*      | Uses [*--color-paper-light*](#p-color-paper-light) for the text color. |
| *bg-paper-light*         | Uses [*--color-paper-light*](#p-color-paper-light) for the background color. |
| *color-paper-dark*       | Uses [*--color-paper-dark*](#p-color-paper-dark) for the text color. |
| *bg-paper-dark*          | Uses [*--color-paper-dark*](#p-color-paper-dark) for the background color. |
| *color-contrast*         | Uses [*--color-contrast*](#p-color-contrast) for the text color. |
| *bg-contrast*            | Uses [*--color-contrast*](#p-color-contrast) for the background color. |
| *color-contrast-light*   | Uses [*--color-contrast-light*](#p-color-contrast-light) for the text color. |
| *bg-contrast-light*      | Uses [*--color-contrast-light*](#p-color-contrast-light) for the background color. |
| *color-contrast-dark*    | Uses [*--color-contrast-dark*](#p-color-contrast-dark) for the text color. |
| *bg-contrast-dark*       | Uses [*--color-contrast-dark*](#p-color-contrast-dark) for the background color. |

All these classes are defined using the "!important" priority setting, overriding all
previous styling rules.

## Typography

Typography classes let you style text fragments.

### Headers

You can give any text fragment a heading style using one of three methods:

- Using the appropriate `<h*>` HTML tag where `*` indicates the header level.
- Using the sharp notation of Markdown, where the number of sharp characters at the beginning of
  the line indicates the header level.
- Using one of the Stylekit CSS classes listed below.

| CSS class  | Description                      |
| ---------- | -------------------------------- |
| *h1*       | Mimics the `<h1>` tag default style. |
| *h2*       | Mimics the `<h2>` tag default style. |
| *h3*       | Mimics the `<h3>` tag default style. |
| *h4*       | Mimics the `<h4>` tag default style. |
| *h5*       | Mimics the `<h5>` tag default style. |
| *h6*       | Mimics the `<h6>` tag default style. |

The CSS class always takes precedence over the HTML tag: if, for some reason, you need an HTML
`<h3>` header using the style of `<h5>` tags, you would have to write:
```
<h3 class="h5">My heading</h3>
```

This is how you can do the same thing in Markdown text:
```
### My heading ### {: .h5}
```

### Body text

A few classes are available to style body text:

| CSS class           | Description                            |
| ------------------- | -------------------------------------- |
| *text-body*         | Mimics the body text default style.    |
| *text-small*        | Uses a smaller version of the body text. |
| *text-caption*      | Uses an even smaller version of the body text. |
| *text-weight300*    | Uses the "Light" font weight.          |
| *text-weight400*    | Uses the "Regular" font weight.        |
| *text-weight500*    | Uses the "Medium" font weight.         |
| *text-weight600*    | Uses the "Semi bold" font weight.      |
| *text-weight700*    | Uses the "Bold" font weight.           |
| *text-weight800*    | Uses the "Extra bold" font weight.     |
| *text-weight900*    | Uses the "Heavy" font weight.          |
| *text-left*         | Align text to the left.                |
| *text-center*       | Centers text.                          |
| *text-right*        | Aligns text to the right.              |
| *text-uppercase*    | Transforms text to uppercase.          |
| *text-no-transform* | Cancels all case transformations.      |
| *text-underline*    | Underlines text.                       |
| *text-no-underline* | Prevents the text underlining.         |

Notes:

- All these classes are defined using the "!important" priority setting, overriding all
  previous styling rules.
- By default, all body texts are applied the *text-body* style rules. You should use this
  class only for elements that have a different default style.
- Using specific font weights may require your application to load the appropriate fonts
  to render correctly.

## Spacing

These Stylekit classes let you add margins and padding to elements:

| CSS class | Description                                                   |
| --------- | ------------------------------------------------------------- |
| *m0*      | Removes margins from all sides.                               |
| *m-auto*  | Adds automatic margins to all sides (centering the element in its container) |
| *m-half*  | Adds a [*--spacing-half*](#p-spacing-half) margin value to all sides.        |
| *m1*      | Adds a [*--spacing1*](#p-spacing1) margin value to all sides. |
| *m2*      | Adds a [*--spacing2*](#p-spacing2) margin value to all sides. |
| *m3*      | Adds a [*--spacing3*](#p-spacing3) margin value to all sides. |
| *m4*      | Adds a [*--spacing4*](#p-spacing4) margin value to all sides. |
| *m5*      | Adds a [*--spacing5*](#p-spacing5) margin value to all sides. |
| *m6*      | Adds a [*--spacing6*](#p-spacing6) margin value to all sides. |
| *p0*      | Removes padding from all sides.                               |
| *p-half*  | Adds a [*--spacing-half*](#p-spacing-half) padding value to all sides. |
| *p1*      | Adds a [*--spacing1*](#p-spacing1) padding value to all sides. |
| *p2*      | Adds a [*--spacing2*](#p-spacing2) padding value to all sides. |
| *p3*      | Adds a [*--spacing3*](#p-spacing3) padding value to all sides. |
| *p4*      | Adds a [*--spacing4*](#p-spacing4) padding value to all sides. |
| *p5*      | Adds a [*--spacing5*](#p-spacing5) padding value to all sides. |
| *p6*      | Adds a [*--spacing6*](#p-spacing6) padding value to all sides. |

!!! note "Specifying the impacted side"
    You can specify which side of the element should be impacted by the spacing class.<br/>
    Adding the 't', 'b', 'l' or 'r' character after the 'm' or 'p' letter of the class name
    impacts only and respectively the top, bottom, left or right side of the target
    element.

    Examples: adding the classes *mt-1*, *pt0* and *mb_half* adds a *spacing1* margin
    to the top of the element, removes the padding to its top, and adds a *spacing-half*
    margin to its bottom.

All these classes are defined using the "!important" priority setting, overriding all
previous styling rules.

## Display

A few classes in the Stylekit have an impact on the CSS *display* property of the element
they apply to:

| CSS class        | Description                                                         |
| ---------------- | ------------------------------------------------------------------- |
| <a name="c-d-none"></a>*d-none*         | Hides the element and frees the space it would normally take.       |
| <a name="c-d-flex"></a>*d-flex*         | Makes the element a flexible layout block, so its direct children display horizontally. |
| <a name="c-d-block"></a>*d-block*        | Displays the element as a block on a new line.                      |
| <a name="c-d-inline"></a>*d-inline*       | Displays the element inline, horizontally, and treats it like text. |
| <a name="c-d-inline-block"></a>*d-inline-block* | Displays the element inline but keeps it treated as a block (e.g. for margins, paddings, etc). |

All these classes are defined using the "!important" priority setting, overriding all
previous styling rules.

## Opacity

The Stylekit provides a handful of CSS classes that deal with element opacity:

| CSS class          | Description                          |
| ------------------ | ------------------------------------ |
| *transparent*      | Turns the element transparent.<br/>Although it does not render any longer, the element is still present and occupies space. |
| *half-transparent* | Makes the element 50% transparent.   |
| *opaque*           | Restores the element’s full opacity. |

All these classes are defined using the "!important" priority setting, overriding all
previous styling rules.

# Leveraging the selected theme

The CSS custom properties are set in the `:root` selector.

If you need to reassign a custom property for a specific theme, you can do that by changing
its value on the `.taipy-light` or `.taipy-dark` selectors:

```
/* Default */
:root {
  --color-success: "#96E6B3";
}

/* Dark mode only */
.taipy-dark {
  --color-success: "#98E7D3";
}
```

The same technique can be used to customize CSS classes based on the theme:

```
/* Default selector for cards */
.card {
	box-shadow: 0 0 0.25rem 0.5rem rgba(0, 0, 0, 0.2);
}

/* Dark mode only cards */
.taipy-dark .card {
	box-shadow: none;
}
```

# Styled Sections

The Stylekit defines a few CSS classes that provide widely used styles for sections.<br/>
Although these can be used for any visual element, they are typically applied to the
[*part*](../../../refmans/gui/viselements/generic/part.md) and [*layout*](../../../refmans/gui/viselements/generic/layout.md) block element types.

These allow for making blocks stand out in pages, or be physically constrained at specific locations
with specific sizes.

The classes that the Stylekit define for this purpose are:

- [*container*](#container)
- [*card*](#card)
- [*header*](#header)
- [*sidebar*](#sidebar)

## `container`

The *container* class prevents the block it applies to from consuming all the available space.

The maximum width of that container is set by the [*--container-max-width*](#p-container-max-width)
custom property. Feel free to override this property in your stylesheets to adapt it to your own
needs.

Here is an example of the *container* class applied to a [`part`](../../../refmans/gui/viselements/generic/part.md) block.
In this example, we would have defined the additional class:
```css
.container-bg {
  background-color: rgb(80, 127, 172);
}
```

Now if the Markdown contains the following fragment:
```
Outside the container.
<|container container-bg|
Inside the container
|>
```

Then the result will look like this:
<figure>
  <img src="../container-d.png" class="visible-dark" />
  <img src="../container-l.png" class="visible-light"/>
  <figcaption>The <i>container</i> section style</figcaption>
</figure>

Note that we leverage the Markdown syntax to create a [`part`](../../../refmans/gui/viselements/generic/part.md) block:

- The default block element type name is "part", so it can be removed from the opening
  element syntax. This allows to write `<|container container-bg|` instead of
  `<|container container-bg|part|`.
- The default property name of the *part* block is *class_name*. So `<|container container-bg|`
  is equivalent to `<|part|class_name=container container-bg|`.

## `card`

The *card* class produces an elevated block to display the section in the flow of the page.

The *card* class uses the [*--element-padding*](#p-element-padding) custom property to
add padding around its content.

Let's look at an example using the *card* class.<br/>
Here is the Markdown content for a page:
```
Outside the card.
<|card card-bg|
Inside the card
{: .p1 .mb1 }
|>
```

This example relies on the definition of another CSS class that would look like this
in a stylesheet:
```css
.card-bg {
  background-color: rgb(211, 150, 109);
}
```

Here is how the page would be rendered:
<figure>
  <img src="../card-d.png" class="visible-dark" />
  <img src="../card-l.png" class="visible-light"/>
  <figcaption>The <i>card</i> section style</figcaption>
</figure>

## `header`

The *header* class can be applied on a [`layout`](../../../refmans/gui/viselements/generic/layout.md) or a
[`part`](../../../refmans/gui/viselements/generic/part.md) block to make it stand out from the content as an elevated bar.

*header* does not define any padding. If you need to tune the spacing of the elements
that appear in the styled section, you can use the [spacing classes](#spacing_1).

You can also apply the CSS class *sticky* to fix the header to the top of the page when
it is scrolled.

Here is an example of such a header. Consider the following Markdown content:
```
<|layout|columns=1fr auto 1fr|class_name=container align_columns_center|
<|part|class_name=pt_half pb_half|
<|Taipy App|text|height=30px|width=30px|>
|>
<|part|class_name=align_item_stretch|
<|navbar|lov={[("p1", "Page 1"), ("p2", "Page 2")]}|class_name=fullheight|>
|>
<|part|class_name=text_right|
<|toggle|theme|class_name=relative nolabel|>
|>
|>
```

This creates a three-columns *layout* block that has the *header* CSS class.

This block contains a label, a navigation bar and a theme toggle button.<br/>
Here is how the rendered page looks like:

<figure>
  <img src="../header-d.png" class="visible-dark" />
  <img src="../header-l.png" class="visible-light"/>
  <figcaption>The <i>header</i> section style</figcaption>
</figure>

## `sidebar`

The *sidebar* class produces an elevated area filling the entire height of the page and standing out from the general background and content.

Sections that use the *sidebar* class track the window scroll position. If its content is higher than the
window, it becomes a scrollable area.

The *sidebar* class uses two custom properties:

- [*--element-padding*](#p-element-padding): to add padding around its content.
- [*--sidebar-min-width*](#p-sidebar-min-width): the minimum width of the section. This can be useful
  to implement a responsive design to your pages.
