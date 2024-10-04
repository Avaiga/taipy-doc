Among other functionalities, a data node keep track of the data editing history and
the period of validity.

# What is an Edit?
Every time a data is written using the data node methods, a new `Edit` entry is
added on the head of the list of edits. An `Edit` corresponds to a data modification.
It contains the timestamp of the modification, and some other information such as the
job id in case the edit is done by a job, or the editor in case the edit is done
manually.

In the following example, we create a simple data node and write some data three times
using various Taipy methods. We then print the list of edits to see the history of the
data node modifications.

```python
{%
include-markdown "./code-example/data-node-history/data-node-history-example.py"
comments=false
%}
```

!!! note
    As shown in the previous code, one way to write a data node is to execute a task
    that has the data node as output. If you are not yet familiar with the concepts of
    task or Scenario, you can refer to the
    [task orchestration](../task-orchestration/index.md) section.

## Retrieve Edits

Two methods are available to retrieve the edits from a data node:

- `DataNode.edits^` property returns the sorted list of edits.
    ```python
    edits = data_node.edits
    # [{'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 652773), 'editor': 'TAIPY', 'comment': 'Default data written.'},
    # {'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 689737), 'editor': 'John', 'comment': 'Manual edition: 100', 'extra': 'extra data'},
    # {'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 856928), 'job_id': 'JOB_random_task_a8031d80-26f7-406e-9b31-33561d0f9ccd'}]
    ```
- `DataNode.get_last_edit()^` returns the last edit of the data node.
    ```python
    last_edit = data_node.get_last_edit()
    # {'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 856928), 'job_id': 'JOB_random_task_a8031d80-26f7-406e-9b31-33561d0f9ccd'}]
    ```

## Manual writing

When writing data using the data node methods `DataNode.write()^` or `DataNode.append()^`,
an edit is automatically created and added to the list of edits. Extra information can be
added to the edit by passing any parameter to the methods.

```python
data_node.write(100)
```
Simply calling the write method results in adding an edit the timestamp in it as follows.
```console
{'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 652773)}
```
The append method can also be used for tabular data nodes, resulting in the same edit content.

To add extra information to the edit, you can pass any parameter to the write method.
```python
data_node.write(100, editor="John", comment="Manual edition: 100", extra="extra data")
```
The previous code results in adding an edit with the following content:
```console
{'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 689737), 'editor': 'John', 'comment': 'Manual edition: 100', 'extra': 'extra data'}
```
The append method can also be used for tabular data nodes with any parameter,
resulting in the same edit content.

## Writing from a GUI
Using the [data node viewer](../../../refmans/gui/viselements/corelements/data_node.md) to write
data, an end user can easily add a comment to the edit. The edits can be viewed in
the history tab of the data node viewer.

![The history tab of a data node viewer](img/data-node-history/data-node-history-example.png){ align=center }

## Writing by a Job execution

Another way to write a data node is to execute a task that has the data node as
output. If you are not yet familiar with the concepts of job, task or scenario,
you can refer to the [task orchestration](../task-orchestration/index.md) section.

When a data node is written by a job execution, the job id is automatically added
to the edit. Executing a Job results in adding an edit to the output data nodes
with the following content:
```console
{'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 856928), 'job_id': 'JOB_random_task_a8031d80-26f7-406e-9b31-33561d0f9ccd'}
```

## Writing by a 3rd party

When the data is written by an external system (external software, script, cron, etc.),
Taipy does not automatically add an edit. For that use case, one can manually add
an edit once the data modification is done. This can be done by calling the
`DataNode.track_edit()^` method passing any useful parameter to track the modification.

```python
data_node.track_edit(comment="From external system")
```
```console
{'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 856928), 'comment': 'From external system'}
```

# Validity period

In addition to the history of edits, a data node can also keep track of the validity
period. The validity period is a time interval during which the data is considered valid.
It is useful to monitor the data validity and to ensure that the data is not used after
an expiration date.

## Set the validity period

1. From the `DataNodeConfig^`:
    The validity period can be set when configuring a data node as follows:
    ```python
    from datetime import timedelta
    from taipy.common.config import Config
    import taipy as tp

    dataset_cfg = Config.configure_data_node("dataset", validity_period=timedelta(days=7))
    dataset = tp.create_global_data_node(dataset_cfg)
    ```
    In the previous code, the validity period is set to 7 days. Each data node instantiated
    from the "dataset" configuration will be invalidated 7 days after their last edit.

2. From the `DataNode^`:
    The validity period can also be set directly on an existing data node as follows:
    ```python
    dataset.validity_period = timedelta(days=1)
    ```
    The previous code sets the validity period of the dataset data node to 1 day, so it
    will be invalidated 1 day after its last edit.

## Check validity or expiration date

The validity of a data node can be checked using the `DataNode.is_valid^` property returning
a Boolean value.

The expiration date is also available using the `DataNode.expiration_date^` property
returning a `datetime` object.
