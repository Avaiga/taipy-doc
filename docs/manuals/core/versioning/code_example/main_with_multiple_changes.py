import taipy as tp
from taipy import Config, Scope


def example_algorithm(entry: str):
    # does nothing!
    return entry


input_cfg = Config.configure_data_node("input", path="input.pkl", scope=Scope.GLOBAL, default_data="A string")
output_cfg = Config.configure_data_node("output", path="output.pkl", scope=Scope.GLOBAL)
task_cfg = Config.configure_task("example_algorithm", example_algorithm, input_cfg, output_cfg, skippable=True)
scenario_cfg = Config.configure_scenario_from_tasks("my_scenario", [task_cfg])

if __name__ == "__main__":
    tp.Core().run()
    tp.create_scenario(scenario_cfg)
    print(f"Number of scenarios: {len(tp.get_scenarios())}")
