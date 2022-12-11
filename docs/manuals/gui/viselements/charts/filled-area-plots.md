## Filled Area Plots

An area chart displays a solid color between the traces of a graph. It is an option on scatter charts. Areas will be filled according to the ‘fill’ option ("none", "tozeroy", "tozerox" , "tonexty", "tonextx", "toself", and "tonext")

### Simple example
This example shows the number of sold items per day (The shop closes on Weekend :) ).
```py

from taipy.gui import Gui
import pandas as pd
 
options = {"fill":"tonextx"}
 
data = {
  "day": ['Mon', 'Tue','Wed','Thu','Fri'],
  "items": [32, 25, 86, 60, 70],
 }
 
 
md = "<|{data}|chart|x=day|y=items|type=scatter|options={options}|>"
 
Gui(md).run()
```
![Simple example](filled-area.png)

### Basic Overlaid Area Chart
With above example, we want to add one more trace to visualize the total price (x 1000$) per day.

```py

from taipy.gui import Gui
import pandas as pd
 
options = {"fill":"tonextx"}
 
data = {
  "day": ['Mon', 'Tue','Wed','Thu','Fri'],
  "items": [32, 25, 86, 60, 70],
  "prize": [80, 50, 140, 10, 70],
 }
 
 
md = "<|{data}|chart|x=day|y[1]=items|y[2]=prize|type=scatter|options={options}|>"
 
Gui(md).run()
```
![Basic Overlaid Area Chart](filled-area-overlaid.png)

It is not perfect, isn't it. So we have to define 2 types of fill option for "items" and "prize"

```py

from taipy.gui import Gui
import pandas as pd
 
optionsItem = {"fill": "tozeroy"}
optionsPrize = {"fill": "tonexty"}
 
data = {
  "day": ['Mon', 'Tue','Wed','Thu','Fri'],
  "items": [32, 25, 86, 60, 70],
  "prize": [80, 50, 140, 10, 70],
 }
 
 
md = "<|{data}|chart|x=day|y[1]=items|y[2]=prize|type=scatter|options[1]={optionsItem}|options[2]={optionsPrize}|>"
 
Gui(md).run()
```
![Basic Overlaid Area Chart with different options](filled-area-overlaid-2.png)

Great, it is better now, however we don't want to see the lines.
```py
from src.taipy.gui import Gui
import pandas as pd

optionsItem = {"fill": "tozeroy"}
optionsPrize = {"fill": "tonexty"}

mode = "none"

data = {
    "day": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    "items": [32, 25, 86, 60, 70],
    "prize": [80, 50, 140, 10, 70],
}


md = "<|{data}|chart|x=day|y[1]=items|y[2]=prize|type=scatter|mode={mode}|options[1]={optionsItem}|options[2]={optionsPrize}|>"

Gui(md).run()
```
![Basic Overlaid Area Chart without boundary lines](filled-area-overlaid-3.png)

### Stacked Area Chart
A stacked area chart is a variation of an area chart. It visualized the evolution of multiple data series (value of several groups) over time.

This example will show the income (x 1000$) of each products per month.

```py
from src.taipy.gui import Gui
import pandas as pd

options4Milk = {"stackgroup": "one"}
options4Bread = {"stackgroup": "one"}
options4Apples = {"stackgroup": "one"}

mode = "none"

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "milk": [80, 85, 95, 120, 140, 130, 145, 150, 120, 100, 90, 110],
    "bread": [100, 90, 85, 90, 100, 110, 105, 95, 100, 110, 120, 125],
    "apples": [50, 65, 70, 65, 70, 75, 85, 70, 60, 65, 70, 80],
}


md = "<|{data}|chart|x=month|y[1]=milk|y[2]=bread|y[3]=apples|type=scatter|mode={mode}|options[1]={options4Milk}|options[2]={options4Bread}|options[3]={options4Apples}|>"

Gui(md).run()
```
![Stacked Area Chart](filled-area-stacked.png)

### Normalized Stacked Area Chart

A percentage stacked area chart is very close to a classic stacked area chart. However, values are normalised to make in sort that the sum of each group is 100 at each position on the X axis

Now we want to show the ratio of cosmetic products sales between each regions.
```py
from src.taipy.gui import Gui
import pandas as pd

options4USA = {"stackgroup": "one", "groupnorm": "percent"}
options4China = {"stackgroup": "one"}
options4EU = {"stackgroup": "one"}
options4Africa = {"stackgroup": "one"}

data = {
    "region": ["Nail polish", "Eyebrow pencil", "Rouge", "Lipstick", "Eyeshadows", "Eyeliner", "Foundation", "Lip gloss", "Mascara"],
    'usa': [12814, 13012, 11624, 8814, 12998, 12321, 10342, 22998, 11261],
    'china': [3054, 5067, 7004, 9054, 12043, 15067, 10119, 12043, 10419],
    'eu': [4376, 3987, 3574, 4376, 4572, 3417, 5231, 4572, 6134],
    'africa': [4229, 3932, 5221, 9256, 3308, 5432, 13701, 4008, 18712],
}

layout={
    # Show all value of cosmetic products when hovering on a region
    'hovermode': 'x unified',
}

md = "<|{data}|chart|x=region|y[1]=usa|y[2]=china|y[3]=eu|y[4]=africa|type=scatter|options[1]={options4USA}|options[2]={options4China}|options[3]={options4EU}|options[4]={options4Africa}|layout={layout}|>"

Gui(md).run()
```
![Normalized Stacked Area Chart](filled-area-stacked-2.png)