from taipy import Config
import taipy as tp


def double(nb):
    return nb * 2

Config.load('config_02.toml')

if __name__ == '__main__':
    # my_scenario is the id of the scenario configured
    scenario_cfg = Config.scenarios['my_scenario']

    tp.Core().run()

    scenario = tp.create_scenario(scenario_cfg, name="Scenario")
    tp.submit(scenario)
    print("First submit", scenario.output.read())

    print("Before write", scenario.input.read())
    scenario.input.write(54)
    print("After write",scenario.input.read())


    tp.submit(scenario)
    print("Second submit",scenario.output.read())

    # Basic functions of Taipy Core 
    print([s.name for s in tp.get_scenarios()])
    scenario = tp.get(scenario.id)
    tp.delete(scenario.id)
