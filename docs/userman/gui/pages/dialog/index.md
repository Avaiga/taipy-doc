---
hide:
    - toc
---

Applications sometimes need to prompt the user to indicate a situation or request
input of some sort. Dialogs are forms that can be displayed on top of the page
the user is looking at, prompting for some input.

To create a dialog, you will use a [`dialog`](../../../../refmans/gui/viselements/generic/dialog.md) control in your
page. The dialog holds a page content or a *Partial* (see [Partials](../partial/index.md)).

You can control whether the dialog is visible or not, and what to do when the end-user
presses the *Validate* or *Cancel* button, so your application can deal with the
user's response.

Here is an example of how you would create a dialog:

=== "Markdown"
    ```python
    from taipy.gui import Gui


    dialog_is_visible = False
    name = ""

    def show_or_hide_dialog(state):
        state.dialog_is_visible = not state.dialog_is_visible

    page = """
    <|Show dialog|button|on_action=show_or_hide_dialog|>

    <|{dialog_is_visible}|dialog|title=Form|on_action=show_or_hide_dialog|
    Enter a name:

    <|{name}|input|>
    |>
    """

    Gui(page).run()
    ```

=== "Python"
    ```python
    from taipy.gui import Gui
    import taipy.gui.builder as tgb


    dialog_is_visible = False
    name = ""

    def show_or_hide_dialog(state):
        state.dialog_is_visible = not state.dialog_is_visible

    with tgb.Page() as page:
        tgb.button("Show dialog", on_action=show_or_hide_dialog)

        with tgb.dialog(open="{dialog_is_visible}", title="Form", on_action=show_or_hide_dialog):
            tgb.text("Enter a name:")
            tgb.input("{name}")

    Gui(page).run()
    ```
    

Please refer to the documentation page on the [`dialog`](../../../../refmans/gui/viselements/generic/dialog.md)
control for more details and examples.
