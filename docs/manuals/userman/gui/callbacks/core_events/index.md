
# Real-time feedback on the GUI

The `on_submission_change` property extends this functionality in a
GUI setting. It triggers a specific function upon each
submission status change, enabling real-time updates to the user interface. This
ensures that users are always informed of the current status, from SUBMITTED to
COMPLETED or CANCELED, enhancing user experience through immediate feedback and
interaction.

# Parameters of the Function

- `state (State)`: The state instance.
- `submittable (Submittable)`: The entity, usually a Scenario, that was submitted.
- `details (dict)`: Details on this callback's invocation, including the new status of the submission and the Job causing the status change.

# Handling Different Submission Statuses

Here’s an example of how you can use this property in your code:

```python
from taipy.gui import Gui, notify

def on_submission_status_change(state, submittable, details):
    submission_status = details.get('submission_status')

    if submission_status == 'COMPLETED':
        print(f"{submittable.name} has completed.")
        notify(state, 'success', 'Completed!')
        # Add additional actions here, like updating the GUI or logging the completion.

    elif submission_status == 'FAILED':
        print(f"{submittable.name} has failed.")
        notify(state, 'error', 'Completed!')
        # Handle failure, like sending notifications or logging the error.

    # Add more conditions for other statuses as needed.
```

# Implementing in GUI

When creating a GUI for your scenarios, you can associate this function with a visual element for real-time updates. For example:

```
<|{scenario}|scenario|on_submission_change=on_submission_status_change|>
```

This visual element will be updated whenever there is a change in the submission status, providing real-time feedback on the GUI.

# Entire code

```python
import taipy as tp
from taipy.config import Config
from taipy.core import Status
from taipy.gui import Gui, notify


# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    return nb + 10

def on_submission_status_change(state=None, submittable=None, details=None):
    submission_status = details.get('submission_status')

    if submission_status == 'COMPLETED':
        print(f"{submittable.name} has completed.")
        notify(state, 'success', 'Completed!')
        # Add additional actions here, like updating the GUI or logging the completion.

    elif submission_status == 'FAILED':
        print(f"{submittable.name} has failed.")
        notify(state, 'error', 'Completed!')
        # Handle failure, like sending notifications or logging the error.

    # Add more conditions for other statuses as needed.

def callback_scenario_state(scenario, job):
    """All the scenarios are subscribed to the callback_scenario_state function. It means whenever a job is done, it is called.
    Depending on the job and the status, it will update the message stored in a json that is then displayed on the GUI.

    Args:
        scenario (Scenario): the scenario of the job changed
        job (_type_): the job that has its status changed
    """
    print(f'{job.id} to {job.status}')

    if job.status == Status.COMPLETED:
        for data_node in job.task.output.values():
            print("Data node value:", data_node.read())

if __name__=="__main__":
    # Configuration of Data Nodes
    input_cfg = Config.configure_data_node("my_input", default_data=21)
    intermediate_cfg = Config.configure_data_node("intermediate")
    output_cfg = Config.configure_data_node("my_output")

    # Configuration of tasks
    first_task_cfg = Config.configure_task("double",
                                        double,
                                        input_cfg,
                                        intermediate_cfg)

    second_task_cfg = Config.configure_task("add",
                                            add,
                                            intermediate_cfg,
                                            output_cfg)

    # Configuration of scenario
    scenario_cfg = Config.configure_scenario(id="my_scenario",
                                            task_configs=[first_task_cfg, second_task_cfg],
                                            name="my_scenario")

    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.subscribe(callback_scenario_state)

    scenario_1.submit(wait=True)

    scenario_md = """
<|{scenario_1}|scenario|on_submission_change=on_submission_status_change|>
    """
    Gui(scenario_md).run()
```



### **Example with Core Events**

Using Taipy’s core event system to trigger actions when specific events occur, such as scenario creation or submission completion.

```python
from taipy.core.notification import CoreEventConsumerBase, EventOperation, EventEntityType

class MyEventConsumer(CoreEventConsumerBase):
    def process_event(self, event):
        if event.operation == EventOperation.UPDATE and event.entity_type == EventEntityType.SUBMISSION:
            print(f"Submission updated: {event.attribute_value}")

MyEventConsumer().start()
```
