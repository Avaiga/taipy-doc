In this section, we explore how to track activity and trigger actions by registering and
processing *events*.

# What is an Event?

Taipy, particularly its scenario and management capabilities, is designed to be natively
multi-user and asynchronous. This means you cannot control when an action is completed
(e.g., an end-user creating a scenario, a submission failing, a data node being edited,
a job completing). To handle these situations, Taipy emits *events* that you can consume
and react to. An *event* is a message emitted by Taipy when something occurs in the system.
It is represented by an object of class `Event^`. An *event* contains attributes necessary
to identify the change.

!!! example "Scenario creation event"

    For example, when a scenario is created, an event is emitted with the following attributes:

    - `entity_type`: `EventEntityType.SCENARIO^`
    - `operation`: `EventOperation.CREATION^`
    - `entity_id`: the identifier of the scenario
    - `creation_date`: the date and time of the event creation

Events are particularly useful for:

- Updating a user interface (e.g., refreshing a list of scenarios when a new one is created)
- Triggering actions (e.g., automatically submitting a scenario when its input is updated)
- Notifying end-users (e.g., sending a GUI notification when a job fails)
- And more...

For more details, see the [event description](events-description.md) page.

# What is a Registration?

Taipy provides the `Notifier.register()^` method to register for events. When you register,
you specify parameters that define the events you want to receive. These parameters allow you to
filter the events you are interested in.
For more details, see the [registration](understanding-notifier-register.md) page.

# How to process events?

To process events, follow these steps:

1. Create a new consumer class and extend it from `CoreEventConsumerBase^`.
2. Implement the `process_event` method to define your specific event-handling behavior.
3. Register the consumer using the `Notifier.register()^` method to obtain
a `registration_id` and a `registered_queue`. These values are used to instantiate a consumer
that can start consuming events.
4. You can stop the consumer and unregister from the `Notifier^` using the `registration_id` from earlier.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/create-and-start-core-event-consumer.py"
    comments=false
     %}
    ```

    This snippet shows a generic way to process all events. However, you might want to
    specify the types of events you are interested in to avoid processing all the events.
    For more details, see the [registration](understanding-notifier-register.md) page.

For more realistic examples, see the [common use cases](examples.md) page.
