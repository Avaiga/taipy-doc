---
title: Scenarios
category: scenario_management
data-keywords: scenario cycle configuration datanode dag
short-description: A Taipy scenario models an instance of your end-user business problem to solve on data and parameter sets.
order: 12
img: scenarios/images/scenario.png
---

In the fast-moving world of business today, people who make decisions need to adapt fast to
changes and look at different possibilities to make smart choices. Taipy scenarios are a strong
tool for running and saving sets of tasks. They can create different versions of a business
problem with different guesses. This helps users understand the effects and possibilities, which
are really important for big decisions.

![Scenarios](images/scenario.png){width=90% : .tp-image }

In this tip, we will examine Taipy scenarios more closely. We will explore what they can do
and how they can be useful when making decisions.

As a reminder, Taipy [scenarios](../../../userman/scenario_features/sdm/scenario/index.md) are one of the
fundamental concept in Taipy.

# Taipy Scenarios: An Overview

A Taipy scenario is like a test run of a business problem using specific data and settings.

You can make, save, change, and run different scenarios in one application. This makes it easy
to study various versions of a business problem. It's really useful for businesses that need to
consider many scenarios with different ideas to make the best choice.

# Example: Monthly Production Planning

Imagine a manufacturing company that has to figure out how much to produce each month based on
expected sales. The person using the system starts by setting up a plan for January. They put in
all the data they need and the rules for calculating sales predictions, deciding how much to
make, and generating production orders for January.

Next, for February, they make a new plan using updated information for that month. They can keep
doing this every month, which helps the company adjust its production plans as things change and
new information comes in.

```python
import taipy as tp
from datetime import datetime
import my_config

# Creating a scenario for January
january_scenario = tp.create_scenario(my_config.monthly_scenario_cfg,
                                      creation_date=datetime(2023, 1, 1),
                                      name="Scenario for January")

# Creating a scenario for February
february_scenario = tp.create_scenario(my_config.monthly_scenario_cfg,
                                       creation_date=datetime(2023, 2, 1),
                                       name="Scenario for February")
```

# Scenarios

Taipy scenarios include tasks and data nodes modeling any kind of data workflow. These tasks can
be submitted as a whole submitting the scenario or independently if needed. When it is
possible, Taipy runs the tasks in parallel.

## Scenario Configuration and Creation

To instantiate a Taipy scenario, users first need to configure it with the
`Config.configure_scenario()` method. They need to set certain things like a name, the tasks it
uses, how often it runs, what it compares, and its properties. Then users can create a scenario
with the `create_scenario()` function passing as a parameter the scenario configuration.

```python
from taipy import Config

# Configuration of Data Nodes, Tasks, ...
...

# Creating a scenario configuration from task configurations
scenario_cfg = Config.configure_scenario("multiply_scenario",
                                         task_configs=[task_cfg])
```

## Accessing and Managing Scenarios

Taipy offers different ways to work with scenarios. You can do things like getting a scenario by
its ID, getting all scenarios, making one scenario the main one, and comparing scenarios.

You can also add tags to scenarios to keep them organized. If you want to
transfer your scenario from one environment to the other,
it is possible to export them with the last command.

```python
...

if __name__ == "__main__":
    # Run of the Orchestrator service
    tp.Orchestrator().run()

    # Get a scenario by id
    scenario_retrieved = tp.get(scenario.id)

    # Get all scenarios
    all_scenarios = tp.get_scenarios()

    # Get primary scenarios
    all_primary_scenarios = tp.get_primary_scenarios()

    # Promote a scenario as primary
    tp.set_primary(scenario)

    # Compare scenarios (use the compare function defined in the configuration)
    comparison_results = tp.compare_scenarios(january_scenario, february_scenario, data_node_config_id="sales_predictions")

    # Tag a scenario
    tp.tag(scenario, "my_tag")

    # Export a scenario
    tp.export(scenario.id, folder_path="./monthly_scenario")
```

The primary benefit of having a scenario is to access the Data Nodes of the different scenarios
that are made. Accessing a data node is as as simple as `<scenario>.<Data Node name>.read()`.
By exploring the data nodes, end users can analyze the results of their data workflow and make
decisions upon it.

## Scenario management visual elements

The
[Scenario management visual elements](../../../refmans/gui/viselements/index.md#scenario-and-data-management-controls)
allow you to include visual elements in the Taipy backend. This makes it easier than ever to
build a web application that matches your backend.

You can add these few lines of code to your script's configuration to create a web application
that lets you:

- Choose from the scenarios you've made.
- Create new scenarios.
- Submit them.
- View the configuration used by the scenario.

=== "Python"
    ```python
    from taipy import Gui
    import taipy as tp
    import taipy.gui.builder as tgb

    ...

    if __name__ == "__main__":
        scenario = None

        with tgb.Page() as page:
            tgb.scenario_selector("{scenario}")
            tgb.scenario("{scenario}")
            tgb.scenario_dag("{scenario}")

        tp.Orchestrator().run()
        Gui(page).run()
    ```
=== "Markdown"
    ```python
    from taipy import Gui
    import taipy as tp

    ...

    if __name__ == "__main__":
        scenario = None

        scenario_md = """
    <|{scenario}|scenario_selector|>
    <|{scenario}|scenario|>
    <|{scenario}|scenario_dag|>
        """
        tp.Orchestrator().run()
        Gui(scenario_md).run()
    ```

# Conclusion

Taipy scenarios are a strong and adaptable tool that businesses can use to investigate different
situations with different assumptions. This helps in making smart decisions and analyzing their
effects.

By using Taipy scenarios, companies can gain a deeper understanding of what might happen as a
result of their choices. This knowledge allows them to make informed decisions that can lead to
success in their business.
