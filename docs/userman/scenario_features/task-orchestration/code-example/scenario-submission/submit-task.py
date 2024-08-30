import taipy as tp
import my_config

if __name__ == "__main__":
    tp.Orchestrator().run()

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    task = scenario.predicting

    submission = tp.submit(task)
