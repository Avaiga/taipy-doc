---
title: <tt>login</tt>
hide:
  - navigation
---

<!-- Category: controls -->
A control that lets users enter their username and password.

If your application needs to authenticate the end user, you can use the `login` control that
provides the username/password input fields pair, ready to use.

This control stands on its own on an authentication page, and the application should navigate
to another page when the user has entered his user and password information (or canceled the
input).

# Properties


<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Default</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
<td nowrap><code id="p-title"><u><bold>title</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>str</code></td>
<td nowrap>"Log in"</td>
<td><p>The title of the login dialog.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_action">on_action</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of the function that is triggered when the dialog button is pressed.<br/><br/>All the parameters of that function are optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>id (str): the identifier of the button.</li>
<li>payload (dict): the details on this callback's invocation.<br/>
This dictionary has the following keys:
<ul>
<li>action: the name of the action that triggered this callback.</li>
<li>args: a list with three elements:<ul><li>The first element is the username</li><li>The second element is the password</li><li>The third element is the current page name</li></ul></li></li>
</ul>
</li>
</ul><br/>When the button is pressed, and if this property is not set, Taipy will try to find a callback function called <i>on_login()</i> and invoke it with the parameters listed above.</p></td>
</tr>
<tr>
<td nowrap><code id="p-message">message</code></td>
<td><code>str</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The message shown in the dialog.</p></td>
</tr>
<tr>
<td nowrap><code id="p-id">id</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The identifier that will be assigned to the rendered HTML component.</p></td>
</tr>
<tr>
<td nowrap><code id="p-properties">properties</code></td>
<td><code>dict[str, any]</code></td>
<td nowrap></td>
<td><p>Bound to a dictionary that contains additional properties for this element.</p></td>
</tr>
<tr>
<td nowrap><code id="p-class_name">class_name</code></td>
<td><code>str</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The list of CSS class names that will be associated with the generated HTML Element.<br/>These class names will be added to the default <code>taipy-&lt;element_type&gt;</code>.</p></td>
</tr>
<tr>
<td nowrap><code id="p-hover_text">hover_text</code></td>
<td><code>str</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The information that is displayed when the user hovers over this element.</p></td>
</tr>
  </tbody>
</table>

<p><sup id="dv">(&#9733;)</sup><a href="#p-title" title="Jump to the default property documentation."><code>title</code></a> is the default property for this visual element.</p>

# Details

If the user presses the 'Close' button (the cross at the top-right corner of the control), the
`on_action` callback is invoked with the two first elements of the array `payload.args`
(representing the input username and password) set to None.<br/>
This is how the application can know whether the user tried to provide the username and password
or if the authentication was canceled.

!!! warning "Using the Taipy Enterprise edition"

    If your application uses the Enterprise edition of Taipy, you can invoke the function
    `taipy.enterprise.gui.login()^` with the appropriate field to authenticate your session.

# Styling

All the login controls are generated with the "taipy-login" CSS class. You can use this class
name to select the login controls and apply style.

# Usage

## Typical use

You create a `login` control in a page to check for the user's credentials and navigate to the
appropriate page afterward.

The control definition can be as simple as:
!!! example "Definition"

    === "Markdown"

        ```
        <|Welcome to Taipy!|login|>
        ```

    === "HTML"

        ```html
        <taipy:login>Welcome to Taipy!</taipy:login>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.login("Welcome to Taipy!")
        ```

With this control, the page will look like this:
<figure class="tp-center">
    <img src="../login-init-d.png" class="visible-dark"  width="80%"/>
    <img src="../login-init-l.png" class="visible-light" width="80%"/>
    <figcaption>Login control after username and password were provided</figcaption>
</figure>

You may improve on the following simple code to implement what to do when users interact with
this control:
```python
def on_login(state: State, id, login_args):
    username, password = login_args["args"][:2]
    if username is None: # The user canceled the login request
        return navigate(s, "anonymous")

    # Check whether the username/password is a valid pair
    # Using Taipy Enterprise edition, you could use:
    #   credentials = taipy.enterprise.gui.login(state, username, password)
    ...

    #     # Store the username in the state
    state.username = username
    navigate(s, "authenticated")
```

If the user closes the control, the application opens the *anonymous* page.<br/>
Otherwise, the *authenticated* page opens, and the *state* has stored the username.
