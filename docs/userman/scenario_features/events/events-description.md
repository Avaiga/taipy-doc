The `Event^` object in Taipy is a notification mechanism for any changes occurring within Taipy Core,
particularly those related to the Scenario and Data Management. It is a crucial part of the system that allows
tracking and responding to changes in the state of various entities managed by Taipy, such as data nodes, jobs,
and scenarios.

An `Event^` object is composed of several key attributes that describe what happened, the
type of operation performed, the entity concerned and its type, and other contextual
details.

1. `entity_type`
    - **Type**: `EventEntityType^` (Enum)
    - **Description**: Specifies the type of entity that has undergone a change. This
        attribute helps identify the nature of the object affected. The possible entity
        types are:

        - `CYCLE`
        - `SCENARIO`
        - `SEQUENCE`
        - `TASK`
        - `DATA_NODE`
        - `JOB`
        - `SUBMISSION`

2. `operation`
    - **Type**: `EventOperation^` (Enum)
    - **Description**: Indicates the type of operation performed. The `operation` attribute
        is essential for understanding the nature of the change. The possible operations are:

        - `CREATION` - An entity has been created.
        - `UPDATE` - An entity has been updated.
        - `DELETION` - An entity has been deleted.
        - `SUBMISSION` - An entity has been submitted for processing.

3. `entity_id`
    - **Type**: `str`
    - **Description**: The unique identifier for the entity that has been changed. This
        ID allows you to precisely identify which object in the system the event refers to.

4. `attribute_name`
    - **Type**: `str`
    - **Description**: The name of the specific attribute that has been changed within
        the entity. This attribute is only relevant for `UPDATE` operations, where
        a specific field of an entity has been modified.

5. `attribute_value`
    - **Type**: `Any`
    - **Description**: The new value of the changed attribute. Like `attribute_name`, this
        only applies to `UPDATE` operations.

6. `metadata`
    - **Type**: `dict`
    - **Description**: A dictionary containing additional metadata about the source of the
        event. This can include context-specific information that provides more insight into
        the event's origin or purpose.

7. `creation_date`
    - **Type**: `datetime`
    - **Description**: The exact date and time the event was created.

!!! example "Scenario creation event"

    For example, when a scenario is created, an event is emitted with
    the following attributes:

    - `entity_type`: `EventEntityType.SCENARIO^`
    - `operation`: `EventOperation.CREATION^`
    - `entity_id`: the id of the scenario
    - `creation_date`: the date and time of the event creation

Events are particularly useful when you want to:

- Update the user interface (e.g., update a list of scenarios when a new one is created)
- Trigger an action (e.g., automatically submit a scenario when its input data is updated)
- Notify end-users (e.g., send a GUI notification to all users when a job fails)
- etc.

For more examples, see the [examples](examples.md) page.
