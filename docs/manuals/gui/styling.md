# Styling

As mentioned several times, page content is parsed and converted to be sent
to the user's browser. The final page content actually is pure HTML that one can apply
some style to, providing the best user experience.

Styling involves some knowledge of [Cascading Style Sheets](https://www.w3.org/Style/CSS/).
This section describes what sort of styling you may want to apply, in different situations.

## Style sheets

There are two ways you can apply a stylesheet to your application:

- Global style sheet.<br/>
  The _css_file_ parameter of the [`Gui` constructor](Gui.__init__()^) lets you
  specify a CSS file that your application will use for every page. The default value
  for this parameter is a file located next to your main Python script, with the
  same name except for the extension that must be '.css'.

- Page-specific style.<br/>
  The method `Gui.add_page()^` has a _style_ parameter that can be set to CSS content.
  This additional style is applied to the page and **only** this page.

Beside explicit style sheets, you can also modify the global theme, as
described in the [section on Themes](#themes).

## Applying style

Once the style sheets are set for the application, you can start learning about
how styles can be expressed to pages.

### Global styles

As in any Web application, the root element (`:root`) is available for global
style settings.<br/>
For example, if you want to make your application bigger, enlarging the
font size, you could write:
```css
:root {
  font-size: 2rem;
}
```
And all pages will appear twice as big.


### Markdown styles

Thanks to the [_Attribute Lists_](https://python-markdown.github.io/extensions/attr_list/)
extension, the Markdown text can hold attributes used for styling.

If, for example, your Markdown content is the following:
```
...
This line should be displayed in blue.
{ .blue-line }
...
```

and a style sheet used by the application indicates:
```css
.blue-line {
  color: blue;
}
```
then the text line is displayed in blue.

Please check the documentation for the _Attribute Lists_ extension to find
more information.

!!! note "div vs. p"
    Instead of generating &lt;p&gt; HTML tags for lines of text, Taipy
    uses &lt;div&gt; tags. This allows more complex structures in pages,
    such as elements within elements.

### Main page style

The top-most element of the generated page is a &lt;div&gt; element with
the 'id' attribute set to "root".

If you need to reference the top-most element of your page, you 
can select it in your CSS stylesheets using the selector: `div#root`.

### Visual elements-specific styles

You can apply some style to any visual element you have added to
your pages.

#### Using CSS classes

Every visual element is assigned a CSS class that depends on the type
of the element.<br/>
The default associated class name is made of the string _"taipy-"_ followed
by the type of element: all Taipy buttons, for example, have the CSS
class name: _"taipy-button"_.

You can therefore create a weird-looking button displayed in an
oval by setting a style sheet that contains:
```css
.taipy-button {
  border-radius: 50%;
}
```
Now all the buttons of your application will look the same, with an oval
shape instead of a rectangle with rounded corners.

If your Markdown page contains the following control:
```
<|Click me|button|>
```

The CSS rule above will impact your display this way:

<div style="display: flex">
  <figure>
    <img src="../images/regular-button-d.png" class="visible-dark" />
    <img src="../images/regular-button-l.png" class="visible-light" />
    <figcaption>Regular button</figcaption>
    </figure>
  <figure>
    <img src="../images/rounded-button-d.png" class="visible-dark" />
    <img src="../images/rounded-button-l.png" class="visible-light" />
    <figcaption>Rounded button</figcaption>
    </figure>
  </div>

You can also add CSS class names of your choice using the _classname_
property of all visual elements. If you need to assign more than one
class to an element, you can separate each individual class name with
a space character:
```
<|Click me|button|classname="option testing"|>
```
This Markdown fragment gets converted into an HTML element with three CSS classes
assigned: _taipy-button_, _option_, and _testing_.

#### Using the HTML 'id' attribute

You can use the _id_ property of all visual elements to generate an
HTML id that can be used by CSS styling.

For example, if your Markdown page contains the following control:

```
<|Click me|button|id="my_button"|>
```

You can change the style of that button using a CSS selector that
relies on the id of the button:
```css
#my_button {
  text-transform: none;
}
```
Now the button shows the text 'Click me' instead of 'CLICK ME': the default
in Material UI (which is the components library Taipy GUI relies on) is to
capitalize the text of buttons.

<div style="display: flex">
  <figure>
    <img src="../images/regular-button-d.png" class="visible-dark" />
    <img src="../images/regular-button-l.png" class="visible-light" />
    <figcaption>Regular button</figcaption>
    </figure>
  <figure>
    <img src="../images/no-case-button-d.png" class="visible-dark" />
    <img src="../images/no-case-button-l.png" class="visible-light" />
    <figcaption>Uncapitalized button</figcaption>
    </figure>
  </div>


## Themes

The visual elements that Taipy GUI generates are extensions of
[Material UI](https://mui.com/) components. This components library has great
support for theming, so you can customize how things will look across all components.

Material UI exposes the full API for handling themes, which you can find
on the [MUI Theming](https://mui.com/customization/theming/) page.

To change the theme of your application, you must use the _theme_ configuration
parameter (for example in the `Gui.run()` method) as explained in the
[Configuration](configuration.md) section. You could also impact only the _light_
or the _dark_ theme using the _light_theme_ or _dark_theme_ configuration settings.

Here is how you would change the general theme if you wanted the background
color to be a neutral gray color (#808080 in CSS) and make the primary color
an orange-looking color instead of the default blue color.<br/>
In your Python code, you would create a theme dictionary and provide it as
the value of the _theme_ parameter of the method `Gui.run()`:

```py
...
my_theme = {
  "palette": {
    "background": {"default": "#808080"},
    "primary": {"main": "#a25221"}
  }
}
...
gui.run(theme=my_theme)
```

See the impact of setting this custom theme:

<div style="display: flex">
  <figure>
    <img src="../images/no-theme-d.png" class="visible-dark" />
    <img src="../images/no-theme-l.png" class="visible-light"/>
    <figcaption>Regular button</figcaption>
    </figure>
  <figure>
    <img src="../images/theme.png" />
    <figcaption>Themed button</figcaption>
    </figure>
  </div>


