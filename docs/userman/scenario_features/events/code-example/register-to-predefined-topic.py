import taipy as tp
from taipy import Config, Scenario
from taipy.event import Event, EventProcessor
from taipy.gui import Gui, State


# Define the function to be executed when the event is processed.
def store_latest_scenario(state: State, event: Event, scenario: Scenario):
    print(f"Scenario '{scenario.name}' created at '{event.creation_date}'.")
    state.latest_scenario = scenario


if __name__ == "__main__":
    # Create a scenario configuration.
    some_datanode_cfg = Config.configure_data_node("data")
    print_task_cfg = Config.configure_task("print", print, some_datanode_cfg)
    scenario_config = Config.configure_scenario("scenario", [print_task_cfg])

    # Create the Taipy services.
    gui = Gui()
    event_processor = EventProcessor(gui)
    event_processor.broadcast_on_scenario_created(callback=store_latest_scenario)
    event_processor.start()

    # Create a scenario, so Taipy emits an event.
    scenario = tp.create_scenario(scenario_config)
    scenario.data = "Some content."

    tp.run(gui)
