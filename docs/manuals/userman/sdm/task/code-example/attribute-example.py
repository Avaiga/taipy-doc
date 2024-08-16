import taipy as tp
import my_config

if __name__ == "__main__":
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    task = scenario.predicting

    # the config_id is an attribute of the task. Here it equals "predicting"
    task.config_id

    # the function to be executed with data from input data
    # nodes and returns value for output data nodes.
    task.function  # predict

    # input is the list of input data nodes of the task
    task.input  # [trained_model_cfg, current_month_cfg]

    # output is the list of output data nodes of the task
    task.output  # [sales_predictions_cfg]

    # the current_month data node entity is exposed as an attribute of the task
    current_month_data_node = task.current_month
