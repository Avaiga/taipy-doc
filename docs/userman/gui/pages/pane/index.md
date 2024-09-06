---
hide:
    - toc
---

Modern user interfaces also provide small pages that pop out and be removed for
temporary use, such as providing specific parameters for the application. Taipy lets
you create such elements using the [pane](../../../../refmans/gui/viselements/generic/pane.md) block.

A pane can appear from any border of your page, next to or on top of the page, and
disappears when the user clicks outside its area.

Here is an example of how you would create a pane:

=== "Markdown"
    ```python
    from taipy.gui import Gui


    pane_is_visible = False
    name = ""

    def show_or_hide_pane(state):
        state.pane_is_visible = not state.pane_is_visible

    page = """
    <|Show pane|button|on_action=show_or_hide_pane|>

    <|{pane_is_visible}|pane|
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


    pane_is_visible = False
    name = ""

    def show_or_hide_pane(state):
        state.pane_is_visible = not state.pane_is_visible

    with tgb.Page() as page:
        tgb.button("Show pane", on_action=show_or_hide_pane)

        with tgb.pane(open="{pane_is_visible}"):
            tgb.text("Enter a name:")
            tgb.input("{name}")

    Gui(page).run()
    ```

Please refer to the documentation page on the [pane](../../../../refmans/gui/viselements/generic/pane.md) control for more details and examples.
