if __name__ == "__main__":
    import taipy as tp
    import my_config

    core = tp.Core()

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    submission = tp.submit(scenario)
    core.run()
