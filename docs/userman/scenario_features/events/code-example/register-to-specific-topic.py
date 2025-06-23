import taipy as tp
from taipy import Config
from taipy.event import Event, EventEntityType, EventOperation, EventProcessor
from taipy.gui import Gui


# Define the functions to be executed when the event is processed.
def on_entity_creation(event: Event, gui: Gui):
    print(f" {event.entity_type} entity created at {event.creation_date}")

def on_scenario(event: Event, gui: Gui):
    print(f"Scenario '{event.entity_id}' processed for a '{event.operation}' operation.")

if __name__ == "__main__":
    # Create a scenario configuration.
    some_datanode_cfg = Config.configure_data_node("data")
    print_task_cfg = Config.configure_task("print", print, some_datanode_cfg)
    scenario_config = Config.configure_scenario("scenario", [print_task_cfg])

    # Create the Taipy services.
    gui = Gui()
    event_processor = EventProcessor(gui)
    event_processor.on_event(callback=on_entity_creation, operation=EventOperation.CREATION)
    event_processor.on_event(callback=on_scenario, entity_type=EventEntityType.SCENARIO)
    event_processor.start()

    # Create a scenario, so Taipy emits an event.
    scenario = tp.create_scenario(scenario_config)
    scenario.data = "Some content."

    tp.run(gui)
