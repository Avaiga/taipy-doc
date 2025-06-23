from datetime import datetime

import taipy as tp
from taipy import Config, Scope
from taipy.event import Event, EventEntityType, EventOperation, EventProcessor
from taipy.gui import Gui


def on_scenario(event: Event, gui: Gui):
    print(f"A new scenario has been created on a past cycle: {event.entity_id}")


def cycle_filter(event: Event) -> bool:
    scenario = tp.get(event.entity_id)
    if not scenario:
        return False
    return scenario.cycle.end_date < event.creation_date


if __name__ == "__main__":
    # Create a scenario configuration.
    some_datanode_cfg = Config.configure_data_node("data")
    print_task_cfg = Config.configure_task("print", print, some_datanode_cfg)
    scenario_config = Config.configure_scenario("scenario", [print_task_cfg])

    # Create the Taipy services.
    gui = Gui()
    event_processor = EventProcessor(gui)
    event_processor.on_event(callback=on_scenario,
                             entity_type=EventEntityType.SCENARIO,
                             operation=EventOperation.CREATION,
                             filter=cycle_filter
                             )
    event_processor.start()

    # Create a scenario so Taipy emits an event.
    scenario = tp.create_scenario(scenario_config)
    tp.run(gui)
