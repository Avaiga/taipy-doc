When registering to the Notifier, you can specify which events you want to receive by providing topics.

A topic is defined by the combination of an optional entity type, an optional
entity id, an optional operation, and an optional attribute name. The purpose is
to be as flexible as possible. For example, we can register to:

- All actions emitted by Core
- All behaviors of scenarios
- All actions related to a certain data node
- All task creations
- A specific data node update
- A sequence submission
- A scenario deletion
- Job failures

Topic is defined when you call `Notifier.register()^` method with the following
parameters:

- _**entity_type**_: If provided, the listener will be notified for all events related to this entity type. 
    Otherwise, the listener will be notified for events related to all entity types. The possible entity type values
    are defined in the `EventEntityType^` enum. The possible values are:
    - CYCLE
    - SCENARIO
    - SEQUENCE
    - TASK
    - DATA_NODE
    - JOB
    - SUBMISSION

- _**entity_id**_: If provided, the listener will be notified for all events related to this entity.
    Otherwise, the listener will be notified for events related to all entities.

- _**operation**_: If provided, the listener will be notified for all events related to this operation.
    Otherwise, the listener will be notified for events related to all operations. The possible operation values are 
    defined in the `EventOperation^` enum. The possible values are:
    - CREATION
    - UPDATE
    - DELETION
    - SUBMISSION

- _**attribute_name**_: If provided, the listener will be notified for all events related to this entity's attribute.
    Otherwise, the listener will be notified for events related to all attributes.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/register-specific-topic-to-notifier.py"
    comments=false
     %}
    ```
