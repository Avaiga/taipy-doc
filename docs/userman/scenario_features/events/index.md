In this section, we explore how to track the main application activity (on server side)
and trigger actions to refresh the user interface (on client side).

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

    - *entity_type*: `EventEntityType.SCENARIO^`
    - *operation*: `EventOperation.CREATION^`
    - *entity_id*: the identifier of the scenario
    - *creation_date*: the date and time of the event creation

Events are particularly useful for:

- Updating a user interface (e.g., refreshing a list of scenarios when a new one is created)
- Triggering actions (e.g., automatically submitting a scenario when its input is updated)
- Notifying end-users (e.g., sending a GUI notification when a job fails)
- Triggering actions (e.g., automatically submitting a scenario when its input is updated)
- And more...

For more details, see the [event description](events-description.md) page.

# How to process events?

The overall principle is to register custom callbacks to event topics. The
`EventProcessor^` service listens for events matching the topics and triggers
the callback execution when such an event is produced. This allows you to react
to events in a Taipy application, whether you want to update the user interface
or perform some server-side processing.

To process events, follow these steps:

1. Instantiate an `EventProcessor^` object providing the `Gui^` instance.
2. Register a callback to a topic using the various `EventProcessor.on_event()^` methods.
   Several methods are available to register callbacks depending on your needs:

    - `EventProcessor.on_event()^` is a generic method to register a callback to be executed on the
      server side for any matching event.
    - `EventProcessor.broadcast_on_event()^` is a generic method to register a callback to be executed
      for all clients for any matching event.
    - several specific methods are available to register callbacks to be executed
      for specific matching events, such as `EventProcessor.on_scenario_created()^`,
      `EventProcessor.broadcast_on_datanode_written()^`, etc.

3. Start the `EventProcessor^` service to begin listening for events.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/create-and-start-event-processor.py"
    comments=false
     %}
    ```

    This snippet shows two generic ways to process events.

    In line 8, a first callback is defined to be executed for every event emitted by Taipy.
    The callback takes an `Event^` object and a `Gui^` instance as parameters.
    It is registered in line 25 using the `EventProcessor.on_event()^` method.

    In line 9, a second callback is defined to be broadcast to all states. It takes
    a state and an `Event^` object as parameters. It is registered in line 26 using the
    `EventProcessor.broadcast_on_event()^` method.

However, you might want to specify the types of events you are interested in to avoid
processing all the events. For more details, see the [topic description](topics.md) page.

For more realistic examples, see the [examples](examples.md) page.
