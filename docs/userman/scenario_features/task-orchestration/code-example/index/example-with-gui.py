from taipy import Config, Orchestrator, Gui


# Implementing a function to be used as a Taipy task in a scenario
def identity(*values):
    return values

if __name__ == "__main__":
    # Creating a scenario variable and a job variable to be bound to the visual elements
    scenario = None
    job = None

    # Configure a scenario
    in_cfg = Config.configure_data_node(id="inpt", default_data="IN")
    out_cfg = Config.configure_data_node(id="outpt")
    task_cfg = Config.configure_task(id="fct", function=identity, input=[in_cfg], output=[out_cfg])
    scenario_cfg = Config.configure_scenario(id="scenario", task_configs=[task_cfg])

    # Run the Orchestrator service
    Orchestrator().run()

    # Run the GUI service with a scenario selector, a scenario viewer, and a job selector
    page = ("""<|{scenario}|scenario_selector|>
<|{scenario}|scenario|>
<|{job}|job_selector|>
""")
    Gui(page=page).run()
