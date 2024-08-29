from datetime import datetime
import my_config
import taipy as tp

if __name__ == "__main__":
    # Create a scenario using the monthly scenario configuration.
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg,
                                creation_date=datetime(2022, 1, 3))
    cycle = scenario.cycle

    # The frequency is an attribute of the cycle. In the example, it equals
    # Frequency.MONTHLY since my_config.monthly_scenario_cfg is used has been
    # used to instantiate scenario and cycle.
    cycle.frequency
    # The creation date is the date-time provided at the creation. It equals datetime(2022, 1, 3)
    cycle.creation_date
    # The start date is the date-time of the start of the cycle. It equals datetime(2022, 1, 1)
    cycle.start_date
    # The end date is the date-time of the end of the cycle. It equals datetime(2022, 1, 31)
    cycle.end_date
    # By default, the `name` is generated. It can be set manually to be displayed in a user interface.
    cycle.name = "January cycle"
