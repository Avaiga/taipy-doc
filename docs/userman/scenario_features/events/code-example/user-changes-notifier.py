import taipy as tp
import taipy.gui.builder as tgb
from taipy import Config, Gui, Orchestrator, Scenario, SubmissionStatus
from taipy.event import EventEntityType, EventOperation, EventProcessor
from taipy.gui import notify


##### Configuration and Functions #####
def build_message(name: str):
    return f"Hello {name}!"


name_data_node_cfg = Config.configure_data_node(id="input_name", default_data="Florian")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

value = "Default text"


#### Event callbacks ####
def notify_users_of_creation(state, event):
    state.value = "Scenario created"
    notify(state, "s", "Scenario Created")


def notify_users_of_submission(state, event):
    state.value = "Scenario submitted"
    notify(state, "s", "Scenario Submitted")


def notify_users_of_update(state, event):
    submission = tp.get(event.entity_id)
    if not submission:
        return
    scenario = tp.get(submission.entity_id)
    if not scenario or not isinstance(scenario, Scenario):
        return
    if event.attribute_value != SubmissionStatus.COMPLETED:
        return
    new_value_of_dn = scenario.message.read()
    state.value = f"Data Node updated with value: {new_value_of_dn}"
    notify(state, "i", "Data Node Updated")

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
    event_processor.broadcast_on_event(callback=notify_users_of_creation,
                                       entity_type=EventEntityType.SCENARIO,
                                       operation=EventOperation.CREATION)
    event_processor.broadcast_on_event(callback=notify_users_of_submission,
                                       entity_type=EventEntityType.SCENARIO,
                                       operation=EventOperation.SUBMISSION)
    event_processor.broadcast_on_event(callback=notify_users_of_update,
                                       entity_type=EventEntityType.SUBMISSION,
                                       operation=EventOperation.UPDATE,
                                       attribute_name="status")
    event_processor.start()
    orchestrator.run()
    gui.run()
