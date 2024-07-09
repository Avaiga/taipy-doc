if __name__ == "__main__":
    import taipy as tp
    import my_config

    core = tp.Core()
    core.run()

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    submission = scenario.submit()
