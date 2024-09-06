import requests

import taipy as tp
import taipy.gui.builder as tgb
from taipy import Config, Gui, Orchestrator
from taipy.core import SubmissionStatus
from taipy.core.job.status import Status
from taipy.core.notification import CoreEventConsumerBase, EventEntityType, EventOperation, Notifier
from taipy.gui import notify

##### Configuration and Functions #####


def fail_task(name: str):
    raise Exception(f"This function is trigger by {name} and is supposed to fail, and it did!")


name_data_node_cfg = Config.configure_data_node(id="input_name", default_data="Florian")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", fail_task, name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

value = "Default text"


#### Notification function to be called ####


def trigger_api_of_job_failure(job_id):
    requests.get("http://127.0.0.1:5000/replace-this-with-your-api", params={"message": f"Job {job_id} failed."})


class JobFailureCoreConsumer(CoreEventConsumerBase):
    def __init__(self):
        reg_id, queue = Notifier.register(
            entity_type=EventEntityType.JOB, operation=EventOperation.UPDATE, attribute_name="status"
        )  # Adapt the registration to the events you want to listen to
        super().__init__(reg_id, queue)

    def process_event(self, event):
        if event.attribute_value == Status.FAILED:
            trigger_api_of_job_failure(event.entity_id)


#### Normal callbacks ####


def create_and_submit_scenario(state):
    scenario = tp.create_scenario(config=scenario_cfg)
    tp.submit(scenario)


#### Page ####

with tgb.Page() as page:
    tgb.text("{value}")
    tgb.button("Create and submit a scenario!", on_action=create_and_submit_scenario)


if __name__ == "__main__":
    orchestrator = Orchestrator()
    gui = Gui(page)
    orchestrator.run()
    JobFailureCoreConsumer().start()
    gui.run()
