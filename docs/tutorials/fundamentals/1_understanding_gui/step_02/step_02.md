[Download Step 2](./../src/step_02.zip){: .tp-btn target='blank' }
[Download the entire code](./../src/src.zip){: .tp-btn .tp-btn--accent target='blank' }



You can incorporate various visual elements into the basic code demonstrated in Step 1.
This step illustrates how to utilize visual elements such as charts, sliders, tables, and
more within the graphical interface.

Taipy uses different ways to create
pages: [Markdown](../../../../manuals/userman/gui/pages/markdown.md),
[HTML](../../../../manuals/userman/gui/pages/html.md) or
[Python code](../../../../manuals/userman/gui/pages/builder.md). You can choose which you want
to learn in the code snippets below.

## Visual elements

Taipy uses the **[visual element](../../../../manuals/userman/gui/viselements/index.md)**
concept to bring interactivity to the application. A visual element is a
Taipy graphical object displayed on the client. It can be a
[slider](../../../../manuals/userman/gui/viselements/standard-and-blocks/slider.md), a
[chart](../../../../manuals/userman/gui/viselements/standard-and-blocks/chart.md), a
[table](../../../../manuals/userman/gui/viselements/standard-and-blocks/table.md), an
[input](../../../../manuals/userman/gui/viselements/standard-and-blocks/input.md), a
[menu](../../../../manuals/userman/gui/viselements/standard-and-blocks/menu.md), etc.
Check the complete list
[here](../../../../manuals/userman/gui/viselements/index.md).

Every visual element follows a similar syntax:

=== "Markdown"
    ```
    <|{variable}|visual_element_name|param_1=param_1|param_2=param_2| ... |>
    ```
=== "Python"
    ```python
    tgb.visual_element_name("{variable}", param_1=param_1, param_2=param_2, ...)
    ```

    The inclusion of *variable* within `"{...}"` tells Taipy to show and use the
    real-time value of *variable*. Rather than re-executing the entire script,
    Taipy intelligently adjusts only the necessary elements of the GUI to reflect
    changes, ensuring a responsive and performance-optimized user experience.

For example, a [slider](../../../../manuals/userman/gui/viselements/standard-and-blocks/slider.md) is written this way :


=== "Markdown"
    ```
    <|{variable}|slider|min=min_value|max=max_value|>
    ```
=== "Python"
    ```python
    tgb.slider("{variable}", min=min_value, max=max_value, ...)
    ```

For example, at the beginning of the page, if you want to display:

- a Python variable *text*

- an input that "visually" modifies the value of __text__.

Here is the overall syntax:

=== "Markdown"
    ```
    <|{text}|>
    <|{text}|input|>
    ```
=== "Python"
    ```python
    tgb.text("{text}")
    tgb.input("{text}")
    ```


Here is the combined code:

=== "Markdown"
    ```python
    from taipy.gui import Gui

    text = "Original text"

    page = """
    # Getting started with Taipy GUI

    My text: <|{text}|>

    <|{text}|input|>
    """

    Gui(page).run(debug=True)
    ```
=== "Python"
    ```python
    from taipy.gui import Gui
    import taipy.gui.builder as tgb

    text = "Original text"

    with tgb.Page() as page:
        tgb.text("# Getting started with Taipy GUI", mode="md")
        tgb.text("My text: {text}")

        tgb.input("{text}")

    Gui(page).run(debug=True)
    ```

![Visual Elements](images/result.png){ width=90% : .tp-image-border }
