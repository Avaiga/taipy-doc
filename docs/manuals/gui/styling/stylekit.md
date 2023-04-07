# The Stylekit

Taipy GUI comes with predefined cascading stylesheets that solidify your application's
general look and feel. Those stylesheets also make it far easier to customize styles.</br>
All those stylesheets are grouped in what is called the *Stylekit*.

The Stylekit provides a few useful features:

- Predefined styles for Taipy GUI visual elements so they align better on the page;
- CSS variables that are used all over the stylesheets so that you can modify those
  variables and witness the propagation of specific graphical attributes;
- Utility CSS classes that can be used to make some elements appear with appealing
  attributes.

## Using the Stylekit

The Stylekit can apply to your pages if you choose and you can customize most of its properties.

### Enabling or disabling the Stylekit

By default, the Stylekit is enabled: the Stylekit stylesheets are loaded with your application
and impact all your application's page rendering.

In order *not* to use the Stylekit, you must specify the *stylekit* of the
`Gui.run()^` method to False:
```py
gui.run(stylekit=False)
```

Note that setting *stylekit* to True is equivalent to using the default variable values of
the Stylekit.

### Customizing the Stylekit

The Stylekit defines a set of [variables](#variables) with default values. Those variables can be
overloaded by setting the *stylekit* parameter of the `Gui.run()^` method to a dictionary:
each key of this dictionary represents a Stylekit variable name, and you would associate the new value
for this variable to that key.

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

## Variables

The Stylekit defines several variables that impact the overall style of your Taipy GUI
application pages. The values for these variables can be overloaded by providing a dictionary
to the *stylekit* parameter of the `Gui.run()^` method.

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
| <a name="v-border-radius"></a>*border_radius*   | 8 | [*--border-radius*](#p-border-radius) | Rounded corners radius. |
| <a name="v-input-button-height"></a>*input_button_height*    | "48px"    | [*--input-button-height*](#p-input-button-height) | Matching buttons and inputs height. |

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

## CSS custom properties

The Stylekit defines a set of custom properties used in style definitions to produce homogeneous
user interfaces, allowing one to change a single property and have it propagated in all the styles.

Besides the CSS custom properties derived from the [Stylekit variables](#variables), there are
a few more that the Stylekit styles rely on.

### Color

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

### Typography

These properties are used to indicate what text settings to apply in styles.

| CSS custom property     | Default value | Comments                       |
| ----------------------- | ------------- | ------------------------------ |
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

### Spacing

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

## CSS classes

The Stylekit defined several pre-defined CSS classes that are based on the 
[CSS custom properties](#css-custom-properties) described above.

### Colors

You can use the classes called *color_&lt;keyword&gt;* and *bg_&lt;keyword&gt;* to apply a text
or a background color to your elements.<br/>
Here is the list of available classes:

| CSS class                | Description |
| ------------------------ | ----------- |
| *color-primary*          | Use [*--color-primary*](#p-color-primary) for the text color. |
| *bg-primary*             | Use [*--color-primary*](#p-color-primary) for the background color. |
| *color-secondary*        | Use [*--color-secondary*](#p-color-secondary) for the text color. |
| *bg-secondary*           | Use [*--color-secondary*](#p-color-secondary) for the background color. |
| *color-error*            | Use [*--color-error*](#p-color-error) for the text color. |
| *bg-error*               | Use [*--color-error*](#p-color-error) for the background color. |
| *color-warning*          | Use [*--color-warning*](#p-color-warning) for the text color. |
| *bg-warning*             | Use [*--color-warning*](#p-color-warning) for the background color. |
| *color-success*          | Use [*--color-success*](#p-color-success) for the text color. |
| *bg-success*             | Use [*--color-success*](#p-color-success) for the background color. |
| *color-background*       | Use [*--color-background*](#p-color-background) for the text color. |
| *bg-default*             | Use [*--color-background*](#p-color-background) for the background color. |
| *color-background-light* | Use [*--color-background-light*](#p-color-background-light) for the text color. |
| *bg-default-light*       | Use [*--color-background-light*](#p-color-background-light) for the background color. |
| *color-background-dark*  | Use [*--color-background-dark*](#p-color-background-dark) for the text color. |
| *bg-default-dark*        | Use [*--color-background-dark*](#p-color-background-dark) for the background color. |
| *color-paper*            | Use [*--color-paper*](#p-color-paper) for the text color. |
| *bg-paper*               | Use [*--color-paper*](#p-color-paper) for the background color. |
| *color-paper-light*      | Use [*--color-paper-light*](#p-color-paper-light) for the text color. |
| *bg-paper-light*         | Use [*--color-paper-light*](#p-color-paper-light) for the background color. |
| *color-paper-dark*       | Use [*--color-paper-dark*](#p-color-paper-dark) for the text color. |
| *bg-paper-dark*          | Use [*--color-paper-dark*](#p-color-paper-dark) for the background color. |
| *color-contrast*         | Use [*--color-contrast*](#p-color-contrast) for the text color. |
| *bg-contrast*            | Use [*--color-contrast*](#p-color-contrast) for the background color. |
| *color-contrast-light*   | Use [*--color-contrast-light*](#p-color-contrast-light) for the text color. |
| *bg-contrast-light*      | Use [*--color-contrast-light*](#p-color-contrast-light) for the background color. |
| *color-contrast-dark*    | Use [*--color-contrast-dark*](#p-color-contrast-dark) for the text color. |
| *bg-contrast-dark*       | Use [*--color-contrast-dark*](#p-color-contrast-dark) for the background color. |

All these classes are defined using the "!important" priority setting, overriding all
previous styling rules.

### Typography

Typography classes let you style text fragments.

#### Headers

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

#### Body text

A few classes are available to style body text:

| CSS class           | Description                            |
| ------------------- | -------------------------------------- |
| *text-body*         | Mimics the body text default style.    |
| *text-small*        | Smaller version of the body text.      |
| *text-caption*      | Even smaller version of the body text. |
| *text-weight300*    | "Light" font weight.                   |
| *text-weight400*    | "Regular" font weight.                 |
| *text-weight500*    | "Medium" font weight.                  |
| *text-weight600*    | "Semi bold" font weight.               |
| *text-weight700*    | "Bold" font weight.                    |
| *text-weight800*    | "Extra bold" font weight.              |
| *text-weight900*    | "Black" font weight.                   |
| *text-left*         | Align text to the left.                |
| *text-center*       | Center text.                           |
| *text-right*        | Align text to the right.               |
| *text-uppercase*    | Transform text to uppercase.           |
| *text-no-transform* | Cancel all case transformations.       |
| *text_underline*    | Underline text.                        |
| *text_no_underline* | Do not underline text.                 |

Notes:

- All these classes are defined using the "!important" priority setting, overriding all
  previous styling rules.
- By default, all body texts are applied the *text-body* style rules. You should use this
  class only for elements that have a different default style.
- Using specific font weights may require your application to load the appropriate fonts
  to render correctly.

### Spacing

These Stylekit classes let you add margins and padding to elements:

| CSS class | Description                            |
| --------- | -------------------------------------- |
| *m0*      | Remove margins from all sides.                               |
| *m-auto*  | Add automatic margins to all sides (centering the element in its container) |
| *m-half*  | Add a [*--spacing-half*](#p-spacing-half) margin value to all sides.        |
| *m1*      | Add a [*--spacing1*](#p-spacing1) margin value to all sides. |
| *m2*      | Add a [*--spacing2*](#p-spacing2) margin value to all sides. |
| *m3*      | Add a [*--spacing3*](#p-spacing3) margin value to all sides. |
| *m4*      | Add a [*--spacing4*](#p-spacing4) margin value to all sides. |
| *m5*      | Add a [*--spacing5*](#p-spacing5) margin value to all sides. |
| *m6*      | Add a [*--spacing6*](#p-spacing6) margin value to all sides. |
| *p0*      | Remove padding from all sides.                               |
| *p-half*  | Add a [*--spacing-half*](#p-spacing-half) padding value to all sides. |
| *p1*      | Add a [*--spacing1*](#p-spacing1) padding value to all sides. |
| *p2*      | Add a [*--spacing2*](#p-spacing2) padding value to all sides. |
| *p3*      | Add a [*--spacing3*](#p-spacing3) padding value to all sides. |
| *p4*      | Add a [*--spacing4*](#p-spacing4) padding value to all sides. |
| *p5*      | Add a [*--spacing5*](#p-spacing5) padding value to all sides. |
| *p6*      | Add a [*--spacing6*](#p-spacing6) padding value to all sides. |

!!! note "Specifying the impacted side"
    You can specify which side of the element should be impacted by the spacing class.<br/>
    Adding the 't', 'b', 'l' or 'r' character after the 'm' or 'p' letter of the class name
    impacts only and respectively the top, bottom, left or right side of the target
    element.

    Examples: adding the classes *mt-1*, *pt0* and *mb_half* adds a *spacing1* margin
    to the top of the element, removes the padding to its top, and adds a *spacing-half*
    margin to its bottom. 


## Leveraging the selected theme

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

## Boxes (?)

TODO
