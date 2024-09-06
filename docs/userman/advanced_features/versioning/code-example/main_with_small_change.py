import taipy as tp
from taipy import Config


def example_algorithm(entry: str):
    # does nothing!
    return entry

if __name__ == "__main__":
    input_cfg = Config.configure_data_node("my_input", default_data="a_string")
    output_cfg = Config.configure_data_node("my_output", description="What a description")
    task_cfg = Config.configure_task("example_algorithm", example_algorithm, input_cfg, output_cfg)
    scenario_cfg = Config.configure_scenario("my_scenario", [task_cfg])

    tp.Orchestrator().run()
    tp.create_scenario(scenario_cfg)
    print(f"Number of scenarios: {len(tp.get_scenarios())}")
