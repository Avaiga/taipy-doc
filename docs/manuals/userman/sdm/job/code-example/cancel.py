from time import sleep

def double(nb):
    sleep(5)
    return nb * 2

if __name__ == "__main__":
    import taipy as tp
    from taipy import Config

    print(f'(1) Number of jobs: {len(tp.get_jobs())}.')

    # Create a scenario configuration with 2 sequential tasks.
    input_data_node_cfg = Config.configure_data_node("my_input", default_data=21)
    output_data_node_cfg = Config.configure_data_node("my_output")
    double_task_cfg = Config.configure_task("double_task", double, input_data_node_cfg, output_data_node_cfg)
    print_task_cfg = Config.configure_task("print_task", print, output_data_node_cfg)
    scenario_config = Config.configure_scenario("my_scenario", [double_task_cfg, print_task_cfg])

    # Run the core service.
    tp.Core().run()

    # Create a scenario and submit it.
    scenario = tp.create_scenario(scenario_config)
    submission = tp.submit(scenario)

    # Count and get the jobs.
    print(f'(2) Number of jobs: {len(tp.get_jobs())}.')
    job_double = tp.get_latest_job(scenario.double_task)
    job_print = tp.get_latest_job(scenario.print_task)

    # Get status of the job.
    print(f'(3) Status of job double_task: {job_double.status}')
    print(f'(4) Status of job print_task: {job_print.status}')

    # Then cancel the second job from print_task.
    tp.cancel_job(job_print)

    sleep(10)

    print(f'(5) Status of job double_task: {job_double.status}')
    print(f'(6) Status of job print_task: {job_print.status}')
