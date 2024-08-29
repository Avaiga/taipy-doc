import random

import taipy as tp
from taipy import Config


def random_value():
    return random.randint(0, 100)

if __name__ == "__main__":
    # Configure a data node, a tasks and a scenario
    int_cfg = Config.configure_data_node("random_val", scope=tp.Scope.GLOBAL, default_data=12)
    task_cfg = Config.configure_task("random_task", function=random_value, output=int_cfg)
    scenario_cfg = Config.configure_scenario("random_scenario", task_configs=[task_cfg])

    # Create a data node along with a scenario. A default value is written automatically
    scenario = tp.create_scenario(scenario_cfg)
    data_node = scenario.random_val

    # Manually write a new value to the data node
    data_node.write(100, editor="John", comment="Manual edition: 100", extra="extra data")

    # Submit the scenario so that the data node is written again through a job
    tp.Orchestrator().run()
    scenario.submit()

    print(data_node.edits)
    # [{'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 652773), 'editor': 'TAIPY', 'comment': 'Default data written.'},
    # {'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 689737), 'editor': 'John', 'comment': 'Manual edition: 100', 'extra': 'extra data'},
    # {'timestamp': datetime.datetime(2024, 5, 14, 20, 12, 27, 856928), 'job_id': 'JOB_random_task_a8031d80-26f7-406e-9b31-33561d0f9ccd'}]

    tp.Gui("<|{scenario.random_val}|data_node|>").run()
