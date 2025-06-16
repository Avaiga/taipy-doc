Taipy GUI provides a set of utility features that enhance application development. While not core
structural elements like pages or visual components, these utilities offer useful interactions with
the application environment.<br/>
They include features like user notifications for alerts and access to local storage for data
persistence, enabling developers to build more interactive and dynamic applications with minimal
effort.

# Notifications

Taipy provides a way to inform users about ongoing actions through non-intrusive messages that do
not disrupt user interaction.<br/>
A **notification** is a short message displayed as a small popup at the bottom of the page. The
message’s urgency level is indicated by the popup’s color, and a close button ([MUI:Close]) allows
users to dismiss it manually.

Notifications can be triggered at any time using the `notify()^` function to send temporary messages
to users:
```python
notify(state, "success", "Taipy up and running!")
```

This results in a notification appearing on the current page:
<figure>
    <img src="../notifications-d.png" class="visible-dark" />
    <img src="../notifications-l.png" class="visible-light"/>
    <figcaption>Success notification</figcaption>
</figure>
By default, the notification remains visible for a duration controlled by the *duration* parameter
in `notify()^` or until the user closes it manually.

If browser permissions allow, notifications can also appear directly on the user’s desktop. This
behavior is controlled by the
[*system_notification*](../advanced_features/configuration/gui-config.md#p-system_notification)
configuration setting.

## Permanent notifications

The duration of a notification’s visibility can be customized. By default, notifications remain on
the screen for 3 seconds before disappearing. This default duration can be modified using the
[*notification_duration*](../advanced_features/configuration/gui-config.md#p-notification_duration)
configuration setting.

To make a notification permanent, set the *duration* parameter of the `notify()^` function to 0:
```python
notify(state, "info", "This is a permanent notification!", duration=0)
```
A permanent notification remains visible until the user clicks the close button.

Alternatively, your application can explicitly close the notification using
`close_notification()^`. To do this, the notification must be created with the *id* parameter set to
a non-empty string. This identifier is then required when calling `close_notification()^`.

This line creates a permanent notification with an identifier:
```python
notify(state, "error", "Important!", duration=0, id="my_notification")
```

To remove this notification programmatically, you can call:
```python
close_notification(state, id="my_notification")
```

## Grouping notifications

In some cases, your application may need to issue multiple notifications and remove them all at
once. This can be useful when a computation process involves several parallel steps, and you want to
keep the user informed of its progress.<br/>
Once all sub-processes are complete, you may want to close all related notifications simultaneously.

To achieve this, call `notify()^` for each step of the process, using the same notification
identifier. Then, a single call to `close_notification()^` with that identifier will remove all
associated notifications at the same time.

For example:
```python
notify(state, "info", "Step 1 completed", id="full_process")
notify(state, "info", "Step 2 completed", id="full_process")
notify(state, "info", "Step 3 completed", id="full_process")

...

# Remove all notifications with the same identifier
close_notification(state, id="full_process")
```

# Local storage

The local storage is a memory area within the user’s web browser where an application can store
information. This allows the application to remember certain data even after the page is refreshed
or the browser is closed, improving the user experience.

You can access the client's local storage using the `query_local_storage()^` function: given a
`State^` instance and one or several key names, this function retrieves the associated values from
the user agent and returns them to the application.

The following JavaScript snippet stores a data item in the application's local storage:
```javascript
localStorage.setItem("myKey", "My value");
```

If this code runs (from a script indicated in the `Gui.__init__()^`(`Gui` constructor) or an
[Extension Library](extension/index.md)), the application can retrieve the stored value using:
```python
from taipy.gui import query_local_storage

...

my_value = query_local_storage(state, "myKey")
```

# Mocking `State` in unit tests

Taipy includes the `MockState^` class to facilitate unit testing of stateful logic typically
executed in response to user interactions or programmatic events in a GUI application (*actions* and
*callbacks*). This can be used in frameworks like _unittest_ or *pytest*.

`MockState^` simulates a GUI state object, allowing you to test how your logic updates the
application state without needing to launch an actual UI. This is especially useful for testing
action callbacks, value assignments, and conditional logic in isolation.

You can create a `MockState^` instance by calling it constructor:

```python
MockState(gui: Gui, **initial_state_variables)
```

Where:

- _gui_ is an instance of `Gui^`, typically created with an empty or dummy page.
- _\*\*initial_state_variables_: Keyword arguments representing the initial values of state
  variables.<br/>
  Each key indicates the name of a variable that is managed in the state, and values define the
  initial values of these variables.

Here is an example of how this can be used:
```python
from taipy.gui import Gui
from taipy.gui.mock import MockState

def test_callback():
    def on_action(state: State):
        state.assign("my_var", "my_new_value")

    mock_state = MockState(Gui(""), my_var="my_value")
    on_action(mock_state)
    assert mock_state.my_var == "my_new_value"
```
