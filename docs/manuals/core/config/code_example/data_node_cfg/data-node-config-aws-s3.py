#Upload and retrive raw data from existing s3 bucket
import taipy as tp
import boto3
from taipy import Config, Core, Gui


input_text = None
s3_result = None


page = """
message: <|{input_text}|input|>
<|submit|button|on_action=upload_scenario|>

Retrived : <|{s3_result}|text|>
"""



def get_s3_data(s3_object, s3_result):
    return f"Your S3 results:  {s3_result}"


def upload_scenario(state):
    state.scenario.input_text.write(state.input_text)
    state.scenario.my_s3_object.write(state.input_text)
    state.scenario.submit()
    state.s3_result = scenario.my_s3_object.read()


s3_object_cfg = Config.configure_s3_object_data_node(
    id="my_s3_object",
    aws_access_key="YOUR AWS ACCESS KEY",  # Can be passed as env variable as well
    aws_secret_access_key="YOUR AWS SECRET ACCESS KEY", # Can be passed as env variable as well
    aws_s3_bucket_name="YOUR AWS BUCKET Name", #Must be Already existing bucket
    aws_s3_object_key="taipy_object",
    aws_s3_object_parameters = {'CacheControl': 'max-age=86400'})

input_text_data_node_cfg = Config.configure_data_node(id="input_text")
s3_result_data_node_cfg = Config.configure_data_node(id="s3_result")
store_data_task_cfg = Config.configure_task("upload", get_s3_data, input=[s3_object_cfg,input_text_data_node_cfg], output=[s3_result_data_node_cfg])
scenario_cfg = Config.configure_scenario("scenario", task_configs=[store_data_task_cfg])

if __name__ == "__main__":

    Core().run()
    scenario = tp.create_scenario(scenario_cfg)
    Gui(page).run(debug=True)
