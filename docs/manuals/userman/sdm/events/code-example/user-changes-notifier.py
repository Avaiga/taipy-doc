import taipy as tp
import taipy.gui.builder as tgb
from taipy import Config, Gui, Orchestrator
from taipy.core import SubmissionStatus
from taipy.core.notification import CoreEventConsumerBase, EventEntityType, EventOperation, Notifier
from taipy.gui import notify

##### Configuration and Functions #####


def build_message(name: str):
    return f"Hello {name}!"


name_data_node_cfg = Config.configure_data_node(id="input_name", default_data="Florian")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

value = "Default text"


#### Notification function to be called ####


def notify_users_of_creation(state):
    state.value = "Scenario created and submitted"
    notify(state, "s", "Scenario Created")


def notify_users_of_update(state, new_value_of_dn):
    print("Value of Data Node:", new_value_of_dn)
    state.value = f"Data Node updated with value: {new_value_of_dn}"
    notify(state, "i", "Data Node Updated")


class SpecificCoreConsumer(CoreEventConsumerBase):
    def __init__(self, gui):
        self.gui = gui
        reg_id, queue = Notifier.register()  # Adapt the registration to the events you want to listen to
        super().__init__(reg_id, queue)

    def process_event(self, event):
        if event.operation == EventOperation.CREATION:
            if event.entity_type == EventEntityType.SCENARIO:
                self.gui.broadcast_callback(notify_users_of_creation)
        elif event.operation == EventOperation.UPDATE:
            if event.entity_type == EventEntityType.SUBMISSION:
                print(event)
                if event.attribute_value == SubmissionStatus.COMPLETED:
                    scenario_id = event.metadata["origin_entity_id"]
                    scenario = tp.get(scenario_id)
                    new_value_of_dn = scenario.message.read()
                    self.gui.broadcast_callback(notify_users_of_update, [new_value_of_dn])


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
    SpecificCoreConsumer(gui).start()
    gui.run()
