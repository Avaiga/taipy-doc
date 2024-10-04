import requests
import time
import logging
import os

BASIC_TIMEOUT = 60 * 15
INTERMEDIATE_TIMEOUT = 60

class WatsonStudio:
    def __init__(self, token, wml_endpoint, project_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        self.wml_endpoint = wml_endpoint
        self.project_id = project_id


    def start_job(self, job_id, payload):
        start_url = f"{self.wml_endpoint}/v2/jobs/{job_id}/runs?project_id={self.project_id}"
        data = {
                "job_run": {
                    "name": "Taipy integration",
                    "description": "Show Taipy integration",
                    "configuration": {
                        "env_variables": [
                            "param1=value1",
                            "param2=value2"
                        ]
                    }
                }
        }
        response = requests.post(start_url, json=data, headers=self.headers, timeout=3000).json()
        return response["metadata"]["asset_id"]

    def get_job_run_status(self, job_id, run_id):
        status_url = f"{self.wml_endpoint}/v2/jobs/{job_id}/runs/{run_id}?project_id={self.project_id}"
        response = requests.get(status_url, headers=self.headers, timeout=INTERMEDIATE_TIMEOUT).json()
        return response['entity']['job_run']['state']

    def get_job_run_results(self, job_id, run_id):
        results_url = f"{self.wml_endpoint}/v2/jobs/{job_id}/runs/{run_id}/logs?project_id={self.project_id}"
        response = requests.get(results_url, headers=self.headers, timeout=INTERMEDIATE_TIMEOUT).json()
        return response['results']

    def run_and_get_results(self, job_id, payload, timeout=BASIC_TIMEOUT):
        run_id = self.start_job(job_id, payload)

        for _ in range(timeout):
            status = self.get_job_run_status(job_id, run_id)
            if status.upper() not in ['STARTING', 'PENDING', 'RUNNING']:
                break
            else:
                time.sleep(1)

        results = self.get_job_run_results(job_id, run_id)
        return results

default_param = {"param1": "jobvalue1", "param2": "jobvalue2"}

# It can be find in your IBM Watson Studio URL
JOB_ID = os.environ["JOB_ID"]

def predict(parameters):
    wml = WatsonStudio(os.environ['WATSON_BEARER_TOKEN'],
                       os.environ['WATSON_ENDPOINT'],
                       os.environ['PROJECT_ID'])

    try:
        return wml.run_and_get_results(JOB_ID, parameters)
    except Exception as e:
        logging.info(f'Error during the Watson Studio call\n{e}')
        return None


# config.py
from taipy.common.config import Config

params_cfg = Config.configure_data_node("params", default_data={"param1": "value1", "param2": "value2"})

results_cfg = Config.configure_data_node("result")

task_databricks_cfg = Config.configure_task("watsonstudio",
                                            input=[params_cfg],
                                            function=predict,
                                            output=[results_cfg])

scenario_cfg = Config.configure_scenario("scenario", task_configs=[task_databricks_cfg])


# main.py
import taipy as tp

if __name__ == "__main__":
    tp.Orchestrator().run()

    scenario = tp.create_scenario(scenario_cfg)

    scenario.submit()
    print(scenario.result.read())
