---
title: Data Nodes
category: scenario_management
data-keywords: scenario datanode storage_type configuration
short-description: Understand data nodes and their central role in accessing data from various sources.
order: 13
img: the_data_nodes/images/data_notes.png
---
Taipy is a Python tool for making web applications that use data.
It can do many things, but we're going to talk about
two important things in Taipy: Data nodes and Tasks.

Data nodes are like a bridge to get data from different places.
They help us access data easily. This tip is mostly about data nodes,
what they do, and how we use them in Taipy scenarios.

Data nodes in Taipy are like tools to work with data. They don't hold data themselves,
but they know how to get it from different places.
Think of a data node as something that can read and write data, and it's really good at doing that.

Now, we'll talk about two types of data nodes:

- **Input data nodes**: These are data nodes that help us bring data into our system.

- **Output data nodes**: These are data nodes that help us send data out of our system.

So, data nodes are like helpers for handling data,
and they come in these two varieties: *my_input* and *my_output*.

![data nodes](images/data_notes_2.svg){width=90% : .tp-image }

Taipy has a set of predefined data nodes ready to be used when configuring your data workflow.

Here’s the list of predefined data nodes:

![data nodes](images/data_notes.png){width=90% : .tp-image }

## Pickle Data Node

The [Pickle](../../../userman/scenario_features/data-integration/data-node-config.md#pickle)
data node is the standard data node in Taipy.
It can handle various types of Python stuff like strings, numbers, lists, dictionaries,
models (for machine learning or other things), and data tables. Here's some code that uses
two Pickle data nodes: one for getting data in and one for sending data out.

- *model* is an input *Pickle* data node. It looks at a Pickle file called *model.p* and gets
    data from there.

- *predictions* is an output data node, but right now, it doesn't have any data in it.
  We haven't told it where to get data from yet.

<video width="640" height="360" controls class="tp-video">
  <source src="images/pickle-data-node.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

The Python configuration translates as the code below:

```py
from taipy.common.config import Config

model_cfg = Config.configure_data_node("model", default_path="model.p")
predictions_cfg = Config.configure_data_node("predictions")
task_cfg = Config.configure_task("task", predict, model_cfg, predictions_cfg)

scenario_cfg = Config.configure_scenario("my_scenario", [task_cfg])
```

Once you've set up this basic graph, the next step is to create a scenario using it and then
submit it for execution.

```python
scenario = tp.create_scenario(scenario_cfg)
tp.submit(scenario)
```
When submitting the scenario (for execution), Taipy:

- retrieves and reads the model,
- executes the *predict()* function,
- and writes the results in a Pickle file.

Taipy makes things easy by handling the paths for Pickle files automatically if you haven't
defined them. This simplifies the configuration process. When you create several scenarios,
the output data nodes from each scenario will automatically point to separate files.

```python
scenario_2 = tp.create_scenario(scenario_cfg)
tp.submit(scenario_2)
```

In this example, when we create a second scenario from the same main script, it also brings in
a new pair of data nodes: *model* and *predictions*. The *model* data node still points to the
same Pickle file because its path was set by the developer in advance. However, the new *predictions*
data node points to a different Pickle file. Taipy creates this new Pickle file on the fly during
runtime, so it's separate from the one used in the first scenario. All data nodes that writes in
the local system share this behavior.

## Tabular data nodes

Tabular data nodes in Taipy are a collection of data nodes designed for handling tabular data.
By default, the data they point to is presented to the user or developer as a Pandas DataFrame.

The predefined tabular data nodes in Taipy include:

- [SQL](../../../userman/scenario_features/data-integration/data-node-config.md#sql)
- [CSV](../../../userman/scenario_features/data-integration/data-node-config.md#csv)
- [Excel](../../../userman/scenario_features/data-integration/data-node-config.md#excel)
- [Parquet](../../../userman/scenario_features/data-integration/data-node-config.md#parquet)

These data nodes allow you to work with tabular data from different sources with ease.

<video width="640" height="360" controls class="tp-video">
  <source src="images/tabular-data-nodes.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

To use Tabular data nodes in Taipy, you only need to include them in the configuration
and specify certain parameters, like a default path for CSV or Parquet files. It's important to
note that you can change this path during runtime. For instance, if you create a new scenario,
you can instruct the Tabular data nodes to save the results in a different file or directory,
thereby preventing the overwriting of previous data. Taipy can also manage file destinations in cases where no 'default_path' has been specified.

```python
scenario = tp.create_scenario(scenario_cfg)
tp.submit(scenario)
```

When you submit the scenario described above for execution in Taipy, the following steps occur:

- Taipy reads the CSV file named `data.csv` because it is the input data node.

- It takes the data from the CSV file and passes it to the *some_preprocessing()* function
    using the chosen exposed type, which is typically a Pandas DataFrame by default.

- After the processing is done, Taipy writes or overwrites the result,
    which is typically in the form of a Pandas DataFrame, into the Parquet file located at
    *data.parquet*.

- This Parquet file may overwrite any existing data in that file if it already exists.

Here, we'll demonstrate how you can change the exposed type from the default Pandas DataFrame
to other types, such as *Numpy arrays*:

<video width="640" height="360" controls class="tp-video">
  <source src="images/tabular-data-nodes_2.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Generic data nodes

The **Generic** data node in Taipy is a flexible option that users can customize to include
their own *read()* and *write()* functions. This feature is particularly useful when dealing
with data sources that don't have a predefined Taipy Data node. With a Generic data node, you
can tailor it to access data in specific formats or from custom sources.

For more detailed information and guidance on using the Generic data node and customizing it to
your specific needs, check the
[Taipy documentation](../../../userman/scenario_features/data-integration/data-node-config.md#generic). It will
provide you with step-by-step instructions and examples.

Taipy integrates two other predefined storage types to work with documents. Check the
documentation for more details.

- [Mongo](../../../userman/scenario_features/data-integration/data-node-config.md#mongo-collection)
- [Json](../../../userman/scenario_features/data-integration/data-node-config.md#json)

## Conclusion

As mentioned before, data nodes serve as references to data sources,
and they hide the complexities of how data is stored and fetched.
This simplifies the process of working with data within a complete web application.

Furthermore, Taipy's capability to model data nodes enables it to eliminate redundant tasks.
Taipy can recognize situations where inputs have remained unchanged between two runs,
resulting in the same outputs. As a result, it becomes unnecessary to re-execute the task.
This *skippability* feature enhances the efficiency of data processing,
ultimately saving users valuable time and resources.
