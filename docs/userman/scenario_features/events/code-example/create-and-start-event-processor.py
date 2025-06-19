import taipy as tp
from taipy import Config
from taipy.event import Event, EventProcessor
from taipy.gui import Gui


# Define the functions to be executed when the event is processed.
def process_event(event: Event, gui: Gui):
    # Custom event processing logic here
    print(f"Received a {event.entity_type} {event.operation} event at : {event.creation_date}")

def broadcast_event(state, event: Event):
    # Custom event broadcast to all states
    print(f"Broadcasting event: {event.entity_type} {event.operation} at {event.creation_date}")

if __name__ == "__main__":
    # Create a scenario configuration.
    some_datanode_cfg = Config.configure_data_node("data")
    print_task_cfg = Config.configure_task("print", print, some_datanode_cfg)
    scenario_config = Config.configure_scenario("scenario", [print_task_cfg])

    # create the taipy services.
    gui = Gui()
    event_processor = EventProcessor(gui)
    event_processor.on_event(callback=process_event)
    event_processor.broadcast_on_event(callback=broadcast_event)
    event_processor.start()

    # Create a scenario, so Taipy emits an event.
    scenario = tp.create_scenario(scenario_config)
    scenario.data = "Some content."

    tp.run(gui)
