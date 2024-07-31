In this section, we explore how to register and process *events*.

# What is an Event

Taipy, particularly the scenario and management capability, is designed to be natively
multi-user and asynchronous. That means you cannot control when an action is done or completed
(an end-user created a scenario, my submission failed, a data node has been edited, a job
completed, etc.). For that purpose, Taipy emits *events* that you can consume and react to.
An *event* is a message that Taipy emits when something happens in the system. It is
represented by an object of class `Event^`. An *event* holds the necessary attributes to
identify the change.

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

For more details, see the [event](events-description.md) page.

# What is a Registration

Taipy exposes the `Notifier.register()^` method to register to events. When you register,
you specify parameters that define the events you want to receive. These parameters
allow you to filter the events you want to receive.
For more details, see the [registration](understanding-topics.md) page.

# How to process events

To create an event consumer, you need to create a new consumer class
and extend it from `CoreEventConsumerBase^`. Your class should implement
the `process_event` method to define their specific event handling behavior.
Then, your need to register through the `Notifier.register()^` method to get a
`registration_id` and a `registered_queue`. These values are used to instantiate
a consumer that you can start to begin consuming events.

You can also stop the consumer and unregister from the `Notifier^` with the `registration_id`
from earlier.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/create-and-start-core-event-consumer.py"
    comments=false
     %}
    ```

    This snippet provides a generic way to process all the events. However, you might want to 
    specify the type of events you are interested in to avoid processing all the events.
    For more details, see the [registration](understanding-topics.md) page.

For more realistic examples, see the [common use cases](examples.md) page.