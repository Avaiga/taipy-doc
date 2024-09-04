import taipy as tp
from taipy import Config


def do_nothing():
    ...

def my_global_subscriber(scenario, job):
    print(f"  my_global_subscriber: scenario '{scenario.config_id}'; task '{job.task.config_id}'.")

def my_subscriber(scenario, job):
    print(f"  my_subscriber: scenario '{scenario.config_id}'; task '{job.task.config_id}'.")

def my_subscriber_multi_param(scenario, job, params):
    print(f"  my_subscriber_multi_param: params {params}; task '{job.task.config_id}'.")

if __name__ == "__main__":
    task_1 = Config.configure_task("my_task_1", do_nothing)
    task_2 = Config.configure_task("my_task_2", do_nothing)
    scenario_1 = Config.configure_scenario("my_scenario", [task_1, task_2])
    scenario_2 = Config.configure_scenario("my_scenario", [task_1, task_2])

    tp.Orchestrator().run()

    params = ["my_param_1", 42]

    tp.subscribe_scenario(my_global_subscriber)  # Global subscription
    tp.subscribe_scenario(my_subscriber, scenario_1)  # Subscribe only to one scenario
    tp.subscribe_scenario(my_subscriber_multi_param, params, scenario_1)  # Subscribe with params

    print('Submit: scenario_1')
    tp.submit(scenario_1)
    print('Submit: scenario_2')
    tp.submit(scenario_2)
    print('Unsubscribe to my_global_subscriber for scenario_1')
    tp.unsubscribe_scenario(my_global_subscriber, scenario_1)
    print('Submit: scenario_1')
    tp.submit(scenario_1)
