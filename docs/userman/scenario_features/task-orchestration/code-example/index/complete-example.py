import taipy as tp
from taipy import Config


def do_nothing(value):
    print(f"do_nothing but printing the value: {value}")

if __name__ == "__main__":
    # Configure a scenario
    value_cfg = Config.configure_data_node("my_value", default_data=42)
    task_cfg = Config.configure_task("my_task", do_nothing, input=[value_cfg])
    scenario_cfg = Config.configure_scenario("my_scenario", [task_cfg])

    # Run the Orchestrator service
    tp.Orchestrator().run()

    # Create a scenario
    scenario = tp.create_scenario(scenario_cfg)

    # Submit the scenario
    tp.submit(scenario)
