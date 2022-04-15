import taipy as tp

from step_03 import Config, clean_data_task_cfg, predict_baseline_task_cfg, dt

# Create the first scenario configuration
baseline_pipeline_cfg = Config.configure_pipeline(id="baseline",
                                                  task_configs=[clean_data_task_cfg, predict_baseline_task_cfg])

## Execute the "baseline" pipeline
if __name__ == "__main__":
    # Create the pipeline
    baseline_pipeline = tp.create_pipeline(baseline_pipeline_cfg)
    # Submit the pipeline (Execution)
    tp.submit(baseline_pipeline)

    # Read output data from the pipeline
    baseline_predictions = baseline_pipeline.predictions.read()
    print("Predictions of baseline algorithm\n", baseline_predictions)
