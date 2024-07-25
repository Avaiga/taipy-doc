Event object is used to notify any change in the Core service.

In an `Event^` object, `EventEntityType^` is an Enum representing the entity type. It is used as an attribute of
the `Event^` object to describe the entity that was changed. The possible operations are `CYCLE`, `SCENARIO`,
`SEQUENCE`, `TASK`, `DATA_NODE`, `JOB` or `SUBMISSION`.

There is also the `EventOperation^`, which is an Enum representing a type of operation performed on a Core entity. 
It is used as an attribute of the `Event^` object to describe the operation performed on an entity.
The possible operations are `CREATION`, `UPDATE`, `DELETION`, or `SUBMISSION`.

An event holds the following attributes to represent the change:

- _**entity_type**_: Type of the entity that was changed (`DataNode^`, `Scenario^`, `Cycle^`, etc. ).
- _**tasks**_: A list of task configurations.
- _**entity_id**_: Unique identifier of the entity that was changed.
- _**operation**_: Enum describing the operation (among `CREATION`, `UPDATE`, `DELETION`, and `SUBMISSION`) 
    that was performed on the entity.
- _**attribute_name**_: Name of the entity's attribute changed. Only relevant for `UPDATE` operations
- _**attribute_value**_: Name of the entity's attribute changed. Only relevant for `UPDATE` operations.
- _**metadata**_: A dict of additional medata about the source of this event
- _**creation_date**_: Date and time of the event creation.
