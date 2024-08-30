This page describes how to manage *sequences* in Taipy. It explains how to create,
submit and use *sequences*.

A `Sequence^` in Taipy is an attribute of a scenario. It is a submittable entity
that represents a subset of scenario tasks that can be executed together,
independently of the other scenario's tasks.

The *sequences* can be created directly on scenario instances, at run time, but they
can also be describes in the scenario configurations, so they are created along with the
scenario creation.

# Sequence creation

A sequence can be created directly on a scenario instance using the `Scenario.add_sequence()^`
method.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to demonstrate how to create a sequence on a scenario.

    ```python linenums="1"
    {%  include-markdown "./code-example/create.py" comments=false %}
    ```

Sequences can also be created along with the scenario creation by providing the sequences
description in the scenario configuration. For more details, see the
[scenario configuration](../scenario/scenario-config.md#adding-sequence-descriptions)
page.

# Graphical User Interface

Taipy offers visual elements dedicated to scenario management. These elements are designed
to help end-users select, visualize, and edit scenarios in an intuitive way.

In particular, the scenario visual element is designed to help end-users create, submit, and
delete scenarios' sequences.

For more details and examples, see the
[scenario visual elements](../../task-orchestration/vizelmts.md#scenario-viewer) section.

# Sequence attributes

A `Sequence^` is identified by a unique identifier `id` that Taipy generates.
It also holds various properties accessible as an attribute of the sequence:

- _**subscribers**_: The list of Tuples (callback, params) representing the subscribers.
- _**properties**_: The complete dictionary of the sequence properties. It includes a copy
    of the properties of the sequence configuration, in addition to the properties provided
    at the creation and runtime.
- _**tasks**_: The dictionary holds the sequence's various tasks. The key corresponds to
    the *config_id* of the task while the value is the task itself.
- _**data_nodes**_: The dictionary holding the various data nodes of the sequence. The key
    corresponds to the data node's *config_id* (while the value is the data node itself).
- _**owner_id**_: The identifier of the owner, which can be a scenario, cycle, or None.
- _**version**_: The string indicates the application version of the sequence to instantiate.
    If not provided, the current version is used. For more details, refer to
    [version management](../../../advanced_features/versioning/index.md).
- Each property of the _**properties**_ dictionary is also directly exposed as an attribute.
- Each nested entity is also exposed as an attribute of the sequence. The attribute name
    corresponds to the *config_id* of the nested entity.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to show the various attributes of a sequence.

    ```python linenums="1"
    {%  include-markdown "./code-example/attributes.py" comments=false %}
    ```

# Get Sequences

## Get by id

The first method to get a sequence is from its id by using the `taipy.get()^` method:

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to show how to get a sequence from its id.

    ```python linenums="1"
    {%  include-markdown "./code-example/get-by-id.py" comments=false %}
    ```

    Here, `sequence_retrieved` equals `sequence`.

## Get from parents

All sequences that are part of a scenario can be directly accessed as attributes:

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to show how to get a sequence from its parent scenario.

    ```python linenums="1"
    {%  include-markdown "./code-example/get-from-parent.py" comments=false %}
    ```

## Get all sequences

All the existing sequences can be retrieved using the method `taipy.get_sequences()^`.
This method returns the list of all existing sequences for all scenarios.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to show how to retrieve all sequences.

    ```python linenums="1"
    {%  include-markdown "./code-example/get-all-sequences.py" comments=false %}
    ```

# Delete a sequence

A sequence can be deleted by using `taipy.delete()^` which takes the sequence id as
a parameter. The deletion is also propagated to the nested tasks, data nodes, and
jobs if they are not shared with any other sequence.

# Get parent scenarios

To get the parent entities of a sequence (i.e., scenarios) you can use either the
method `Sequence.get_parents()^` or the static function `taipy.get_parents()^`. Both
return the parents of the sequence.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to show how to get the parent scenarios of a sequence.

    ```python linenums="1"
    {%  include-markdown "./code-example/get-parent-scenarios.py" comments=false %}
    ```
