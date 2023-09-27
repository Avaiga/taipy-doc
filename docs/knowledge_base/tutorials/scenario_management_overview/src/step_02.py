from taipy import Config
import taipy as tp


def double(nb):
    return nb * 2

input_data_node_cfg = Config.configure_data_node("input", default_data=21)
output_data_node_cfg = Config.configure_data_node("output")

task_cfg = Config.configure_task("double",
                                 double,
                                 input_data_node_cfg,
                                 output_data_node_cfg)

scenario_cfg = Config.configure_scenario(id="my_scenario",
                                                    task_configs=[task_cfg])

Config.export('config_02.toml')

if __name__ == '__main__':
    tp.Core().run()

    scenario = tp.create_scenario(scenario_cfg, name="Scenario")
    tp.submit(scenario)
    print("Output of First submit:", scenario.output.read())

    print("Before write", scenario.input.read())
    scenario.input.write(54)
    print("After write",scenario.input.read())


    tp.submit(scenario)
    print("Second submit",scenario.output.read())

    # Basic functions of Taipy Core 
    print([s.name for s in tp.get_scenarios()])
    scenario = tp.get(scenario.id)
    tp.delete(scenario.id)

    scenario = None
    data_node = None

    tp.Gui("""<|{scenario}|scenario_selector|>
              <|{scenario}|scenario|>
              <|{scenario}|scenario_dag|>
              <|{data_node}|data_node_selector|>""").run()
