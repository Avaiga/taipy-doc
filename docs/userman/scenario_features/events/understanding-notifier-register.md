Taipy exposes the `Notifier.register()^` method to register to events. The registration
result is passed to a consumer that processes the events. When you register,
you specify parameters that define the events you want to process. These parameters and the
registration mechanism allows you to tailor your event consumer to your application's precise
needs. For example, you can register to:

- All events emitted
- All operations related to scenarios
- All operations related to a specific data node
- All job creations
- A specific data node update
- A sequence submission
- A scenario deletion
- Job failures

To register for event notifications, use the `Notifier.register()` method. The following
parameters define the events you want to process, like a topic of interest:

1. `entity_type`
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

2. `entity_id`
    - **Type**: `str`
    - **Description**: Identifies the specific entity instance to register for. If omitted,
        the consumer will be called of events for all entities of the specified `entity_type`.

3. `operation`
    - **Type**: `EventOperation^` (Enum)
    - **Description**: Specifies the type of operation to monitor (e.g., `CREATION`, `UPDATE`,
        `DELETION`, `SUBMISSION`). If omitted, the consumer will be called for all operations
        performed on the specified `entity_type`.

4. `attribute_name`
    - **Type**: `str`
    - **Description**: Targets a specific attribute within an entity. This is
        particularly useful when you are interested in changes to a particular attribute,
        such as when an attribute's value is updated. If omitted, the consumer will be called
        for changes to all attributes.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/register-specific-topic-to-notifier.py"
    comments=false
     %}
    ```

To see complete and realistic examples, see the [examples](examples.md) page.
