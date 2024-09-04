Examples of using Taipy event notifications to capture and consume *events*.

# Real-Time GUI Updates with Taipy Event Consumers

This script defines a custom event consumer class `SpecificCoreConsumer`, which listens
for all events published by Taipy Core and triggers GUI notification based on those events.
It includes determining if the event is published from a `Scenario^` entity or `DataNode^` entity
and if the action is `CREATION` or `UPDATE`.


```python linenums="1"
{%
include-markdown "./code-example/user-changes-notifier.py"
comments=false
    %}
```

This snippet shows a how you can capture and process events to notify user whenever
a new scenario is created or the value of a data node is updated.
For more details, see the [registration](understanding-notifier-register.md) page.

# External API triggered with Taipy Event Consumers

This script defines a custom event consumer class `JobFailureCoreConsumer`, which listens
for all events published by Taipy Core, when a `JOB` entity's `status` attribute is `UPDATE`,
and triggers an external API call based on the `JOB`'s `id`.


```python linenums="1"
{%
include-markdown "./code-example/external-api-call-notifier.py"
comments=false
    %}
```

This snippet shows a how you can capture and process `JOB` events when an `UPDATE` is made to the `status`
of the `JOB` and request an external API.
For more details, see the [registration](understanding-notifier-register.md) page.
