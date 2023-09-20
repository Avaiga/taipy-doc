> You can download the full code [here](https://github.com/Avaiga/taipy-getting-started/tree/develop/src).

# Data Visualization Page

This is a guide to create a Data Visualization page for our example. The page contains interactive visual elements to display data from a CSV file.

![Interactive GUI](result.gif){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }"

## Importing the Dataset

To import the dataset, use the following Python code:

```python
import pandas as pd

def get_data(path_to_csv: str):
    dataset = pd.read_csv(path_to_csv)
    dataset["Date"] = pd.to_datetime(dataset["Date"])
    return dataset

path_to_csv = "dataset.csv"
dataset = get_data(path_to_csv)
```

## Visual Elements

Taipy GUI introduces the concept of *Visual elements*, which are graphical objects displayed on the client. You can use various visual elements such as [slider](https://docs.taipy.io/en/latest/manuals/gui/viselements/slider/), a 
[chart](https://docs.taipy.io/en/latest/manuals/gui/viselements/chart/), a 
[table](https://docs.taipy.io/en/latest/manuals/gui/viselements/table/), an 
[input](https://docs.taipy.io/en/latest/manuals/gui/viselements/input/), a 
[menu](https://docs.taipy.io/en/latest/manuals/gui/viselements/menu/), etc. Check the list 
[here](https://docs.taipy.io/en/latest/manuals/gui/viselements/controls/). The syntax for adding a visual element is as follows:

```markdown
<|{variable}|visual_element_name|param_1=param_1|param_2=param_2| ... |>
```

For example, to add a [slider](https://docs.taipy.io/en/latest/manuals/gui/viselements/slider/) that modifies the value of the variable *n_week*, use the following syntax:

```markdown
<|{n_week}|slider|min=1|max=52|>
```

To display a chart with the dataset's content, use the following syntax:

```markdown
<|{dataset}|chart|type=bar|x=Date|y=Value|>
```

## Interactive GUI

The Data Visualization page contains the following visual elements:

- A slider connected to the Python variable *n_week*.
- A chart representing the DataFrame content.

## Multi-client - state

Taipy maintains a separate state for each client connection. The state holds the values of all variables used in the user interface. For example, modifying *n_week* through a slider will update *state.n_week*, not the global Python variable *n_week*. Each client has its own state, ensuring that changes made by one client don't affect others.

## [Callbacks](https://docs.taipy.io/en/latest/manuals/gui/callbacks/)

In each visual elements, callbacks can be placed. This will only you to update variables depending on user action. (See local callback and global callback)

- state: The state object containing all the variables.
- The name of the modified variable. (optional)
- Its new value. (optional)

Here's an example of *on_change()* function to update *state.dataset_week* based on the selected week from the slider:

```markdown
<|{n_week}|slider|min=1|max=52|on_change=on_slider|>
```

```python
def on_slider(state):
    state.dataset_week = dataset[dataset["Date"].dt.isocalendar().week == state.n_week]
```

## Markdown (pages/data_viz/data_viz.md)

Here is the entire Markdown of the first page.

```markdown
# Data Visualization page

Select week: *<|{n_week}|>*

<|{n_week}|slider|min=1|max=52|on_change=on_slider|>

<|{dataset_week}|chart|type=bar|x=Date|y=Value|>
```

## Python code (pages/data_viz/data_viz.py)

You can find below the associated code with the Markdown that will populate the objects of the page and create the interaction between the slider and the chart.

```python
from taipy.gui import Markdown
import pandas as pd

def get_data(path_to_csv: str):
    # pandas.read_csv() returns a pd.DataFrame
    dataset = pd.read_csv(path_to_csv)
    dataset["Date"] = pd.to_datetime(dataset["Date"])
    return dataset

# Read the dataframe
path_to_csv = "data/dataset.csv"
dataset = get_data(path_to_csv)

# Initial value
n_week = 10

# Select the week based on the slider value
dataset_week = dataset[dataset["Date"].dt.isocalendar().week == n_week]

def on_slider(state):
    state.dataset_week = dataset[dataset["Date"].dt.isocalendar().week == state.n_week]


data_viz = Markdown("pages/data_viz/data_viz.md")
```

With this configuration, you can create an interactive Data Visualization page using Taipy. The page will display the dataset based on the selected week from the slider.

## Connection to the entire application

Don't forget to add the page to the application in the *main.py*:

Import `data_viz` to the main file.

```python
...

pages = {
    "/": root_page,
    "data_viz": data_viz # add Data Visualization page
}

...
```