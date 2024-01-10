# functions.py
import requests
import time
import logging
import os

BASIC_TIMEOUT = 60 * 15
INTERMEDIATE_TIMEOUT = 60
CLUSTER_NAME = "cluster_name"

class Databricks:
    def __init__(self, token, databricks_endpoint, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = {
            'Authorization': f'Bearer {token}'
        }
        self.databricks_endpoint = f'https://{databricks_endpoint}/api/2.0'

    @property
    def cluster_id(self) -> str:
        clusters = requests.get(f"{self.databricks_endpoint}/clusters/list", headers=self.headers,
                                timeout=INTERMEDIATE_TIMEOUT).json()
        clusters = filter(lambda c: c.get('cluster_name') == CLUSTER_NAME, clusters.get('clusters', []))
        return next(clusters, {}).get('cluster_id')

    def status(self):
        try:
            status = requests.get(f"{self.databricks_endpoint}/clusters/get", headers=self.headers,
                                  json={"cluster_id": self.cluster_id}, timeout=INTERMEDIATE_TIMEOUT).json()
            cluster_state = status.get('state')

            if cluster_state == 'RUNNING':
                return 'Running'
            if cluster_state == 'TERMINATED':
                requests.post(f"{self.databricks_endpoint}/clusters/start", headers=self.headers,
                             json={"cluster_id": self.cluster_id}, timeout=INTERMEDIATE_TIMEOUT)
                return 'Not Started'
            if cluster_state == 'PENDING':
                return 'Starting'
            return cluster_state
        except:
            return "Error when connecting to the DataBricks Cluster"

    def run_and_get_results (self, endpoint, dataset=None, timeout=BASIC_TIMEOUT):
        """
        Call a Databricks jobs base on the endpoint, wait the end of the job and return the result
        The timeout is approximate
        """
        dataset = dataset or {}
        predict_url = f"{self.databricks_endpoint}/jobs/run-now"
        data = {
            "job_id": self._get_job(endpoint),
            "notebook_params": dataset
        }

        try:
            run_id = requests.post(predict_url, json=data,
                                headers=self.headers,
                                timeout=INTERMEDIATE_TIMEOUT).json()
            run_id = run_id['run_id']
            logging.info(run_id)
        except:
            logging.info(run_id)
        
        job_url = f'{self.databricks_endpoint}/jobs/runs/get?run_id={run_id}'

        for _ in range(timeout):
            status = requests.get(job_url, headers=self.headers, timeout=INTERMEDIATE_TIMEOUT)\
                .json()
            status = status.get('state').get('life_cycle_state')
            print(status)
            if status.upper() != 'PENDING' and status.upper() != 'RUNNING' and status.upper() != 'TERMINATING':
                break
            else:
                time.sleep(1)

        output_url = f"{self.databricks_endpoint}/jobs/runs/get-output?run_id=" + \
            str(run_id)
        r = requests.get(output_url, headers=self.headers, timeout=INTERMEDIATE_TIMEOUT).json().get('notebook_output').get('result')
        return r

    def _get_job(self, job_name_search):
        for job_id, job_name in self._list_jobs():
            if job_name == job_name_search:
                return job_id
        raise RuntimeError(f'Job name {job_name_search} not found')

    def _list_jobs(self):
        list_jobs_url = f"{self.databricks_endpoint}/jobs/list"
        jobs = requests.get(list_jobs_url, headers=self.headers).json()
        print(jobs)
        jobs = jobs['jobs']
        for job in jobs:
            yield job['job_id'], job['settings']['name']


default_param = {"param1": "value1", "param2": "value2"}

ENDPOINT = "job_endpoint"

def predict(parameters):
    databricks = Databricks(os.environ['DatabricksBearerToken'],
                            os.environ['DatabricksEndpoint'])

    try:
        return databricks.run_and_get_results(ENDPOINT, parameters)
    except Exception as e:
        try:
            logging.info("Taipy tries predict a second time")
            return databricks.run_and_get_results(ENDPOINT, parameters)
        except Exception as e:
            logging.info(f'Error during the databricks call\n{e}')
            return None


# config.py
from taipy.config import Config

params_cfg = Config.configure_data_node("params", default_data={"param1": "value1", "param2": "value2"})

results_cfg = Config.configure_data_node("result")

task_databricks_cfg = Config.configure_task("databricks",
                                            input=[params_cfg],
                                            function=predict,
                                            output=[results_cfg])

scenario_cfg = Config.configure_scenario("scenario", task_configs=[task_databricks_cfg])


# main.py
import taipy as tp 

if __name__ == "__main__":
    tp.Core().run()

    scenario = tp.create_scenario(scenario_cfg)

    scenario.submit()
    print(scenario.result.read())
