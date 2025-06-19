---
title: Examples of Taipy Event usage
---

These examples demonstrate the power of event-driven programming in real-world applications.

# Real-Time GUI Updates

By consuming and processing events, developers can build reactive and dynamic systems that
notify end-users of important changes (such as new scenario creations or data node updates)
as they happen. This approach significantly enhances the user experience by providing
real-time updates and ensuring users are always informed through an interactive and
engaging interface.

This example registers callbacks to trigger GUI notifications depending on the event
parameters.

!!! example
    ```python linenums="1"
    {%
    include-markdown "./code-example/user-changes-notifier.py"
    comments=false
     %}
    ```

    This snippet shows how you can process events to notify users whenever
    a scenario is created, submitted or completed.

# External API calls

The following example illustrates how to integrate external systems with a Taipy
application by consuming events. It demonstrates how to trigger external API calls
when specific job status updates occur, such as when a job fails. This integration
allows for seamless communication between a Taipy application and an external service.

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

    This snippet shows how you can process Taipy events to trigger calls to an external
    API whenever a job fails.

