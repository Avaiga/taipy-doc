from taipy import Config
import taipy as tp

# Normal function used by Taipy
def double(nb):
    return nb * 2


Config.load('config_01.toml')

if __name__ == '__main__':    
    # my_scenario is the id of the scenario configured
    scenario_cfg = Config.scenarios['my_scenario']


    # Run of the Core
    tp.Core().run()

    # Creation of the scenario and execution
    scenario = tp.create_scenario(scenario_cfg)
    tp.submit(scenario)

    print("Value at the end of task", scenario.output.read())