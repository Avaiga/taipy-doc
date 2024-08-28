Callbacks are functions that are created in the application that are
invoked in response to user actions in generated pages or other events that the
web browser requires that the application handles.

Every callback function receives a `State^` object as its first parameter.<br/>
This object reflects the state of the application variables, for a given end-user:
your application may be used simultaneously by different users connected to the
same web server (note that setting the _single_client_ configuration parameter to
False - as explained in the
[Configuration](../configuration/gui-config.md#configuring-the-gui-instance) section - prevents
multiple users from connecting to your application simultaneously, but you still rely
on the `State^` object to access the application variables that are represented in your
user interfaces).<br/>
When visual elements use application variables (see the [Binding](binding.md)
section), the `State` class is provided an accessor to these variables, both
for reading and writing.

### Types of Callbacks

1. **Global Callbacks**: They are basic callbacks that are triggered by specific events in your application. Taipy recognizes these name functions and will use them if defined.
   - `on_init`: Initialize application state when a client connects.
   - `on_change`: React to changes in application variables.
   - `on_action`: Handle user interactions, such as button clicks.
   - `on_navigate`: Manage navigation between pages.
   - `on_exception`: Handle exceptions raised in callbacks.

=== "on_init"
    ```py

    ```
=== "on_change"

=== "on_action"

=== "on_navigate"

=== "on_exception"

2. **Local Callbacks**:
   - `on_change` and `on_action` callbacks attached directly to visual elements.

3. **Asynchronous Callbacks**:
   - Handling long-running tasks with `invoke_long_callback`.
   - Monitoring task status and progress.

4. **Core Events**:
   - `on_submission_change`: Track submission status changes using core events.