> You can download the code for
<a href="./../src/step_06.py" download>Step 6</a> 
or all the steps <a href="./../src/src.zip" download>here</a>. 

!!! warning "For Notebooks"

    The Notebook is available [here](../getting_started.ipynb). In Taipy GUI, the process to 
    execute a Jupyter Notebook is different from executing a Python Script.
    It is important to check the [Notebook](../getting_started.ipynb) 
    content and see the [documentation](../../../../manuals/gui/notebooks.md).


# Step 6: Page layout

You've successfully built a comprehensive forecasting application capable of making predictions 
for multiple days with various parameters in just a few steps. Nevertheless, there is room for 
substantial improvement in the page's layout. We'll introduce three new helpful controls to 
enhance the page's visual appeal. These controls are:

- [part](../../../../manuals/gui/viselements/part.md): creates a group of text/visual elements. 
    A useful property of `part` is _render_. If set to False, it will not display the part. This 
    allows the developer to hide a group of visual elements dynamically.

    ```
    <|part|render={bool_variable}|
    Text
    Or visual elements...
    |>
    ```

- [layout](../../../../manuals/gui/viselements/layout.md): creates invisible columns where you 
    can put your texts and visual elements. The _columns_ property indicates the width and number 
    of columns. Here, we create three columns of the same width.

    ```
    <|layout|columns=1 1 1|
    Button in first column <|Press|button|>
    
    Second column
    
    Third column
    |>
    ```
    
    ![Layout](layout.png){ width=500 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }


- [expandable](../../../../manuals/gui/viselements/expandable.md): creates a block that can 
    expand or shrink.

    ![expandable](expandable.png){ width=500 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }


## Back to the code

```python

page = """
<|toggle|theme|>

# Getting started with Taipy GUI

<|layout|columns=1 1|
<|
My text: <|{text}|>

Enter a word:
<|{text}|input|>
<|Analyze|button|on_action=local_callback|>
|>


<|Table|expandable|
<|{dataframe}|table|width=100%|>
|>
|>

<|layout|columns=1 1 1|
## Positive <|{np.mean(dataframe['Score Pos'])}|text|format=%.2f|raw|>

## Neutral <|{np.mean(dataframe['Score Neu'])}|text|format=%.2f|raw|>

## Negative <|{np.mean(dataframe['Score Neg'])}|text|format=%.2f|raw|>
|>

<|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|>
"""
```

![Layout](result.png){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }

