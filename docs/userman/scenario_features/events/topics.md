Taipy exposes an `EventProcessor^` service to simplify the processing of events
emitted by Taipy. The main principle is to register a callback to be executed
when an event matching a specified topic is emitted.

When you register, you specify topic parameters that define the events you want to process.
These parameters allow you to tailor the event processing to your application's precise
needs. For example, you can register to:

- All events emitted
- All operations related to scenarios
- All operations related to a specific data node
- All job creations
- A specific data node update
- A sequence submission
- A scenario deletion
- Job failures
- etc.

# Topic parameters

To register for event notifications, use the `EventProcessor.on_event()^` or
`EventProcessor.broadcast_on_event()^` methods. The input parameters define
the events you want to process, like a topic of interest.

## 1. *entity_type*

- **Type**: `EventEntityType^` (Enum)
- **Description**: Specifies the entity type for which you want to receive notifications.
    If omitted, the consumer will be called for events across all entity types. The
    possible entity types are:

    - `CYCLE`
    - `SCENARIO`
    - `SEQUENCE`
    - `TASK`
    - `DATA_NODE`
    - `JOB`
    - `SUBMISSION`

## 2. *entity_id*

- **Type**: `str`
- **Description**: Identifies the specific entity instance to register for. If omitted,
        the consumer will be called of events for all entities of the specified *entity_type*.

## 3. *operation*

- **Type**: `EventOperation^` (Enum)
- **Description**: Specifies the type of operation to monitor (e.g., `CREATION`, `UPDATE`,
    `DELETION`, `SUBMISSION`). If omitted, the consumer will be called for all operations
    performed on the specified *entity_type*.

## 4. *attribute_name*

- **Type**: `str`
- **Description**: Targets a specific attribute within an entity. This is
    particularly useful when you are interested in changes to a particular attribute,
    such as when an attribute's value is updated. If omitted, the consumer will be called
    for changes to all attributes.

# Usage and examples

Taipy exposes several methods to register callbacks to predefined topics. You can get
the list of available methods in the `EventProcessor^` class documentation.

## Predefined topics

!!! example "Predefined topics"

    ```python linenums="1"
    {%
    include-markdown "./code-example/register-to-predefined-topic.py"
    comments=false
     %}
    ```

    This snippet shows an example of how to register callbacks to predefined topics.

    In line 22, the *store_latest_scenario* callback is registered to a predefined topic
    using the `EventProcessor.broadcast_on_scenario_created()^` method. This method is a
    shortcut for registering to `SCENARIO` entity types with the `CREATION` operation.

    Please refer to the `EventProcessor^` class documentation for the complete list of
    shortcuts.

## Custom topics

To register a callback for a specific custom topic, you can use the standard
`EventProcessor.on_event()^` or `EventProcessor.broadcast_on_event()^` methods
passing the topic parameters as arguments.

!!! example "Register to custom topics"

    ```python linenums="1"
    {%
    include-markdown "./code-example/register-to-specific-topic.py"
    comments=false
     %}
    ```

    In line 23 the *on_entity_creation* callback (defined in line 8) is registered using
    the `EventProcessor.on_event()^` method. The `CREATION` operation is passed as
    an argument so that the callback is only triggered for entity creations (any kind of
    entity).

    In line 24, the *on_scenario* callback (defined in line 11) is also registered.
    It is registered to be triggered only for scenario by passing the `EventEntityType^`
    to `SCENARIO`.

In addition to the *operation* or the *entity_type* parameters, as shown in the
previous example, you can also describe the topics an *attribute_name* or an *entity_id*.
The various combinations of parameters allow you to create very tailored topics to which
you can register callbacks.

For example, you can register to any updates on the path attribute of a given data node
by passing the following parameters:

- `entity_type=EventEntityType.DATA_NODE`,
- `entity_id="my_unique_id"`,
- `operation=EventOperation.UPDATE`,
- `attribute_name="path"`.

## Advanced topics

Combining with the topic parameters, you can also use the *filter* parameter.
It accepts a boolean function that takes an `Event^` object as input and returns
*True* or *False*. If the function returns *True*, the callback will be executed.
This allows you to filter events based on advanced logic.

!!! example "Advanced topic registration"

    ```python linenums="1"
    {%
    include-markdown "./code-example/register-to-advanced-topic.py"
    comments=false
     %}
    ```

    Combined with the topic parameters provided (`SCENARIO` *entity_type* and
    `CREATION` *operation*), the *cycle_filter* boolean function checks if the
    processed `Event^` corresponds to a scenario creation on a past cycle.
    If so, the callback is executed and prints a message to the console.
