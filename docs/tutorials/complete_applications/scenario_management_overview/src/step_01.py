from taipy import Config
import taipy as tp

# Normal function used by Taipy
def double(nb):
    return nb * 2

# Configuration of Data Nodes
input_data_node_cfg = Config.configure_data_node("input", default_data=21)
output_data_node_cfg = Config.configure_data_node("output")

# Configuration of tasks
task_cfg = Config.configure_task("double",
                                 double,
                                 input_data_node_cfg,
                                 output_data_node_cfg)

# Configuration of the pipeline and scenario
pipeline_cfg = Config.configure_pipeline("my_pipeline", [task_cfg])
scenario_cfg = Config.configure_scenario("my_scenario", [pipeline_cfg])

Config.export('config_01.toml')

if __name__ == '__main__':
    # Run of the Core
    tp.Core().run()

    # Creation of the scenario and execution
    scenario = tp.create_scenario(scenario_cfg)
    tp.submit(scenario)

    print("Value at the end of task", scenario.output.read())