## Incorporate Third-Party Components

In the world of web development, it's often necessary to integrate third-party 
components into your applications. These components could be anything from interactive 
visualizations to videos or other web pages. This article will demonstrate how to 
effectively include these external resources in your web app.

## Example: Embedding a Sankey Diagram

![Sankey Diagram](sankey_diagram.png){width=100%}

Let's explore a practical example of how to integrate a Sankey Diagram into a web 
application. A Sankey Diagram is a visualization tool used to represent the flow of 
resources or information between multiple entities. It finds applications in energy 
studies, cost analysis, and network analysis.

In our scenario, we have a Python application that processes recruitment data, performs 
analysis, and generates a Sankey Diagram using Plotly, a Python library for interactive 
visualizations.

Here's a code snippet creating a Plotly object:

```python
def sankey_graph(df):
    # Processing the data for a Sankey Diagram
    ...

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            label=unique_stages2, 
        ),
        link=dict(
            source=sankey_pairs['source'],
            target=sankey_pairs['target'],
            value=sankey_pairs['count'],
        )
    )])

    fig.update_layout(
        title='Sequences per application',
        font=dict(size=12),
    )

    return fig
```

## Incorporating the Sankey Diagram

To integrate this `fig` object in our web appliation, the HTML version of this object 
has to be created.

```python
import io

def expose_plotly(fig):
    buffer = io.StringIO()
    fig.write_html(buffer)
    return buffer.getvalue()
```

In this code, the function `expose_plotly` is responsible for taking a Plotly `fig` 
object as an input and converting it into HTML. This conversion is a crucial step in the 
process of integrating the Sankey Diagram into your application.

The `fig` object is transformed into HTML, and then we proceed to define two callback 
functions, namely, `on_user_content` and `on_init`. The `on_init` callback serves as a 
fundamental Taipy callback that is triggered when a new user accesses the application. 
On the other hand, the `on_user_content` function is designed to return the HTML content 
to be rendered, while the `get_user_content_url` function is utilized to obtain the URL 
for rendering the HTML content.

```python
html = expose_plotly(sankey_graph(data))
uc_url = None

def on_user_content(state, path: str, query: dict):
    return state.html

def on_init(state):
    state.uc_url = get_user_content_url(state, "val", {"name": "param"})
```

Finally, we can embed the Sankey Diagram within our web application using the 
following `part` component:

```
<|part|page={uc_url}|height=800px|>
```

This element seamlessly integrates the Sankey Diagram into your web app, providing an 
engaging user experience.

## Conclusion

Incorporating third-party components into your web applications is a powerful technique 
that can greatly enhance user engagement. You can achieve this by converting external 
content into HTML and seamlessly integrating it into your web app as a URL.

This article demonstrated how to embed a Sankey Diagram in your web application using 
this method. This approach ensures that the integrated content doesn't interfere with 
your page and provides a secure user experience.

# Entire Code

```python
# Plotly code to create "fig"
import plotly.graph_objects as go
import urllib.request, json


url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())


# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]


fig = go.Figure(data=[go.Sankey(
    # Define nodes
    node = dict(
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
))])


fig.update_layout(title_text="Energy forecast for 2050")


# Taipy Code
from taipy.gui import Gui, get_user_content_url, notify
import io


def expose_plotly(fig):
    buffer = io.StringIO()
    fig.write_html(buffer)
    return buffer.getvalue()


def on_user_content(state, path: str, query: dict):
    return state.html


def on_init(state):
    state.uc_url = get_user_content_url(state, "hello", {"t": "a"})


html = expose_plotly(fig)
uc_url = None


example = "<|part|page={uc_url}|height=800px|>"


Gui(example).run()
```