## Heatmap charts

A heatmap depicts values for a main variable of interest across two axis variables as a grid of colored squares. The axis variables are divided into ranges like a bar chart or histogram, and each cell’s color indicates the value of the main variable in the corresponding cell range.

### When to Use?
- To show user behavior on specific webpages.
- To display the magnitude of a data set over two dimensions.
- In retail matrix, manufacturing diagram, and population maps.
- For marketing goals and analytics, reflecting on user behavior on specific webpages.
- And more

### Basic Heatmap
The chart below shows the colors in accordance with each temperatures

```py
from taipy.gui import Gui

data = {
    "temperature": [[1, 20, 30], [20, 1, 60], [30, 60, 1]],
}
options = {'colorscale': 'Reds'}
md = """
## Basic Heatmap
<|{data}|chart|z=temperature|type=heatmap|options={options}|>
"""

Gui(md).run()
```
![Basic Heatmap](heatmap_basic.png)

### Heatmap with Categorical Axis Labels
In the following example, we have an array which defines the data (harvest by different farmers in tons/year) to color code. We then also need two lists of names of farmers and vegetables cultivated by them.
```py
from taipy.gui import Gui
import pandas as pd

data = [
    pd.DataFrame({
        'harvest': [
            [0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
            [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
            [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
            [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
            [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
            [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
            [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]
        ],
        'vegetables': ["cucumber",
                       "tomato",
                       "lettuce",
                       "asparagus",
                       "potato",
                       "wheat",
                       "barley"]
    }),
    pd.DataFrame({
        'farmers': ["Farmer Joe",
                    "Upland Bros.",
                    "Smith Gardening",
                    "Agrifun",
                    "Organiculture",
                    "BioGoods Ltd.",
                    "Cornylee Corp."],
    })
]
options = {'colorscale': 'Rainbow'}
md = """
## Heatmap with Categorical Axis Labels
<|{data}|chart|type=heatmap|z=0/harvest|x=1/farmers|y=0/vegetables|options={options}|>
"""

Gui(md).run()
```
![Heatmap with Categorical Axis Labels](heatmap_axis_labels.png)

### Annotated Heatmap
In this chart, we have average temperature (°F) in seasons of top 4 US cities
```py
from taipy.gui import Gui
import pandas as pd

seasons = ['Winter', 'Summer', 'Spring', 'Autumn']

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']

temperature = [
    [33.7, 74.49, 57.8, 57.6],
    [60.1, 68.2, 64.5, 65.7],
    [22.89, 72.2, 55.7, 51.6],
    [53.0, 83.3, 72.7, 53.0],
]

data = [
    pd.DataFrame({
        'temperature': temperature,
        'cities': cities
    }),
    pd.DataFrame({
        'seasons': seasons,
    })
]

options = {'colorscale': 'Portland'}

layout = {
    'annotations': [],
    'xaxis': {
        'ticks': '',
        'side': 'top'
    },
    'yaxis': {
        'ticks': '',
        'ticksuffix': ' ',
        'width': 700,
        'height': 700,
        'autosize': False
    }
}

for i in range(len(cities)):
  for j in range(len(seasons)):
    currentValue = temperature[i][j]
    if (currentValue < 40 or currentValue > 70):
        textColor = 'white'
    else:
        textColor = 'black'
    result = {
        'xref': 'x1',
        'yref': 'y1',
        'x': seasons[j],
        'y': cities[i],
        'text': str(temperature[i][j]) + '°F',
        'font': {
            'family': 'Arial',
            'size': 12,
            'color': textColor
        },
        'showarrow': False
    }
    layout['annotations'].append(result)

md = """
## Annotated Heatmap
<|{data}|chart|type=heatmap|z=0/temperature|x=1/seasons|y=0/cities|options={options}|layout={layout}|>
"""

Gui(md).run()
```
![Annotated Heatmap](heatmap_annotated.png)

### Heatmap with Unequal Block Sizes

```py
from taipy.gui import Gui
import numpy as np
import pandas as pd

# Data for the heatmap
phi = (1 + np.sqrt(5)) / 2.  # golden ratio
xe = [0, 1, 1 + (1 / (phi**4)), 1 + (1 / (phi**3)), phi]
ye = [0, 1 / (phi**3), 1 / phi**3 + 1 / phi**4, 1 / (phi**2), 1]

z = [
        [13, 3, 3, 5 ],
        [13, 2, 1, 5],
        [13, 10, 11, 12],
        [13, 8, 8, 8]
     ]

# Data for the spiral
def spiral(th):
    a = 1.120529
    b = 0.306349
    r = a * np.exp(-b * th)
    return (r * np.cos(th), r * np.sin(th))

theta = np.linspace(-np.pi / 13, 4 * np.pi, 1000)  # angle
(x, y) = spiral(theta)

data = [
    pd.DataFrame({
        'zHeatmap': z,
    }),
    pd.DataFrame({
        'xHeatmap': np.sort(xe),
        'yHeatmap': np.sort(ye)
    }),
    pd.DataFrame({
        'xTrace': -x + x[0],
        'yTrace': y - y[0],
    })
]

axisTemplate = {
    'range': [0, 1.6],
    'autorange': False,
    'showgrid': False,
    'zeroline': False,
    'linecolor': 'black',
    'showticklabels': False,
    'ticks': ''
}

layout = {
    'title': 'Heatmap with Unequal Block Sizes',
    'xaxis': axisTemplate,
    'yaxis': axisTemplate,
    'showlegend': False,
    'with': 700,
    'height': 700,
    'autosize': False
}

# Everything with index [1] is for heatmap
# Everything with index [2] is for scatter
md = """
## Annotated Heatmap
<|{data}|chart|type[1]=heatmap|z[1]=0/zHeatmap|x[1]=1/xHeatmap|y[1]=1/yHeatmap|layout={layout}|type[2]=scatter|x[2]=2/xTrace|y[2]=2/yTrace|>
"""

Gui(md).run()
```
![Heatmap with Unequal Block Sizes](heatmap_unequal_block_sizes.png)
