import taipy as tp
from taipy import Config, Scope


def placeholder_algo(entry: str):
    # does nothing!
    return entry


input_cfg = Config.configure_data_node("input", path="input.pkl", scope=Scope.GLOBAL, default_data="a_string")
output_cfg = Config.configure_data_node("output", path="output.pkl", scope=Scope.GLOBAL)
task_cfg = Config.configure_task("placeholder_algo", placeholder_algo, input_cfg, output_cfg, skippable=True)
scenario_cfg = Config.configure_scenario_from_tasks("my_scenario", [task_cfg])

if __name__ == "__main__":
    tp.Core().run()
    tp.create_scenario(scenario_cfg)
    print(f"nb scenarios: {len(tp.get_scenarios())}")
