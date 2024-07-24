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

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/register-specific-topic-to-notifier.py"
    comments=false
     %}
    ```
