Examples of using Taipy event notifications to capture and consume *events*.

# Real-Time GUI Updates with Taipy Event Consumers

This example demonstrates the power of event-driven programming in real-world applications. By
capturing and processing events, developers can build responsive, dynamic systems that notify
users of important changes (such as new scenario creations or data node updates) as they happen.
This approach significantly enhances the user experience by providing real-time updates and
ensuring users are always informed through an interactive and engaging interface.

This script defines a custom event consumer class `SpecificCoreConsumer`, which listens
for all events published by Taipy and triggers GUI notification based on those events.
It includes determining if the event is published from a `Scenario^` entity or `DataNode^` entity
and if the action is `CREATION` or `UPDATE`.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/user-changes-notifier.py"
    comments=false
     %}
    ```

    This snippet shows how you can capture and process events to notify users whenever
    a new scenario is created, or a data node's value is updated.
    For more details, see the [registration](understanding-notifier-register.md) page.

# External API triggered with Taipy Event Consumers

This example illustrates leveraging event-driven programming to monitor and respond to
specific event types. By implementing a custom event consumer, `JobFailureCoreConsumer`,
developers can easily trigger external API calls based on specific job status updates. This
approach ensures that critical job status changes are promptly communicated to external systems,
enhancing the application's monitoring and integration with third-party systems.

This script defines a custom event consumer class `JobFailureCoreConsumer`, which listens
for all events published by Taipy, when a `JOB` entity's `status` attribute is `UPDATE`,
and triggers an external API call based on the `JOB`'s `id`.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/external-api-call-notifier.py"
    comments=false
     %}
    ```

    This snippet shows how you can capture and process `JOB` events when an `UPDATE` is made to the `status`
    of the `JOB` and request an external API.
    For more details, see the [registration](understanding-notifier-register.md) page.

