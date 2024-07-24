This page covers how you can utilize the Core event consumer feature to get notifications
about the changes to the entities in the Core service.

Objects of class `Event^` are used to represent the changes in the Core service.
An `Event^` object holds the necessary attributes to identify the change.

For more details and examples, see the
[event descriptions](../events-description.md) page.

`CoreEventConsumerBase^` provides a framework for defining custom logic to consume `Event^` from
a queue in a separate thread

# Create an event consumer

To create an event consumer, you need to create a new consumer class
and extend it from `CoreEventConsumerBase^`. You class should implement
the `process_event` method to define their specific event handling behavior.

Then, we register with the `Notifier^` to retrieve a `registration_id` and a `registered_queue`,
which is an event queue. These values will be used to create an object of the consumer class.

Finally, we can begin consuming events from Core service by starting the consumer. After finishing,
we can stop the consumer and unregister from the `Notifier^` with the `registration_id` from earlier.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/create-and-start-core-event-consumer.py"
    comments=false
     %}
    ```

This snippet provides a method to listen to all events emitting by the Core service. However, 
we might want to specify the type of events we want to receive by providing topics during 
the registration process.

For more details and examples, see the
[understanding topics](../understanding-topics.md) page.
