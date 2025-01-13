---
hide:
  - toc
---

Let's start by creating a simple page with 3 components: a selector to select a category of items, 
a bar chart which displays the sales of the top 10 countries for this category and 
a table which displays data for the selected category

[Download the code](https://github.com/Avaiga/taipy-course-gui/blob/develop/2_visual_elements/main.py){: .tp-btn target='blank' }


![Step 1 Application](images/simple_app.png){ width=90% : .tp-image-border }

Let's start by importing the necessary libraries:

=== "Python"
    ```python
    from taipy.gui import Gui
    import taipy.gui.builder as tgb
    import pandas as pd
    ```
=== "Markdown"
    ```python
    from taipy.gui import Gui
    import pandas as pd
    ```

We can now start creating the page. We will first add a [selector](../../../../refmans/gui/viselements/generic/selector.md).

=== "Python"
    ```python
    with tgb.Page() as page:
        tgb.selector(value="{selected_category}", lov="{categories}", on_change=change_category)
    ```
=== "Markdown"
    ```python
    page = """
    <|{selected_category}|selector|lov={categories}|on_change=change_category|>
    """
    ```

Taipy [visual elements](../../../../refmans/gui/viselements/index.md) take many properties. 
Note that dynamic properties use a quote and brackets syntax. We use `value="{selected_category}"` 
to signal to Taipy that `selected_category` should change when the user uses the selector. 
Likewise, if `categories` changes, the selector will get updated with the new values. 

Here, selector needs an associated string variable which will change when a user selects a value, 
a list of values (lov) to choose from, and a callback function to call when the value changes. 
We can define them above:

```python
data = pd.read_csv("data.csv")
selected_category = "Furniture"
categories = list(data["Category"].unique())

def change_category(state):
    # Do nothing for now, we will implement this later
    return None
```

We can now add a chart to display the sales of the top 10 countries for the selected category.

=== "Python"
    ```python
        tgb.chart(
            data="{chart_data}",
            x="State",
            y="Sales",
            type="bar",
            layout="{layout}",
        )
    ```
=== "Markdown"
    ```
    <|{chart_data}|chart|x=State|y=Sales|type=bar|layout={layout}|>
    ```

Taipy charts have many properties. You can create multiple traces, add styling, change the type of chart, etc.

=== "Python"
    ```python
    data = {"x_col": [0, 1, 2], "y_col1": [4, 1, 2], "y_col_2": [3, 1, 2]}
    with tgb.Page() as page:
        tgb.chart("{data}", x="x_col", y__1="y_col1", y__2="y_col_2", type__1="bar", color__2="red")
    ```
=== "Markdown"
    ```python
    data = {"x_col": [0, 1, 2], "y_col_1": [4, 2, 1], "y_col_2":[3, 1, 2]}
    Gui("<|{data}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|type[1]=bar|color[2]=red|>").run()
    ```

    
You can check the syntax for charts [here](../../../../refmans/gui/viselements/generic/chart.md). 

You 
can also directly embed Plotly charts using the `figure` property as we will do in [Step 3](../step_03/step_03.md).

Here we need to provide a Pandas Dataframe with the data to display, the x and y columns to use, the type of chart,
and a layout dictionary with additional properties.

```python
chart_data = (
    data.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

layout = {"yaxis": {"title": "Revenue (USD)"}, "title": "Sales by State"}
```

Lastly, we can add a table to display the data for the selected category.

=== "Python"
    ```python
        tgb.table(data="{data}")
    ```
=== "Markdown"
    ```
    <|{data}|table|>
    ```

We can now run the application using:
  
```python
if __name__ == "__main__":
    Gui(page=page).run(title="Sales", dark_mode=False, debug=True)
```

`debug=True` will display a stack trace of the errors if any occur. 
You can also set `use_reloader=True` to automatically reload the page 
when you save changes to the code and `port=XXXX` to change the server port.

The application runs but has no interaction. We need to code the callback function
to update the chart and table when the user selects a category.

```python
def change_category(state):
    state.data = data[data["Category"] == state.selected_category]
    state.chart_data = (
        state.data.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    state.layout = {
        "yaxis": {"title": "Revenue (USD)"},
        "title": f"Sales by State for {state.selected_category}",
    }
```

## State

Taipy uses a `state` object to store the variables per client.
The syntax to update a variable will always be `state.variable = new_value`.

State holds the value of all the variables used in the user interface for one specific connection.

Modifying `state.data` will update data for one specific user, without modifying `state.data` for other users
or the global `data` variable. You can test this by opening the application in a separate incognito window.