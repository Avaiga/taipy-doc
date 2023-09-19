> You can download the code of this step [here](../src/step_04.py) or all the steps [here](https://github.com/Avaiga/taipy-getting-started/tree/develop/src).

!!! warning "For Notebooks"

    The "Getting Started" Notebook is available [here](https://docs.taipy.io/en/latest/getting_started/getting-started/getting_started.ipynb).

# Step 4: Pipeline Management

In Step 3, you have described your graph; let's implement it with Taipy! 

## Pipeline configuration

To configure your first pipeline, you need to list all the tasks you want to be done by the pipeline. This pipeline executes the cleaning (*clean_data_task*) and the predicting (*predict_baseline_task*). Note that the **task_configs** is a list, so you don't have to worry about the order of the tasks. Taipy does that for you and optimizes its execution.

```python
# Create the first pipeline configuration
baseline_pipeline_cfg = Config.configure_pipeline(id="baseline",
                                                  task_configs=[clean_data_task_cfg, predict_baseline_task_cfg])
```

## Pipeline creation and execution

First of all, Taipy has to be run (tp.Core().run()). It will create a service that will act as a job scheduler. Then, create your pipeline from its configuration, submit it, and print the "predictions" Data Node results.

```python
import taipy as tp

# Run of the Taipy Core service
tp.Core().run()

# Create the pipeline
baseline_pipeline = tp.create_pipeline(baseline_pipeline_cfg)
# Submit the pipeline (Execution)
tp.submit(baseline_pipeline)
    
# Read output data from the pipeline
baseline_predictions = baseline_pipeline.predictions.read()
print("Predictions of baseline algorithm\n", baseline_predictions)
```

> Note that when creating the pipeline (`tp.create_pipeline()`), all associated Taipy objects of the pipeline (Data nodes, Tasks, etc) get automatically created (unless already present).
