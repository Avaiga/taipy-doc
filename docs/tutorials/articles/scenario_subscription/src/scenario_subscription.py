import taipy as tp
from taipy.common.config import Config
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

    tp.Orchestrator().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.subscribe(callback_scenario_state)

    scenario_1.submit(wait=True)

    scenario_md = """
<|{scenario_1}|scenario|on_submission_change=on_submission_status_change|>
    """
    Gui(scenario_md).run()
