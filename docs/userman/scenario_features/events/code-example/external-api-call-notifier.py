import requests

import taipy as tp
import taipy.gui.builder as tgb
from taipy import Config, Gui, Orchestrator
from taipy.core.job.status import Status
from taipy.core.notification import EventEntityType, EventOperation
from taipy.event import EventProcessor


##### Configuration and Functions #####
def fail_task(name: str):
    raise Exception(f"This function is trigger by {name} and is designed to fail!")


name_data_node_cfg = Config.configure_data_node(id="input_name", default_data="Florian")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", fail_task, name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

value = "Default text"


#### Event callbacks ####
def trigger_external_api(event, gui):
    if event.attribute_value == Status.FAILED:
        job_id = event.entity_id
        requests.get("http://127.0.0.1:5000/replace-this-with-your-api", params={"message": f"Job {job_id} failed."})


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
    event_processor = EventProcessor(gui)
    event_processor.on_event(callback=trigger_external_api,
                             entity_type=EventEntityType.JOB,
                             operation=EventOperation.UPDATE,
                             attribute_name="status")
    event_processor.start()
    orchestrator.run()
    gui.run()
