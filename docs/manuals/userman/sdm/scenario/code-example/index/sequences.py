import taipy as tp
from my_config import monthly_scenario_cfg

if __name__ == "__main__":
    scenario = tp.create_scenario(monthly_scenario_cfg)
    tasks = scenario.tasks
    training_task, predicting_task, planning_task = tasks["training_cfg"], tasks["predicting_cfg"], tasks["planning_cfg"]
    scenario.add_sequences({"sales": [training_task, predicting_task], "production": [planning_task]})

    # and you can remove sequence
    scenario.remove_sequences("sales")
    # or
    scenario.remove_sequences(["sales", "production"])
