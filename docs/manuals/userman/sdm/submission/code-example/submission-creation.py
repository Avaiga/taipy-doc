import taipy as tp
from taipy import Config

def double(nb):
    return nb * 2

if __name__ == "__main__":
    # Create a scenario configuration made of one task configuration
    input_cfg = Config.configure_data_node("my_input", default_data=21)
    output_cfg = Config.configure_data_node("my_output")
    task_cfg = Config.configure_task("double_task", double, [input_cfg], [output_cfg])
    scenario_cfg = Config.configure_scenario("my_scenario", [task_cfg])

    # Run the core service
    tp.Core().run()

    # Create a scenario and submit it
    scenario = tp.create_scenario(scenario_cfg)
    submission = tp.submit(scenario)
