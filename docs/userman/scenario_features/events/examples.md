Examples of using Taipy event notifications to capture and consume *events*.

# Real-Time GUI Updates with Taipy Event Consumers

This example is provided to demonstrate the practical application of event-driven programming in
a real-world scenario. By capturing and processing events, developers can create responsive and
dynamic systems that notify users of important changes, such as the creation of new scenarios or
updates to data nodes. This approach enhances user experience by ensuring that users are always
informed of relevant updates in real-time.

This script defines a custom event consumer class `SpecificCoreConsumer`, which listens
for all events published by Taipy Core and triggers GUI notification based on those events.
It includes determining if the event is published from a `Scenario^` entity or `DataNode^` entity
and if the action is `CREATION^` or `UPDATE^`.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/user-changes-notifier.py"
    comments=false
     %}
    ```

    This snippet shows a how you can capture and process events to notify user whenever
    a new scenario is created or the value of a data node is updated.
    For more details, see the [registration](understanding-topics.md) page.

# External API triggered with Taipy Event Consumers

This example illustrates how to effectively utilize event-driven programming to monitor and
respond to changes of specific event type within Taipy Core. By defining a custom event consumer,
`JobFailureCoreConsumer`, developers can seamlessly integrate external API calls triggered
by specific job status updates. This approach ensures that critical job status changes are promptly
communicated to external systems, enhancing the robustness and responsiveness of the application.

This script defines a custom event consumer class `JobFailureCoreConsumer`, which listens
for all events published by Taipy Core, when a `JOB^` entity's `status` attribute is `UPDATE`,
and triggers an external API call based on the `JOB^`'s `id`.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/external-api-call-notifier.py"
    comments=false
     %}
    ```

    This snippet shows a how you can capture and process `JOB^` events when an `UPDATE` is made to the `status`
    of the `JOB^` and request an external API.
    For more details, see the [registration](understanding-topics.md) page.
Examples of using Taipy event notifications to capture and consume *events*.

# Real-Time GUI Updates with Taipy Event Consumers

This example is provided to demonstrate the practical application of event-driven programming in
a real-world scenario. By capturing and processing events, developers can create responsive and
dynamic systems that notify users of important changes, such as the creation of new scenarios or
updates to data nodes. This approach enhances user experience by ensuring that users are always
informed of relevant updates in real-time.

This script defines a custom event consumer class `SpecificCoreConsumer`, which listens
for all events published by Taipy Core and triggers GUI notification based on those events.
It includes determining if the event is published from a `Scenario^` entity or `DataNode^` entity
and if the action is `CREATION^` or `UPDATE^`.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/user-changes-notifier.py"
    comments=false
     %}
    ```

    This snippet shows a how you can capture and process events to notify user whenever
    a new scenario is created or the value of a data node is updated.
    For more details, see the [registration](understanding-topics.md) page.

# External API triggered with Taipy Event Consumers

This example illustrates how to effectively utilize event-driven programming to monitor and
respond to changes of specific event type within Taipy Core. By defining a custom event consumer,
`JobFailureCoreConsumer`, developers can seamlessly integrate external API calls triggered
by specific job status updates. This approach ensures that critical job status changes are promptly
communicated to external systems, enhancing the robustness and responsiveness of the application.

This script defines a custom event consumer class `JobFailureCoreConsumer`, which listens
for all events published by Taipy Core, when a `JOB^` entity's `status` attribute is `UPDATE`,
and triggers an external API call based on the `JOB^`'s `id`.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/external-api-call-notifier.py"
    comments=false
     %}
    ```

    This snippet shows a how you can capture and process `JOB^` events when an `UPDATE` is made to the `status`
    of the `JOB^` and request an external API.
    For more details, see the [registration](understanding-topics.md) page.
