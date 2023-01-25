import taipy.core as tp
from taipy import Config


def my_print_algo(entry: str):
    # does nothing!
    return entry


input_cfg = Config.configure_data_node("input", default_data="a_string")
output_cfg = Config.configure_data_node("output")
task_cfg = Config.configure_task("my_print_algo", my_print_algo, input_cfg, output_cfg)
scenario_cfg = Config.configure_scenario_from_tasks("my_scenario", [task_cfg])

if __name__ == "__main__":

    tp.Core().run()
    tp.create_scenario(scenario_cfg)

