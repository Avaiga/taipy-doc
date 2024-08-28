# Scheduler

!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

This documentation focuses on providing necessary information to use the
Taipy `Scheduler^`, and in particular the capabilities related to scenario
management and job execution.

Let’s assume also that the configuration used in the examples in this section is
implemented in the module <a href="./code-example/my_config.py" download>`my_config.py`</a>.

=== "Module my_config.py"

    ```python linenums="1"
    {%
    include-markdown "./code-example/my_config.py"
    comments=false
    %}
    ```

The code below is an example of how to use the Taipy `Scheduler^` to schedule a method to run every 10 seconds
in a Taipy application.

=== "Module main.py"

    ```python linenums="1"
    {%
    include-markdown "./code-example/scheduler_example.py"
    comments=false
    %}
    ```

## Start/Stop the scheduler

To make the scheduler execute the scheduled methods, you must first
start the scheduler by using the `start()` method.

```python
import taipy as tp

if __name__ == "__main__":
    tp.Scheduler.start()
```

Once the scheduler is started, the scheduled methods will run in the
background at their specified times. While the scheduler is running, you
can execute other methods without being blocked by the scheduler.

!!! info "Schedule a method before and after starting the scheduler"

    You can schedule a method both before and after starting the scheduler.
    However, keep in mind that the scheduled method will not run until the
    scheduler is started.

By default, the scheduler checks for methods to run every 60 seconds. You can change the interval
by providing the `interval` parameter to the `start()` method.

```python
import taipy as tp

if __name__ == "__main__":
    tp.Scheduler.start(interval=1)
```

It is intended behavior that the scheduler does not run missed methods.
For example, if you've registered a method that should run every second and you set the
interval of the scheduler to one hour, your method won't be run 60 time at each interval but only once.

!!! warning "Scheduler with a short interval"
    If you set the interval to a very short time, the CPU usage of the scheduler will increase.
    It is recommended to set the interval to a reasonable value based on the frequency of the scheduled methods.

To stop the scheduler from running the scheduled methods, you can use the
`stop()` method.

```python
    tp.Scheduler.stop()
```

## Run a method every specific time period

Taipy `Scheduler^` provides the capability to run a method every specific period.
The period can be specified in seconds, minutes, hours, days, weeks, days, months or years.

!!! info "Schedule a method every second"
    If a method is scheduled to run every second, the scheduler must be started with an interval of 1 second or lower.

    If the scheduler is started with the default interval of 60 seconds or higher than the period of the scheduled method, the method will not run every second but only every interval of the scheduler.


```python linenums="1"
import taipy as tp
from my_config import scenario_cfg

if __name__ == "__main__":
    monthly_scenario = tp.create_scenario(scenario_cfg)

    # Submit a scenario every 3 second/minute/hour/day
    # Starting 3 second/minute/hour/day from now
    tp.Scheduler.every(3).seconds.do(tp.submit, monthly_scenario)
    tp.Scheduler.every(3).minutes.do(tp.submit, monthly_scenario)
    tp.Scheduler.every(3).hours.do(tp.submit, monthly_scenario)
    tp.Scheduler.every(3).days.do(tp.submit, monthly_scenario)

    # Submit a scenario every 1 week/month/year
    # Starting 1 week/month/year from now
    tp.Scheduler.every().weeks.do(tp.submit, monthly_scenario)
    tp.Scheduler.every().months.do(tp.submit, monthly_scenario)
    tp.Scheduler.every().years.do(tp.submit, monthly_scenario)

    tp.Scheduler.start()
```

In the above example, we schedule the `tp.submit(monthly_scenario)` method with different periods.
Notice that we chose to submit a scenario as an example, but any Python method can be scheduled.

- First, we need to call the `every()` method and provide the time period.
  If not provided, the default period is 1.
- Secondly, the time unit needs to be provided, which can be either
  `seconds`, `minutes`, `hours`, `days`, `weeks`, `months`, or `years`.
- Finally, we provide the `do()` method with the method to schedule and its parameters.
  In the example, we schedule the `tp.submit()` method, and provide `monthly_scenario` as the parameter.

Once scheduled, the method will run in the background. The first run will be:

- the number of period from the scheduled time, or
- at the start of the scheduler if the scheduler is started **after** the time that the method supposed to run.

## Run a method at a specific time and/or date

To schedule a method to run at a specific time, you can call the `at()` and `on()` methods after providing the time unit.

The `at()` method allows specifying the time to run the method, which accepts the following parameters:

- ***time_str*** is a madatory `datetime.time` object, `datetime.datetime` object, or a string.
  If it's a `datetime.time` or `datetime.datetime` object:

  - For daily scheduled methods, the hour, minute, and second will be used.
  - For hourly scheduled methods, the minute and second will be used.
  - For minute scheduled methods, only the second will be used.

 If a string, it must be in one of the following formats:

  - For daily scheduled methods -> "HH:MM:SS" or "HH:MM"
  - For hourly scheduled methods -> "MM:SS" or ":MM"
  - For minute scheduled methods -> ":SS"
- ***tz*** is the timezone that this timestamp refers to. Can be a string that can be parsed by
  pytz.timezone(), or a pytz.BaseTzInfo object.

The `on()` method allows specifying the date to run the method, which only applies to monthly and
yearly scheduled methods. The `on()` method requires the following parameter:

- ***date*** is a madatory `datetime.date` object, `datetime.datetime` object, or a string.
  If it's a `datetime.date` or `datetime.datetime` object:

  - For monthly scheduled methods, only the day will be used.
  - For yearly scheduled methods, the month and day will be used.

  If a string, it must be in one of the following formats:

  - For monthly scheduled methods -> "DD".
  - For yearly scheduled methods -> "MM-DD". The month can be a number or the name of the month in English
    (e.g. "January" or "Jan").
  The day string can be a number representing the day of the month, or a negative number representing
  the number of days from the end of the month. For example, -1 represents the last day of the month.


```python linenums="1"
import taipy as tp
from my_config import scenario_cfg

if __name__ == "__main__":
    monthly_scenario = tp.create_scenario(scenario_cfg)

    # Submit a scenario every minute at the 23rd second
    tp.Scheduler.every().minute.at(":23").do(tp.submit, monthly_scenario)

    # Submit a scenario every hour at the 42nd minute
    tp.Scheduler.every().hour.at(":42").do(tp.submit, monthly_scenario)

    # Submit a scenario every 5th hour, 20 minutes and 30 seconds in.
    # If current time is 02:00, first execution is at 06:20:30
    tp.Scheduler.every(5).hours.at("20:30").do(tp.submit, monthly_scenario)

    # Submit a scenario every day at specific HH:MM and next HH:MM:SS
    tp.Scheduler.every().day.at("10:30").do(tp.submit, monthly_scenario)
    tp.Scheduler.every().day.at("12:42:30", "Europe/Amsterdam").do(tp.submit, monthly_scenario)

    # Submit a scenario on a specific day of the week
    tp.Scheduler.every().monday.do(tp.submit, monthly_scenario)
    tp.Scheduler.every().wednesday.at("13:15").do(tp.submit, monthly_scenario)

    # Submit a scenario on the 15th of every month
    tp.Scheduler.every().months.at("13:15").on("15").do(tp.submit, monthly_scenario)
    # Submit a scenario on the last day every 2 months
    tp.Scheduler.every(2).months.at("13:15").on("-1").do(tp.submit, monthly_scenario)

    # Submit a scenario on January 3rd every year on Amsterdam timezone
    tp.Scheduler.every().years.at("13:15", "Europe/Amsterdam").on("jan 03").do(tp.submit, monthly_scenario)
    # Submit a scenario on the last day of February every year
    tp.Scheduler.every().years.at("13:15").on("feb -1").do(tp.submit, monthly_scenario)

    tp.Scheduler.start()
```

Once scheduled, the first run of the method is based on the current time and the time specified in the `at()` API.
For example, assume that the current time is 12:00:00:
- If the `tp.submit(monthly_scenario)` is scheduled to run every day at "10:30", the first run will be at 10:30:00 tomorrow.
- If the `tp.submit(monthly_scenario)` is scheduled to run every day at "12:42:30", the first run will be at 12:42:30 today, which is in 42 minutes.

## Run a scheduled method until a certain time

To automatically cancel a scheduled method after a certain time, you can use the `until()` method.
The `until()` method accepts a time indicator, which can be:

- `datetime.datetime` object,
- `datetime.time` object,
- `datetime.timedelta` object,
- or a string in one of the following formats: "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d",
  "%H:%M:%S", "%H:%M".

If only a time is provided, the date is set to today.

```python linenums="1"
from datetime import datetime, timedelta, time
import taipy as tp
from my_config import scenario_cfg

if __name__ == "__main__":
    monthly_scenario = tp.create_scenario(scenario_cfg)

    # Submit a scenario until a 18:30 today
    tp.Scheduler.every(1).hours.until("18:30").do(tp.submit, monthly_scenario)

    # Submit a scenario until a 2030-01-01 18:33
    tp.Scheduler.every(1).hours.until("2030-01-01 18:33").do(tp.submit, monthly_scenario)

    # Submit a scenario until today 11:33:42
    tp.Scheduler.every(1).hours.until(time(11, 33, 42)).do(tp.submit, monthly_scenario)

    # Submit a scenario for every hour until the next 8 hours
    tp.Scheduler.every(1).hours.until(timedelta(hours=8)).do(tp.submit, monthly_scenario)

    # Submit a scenario until a specific datetime
    tp.Scheduler.every(1).months.until(datetime(2030, 1, 1, 12, 30, 0)).do(tp.submit, monthly_scenario)
```

## Get all scheduled methods

To retrieve all scheduled methods from the scheduler, use `tp.Scheduler.get_scheduled_methods()` method.

```python linenums="1"
import taipy as tp
from my_config import scenario_cfg

if __name__ == "__main__":
    monthly_scenario = tp.create_scenario(scenario_cfg)

    tp.Scheduler.every().second.do(tp.submit, monthly_scenario)

    all_scheduled_methods = tp.Scheduler.get_scheduled_methods()
```

The `tp.Scheduler.get_scheduled_methods()` method returns a list of `ScheduledMethod^` objects, which you can use to
get information or cancel the scheduled method.

## Cancel scheduled methods

To remove a scheduled method from the scheduler, use the `tp.Scheduler.cancel_scheduled_method(scheduled_method)` method.

```python linenums="1"
import taipy as tp
from my_config import scenario_cfg

if __name__ == "__main__":
    monthly_scenario = tp.create_scenario(scenario_cfg)

    monthly_submit_method = tp.Scheduler.every().second.do(tp.submit, monthly_scenario)

    tp.Scheduler.cancel_scheduled_method(monthly_submit_method)
```

To remove all scheduled methods from the scheduler, use `tp.Scheduler.clear()`

```python linenums="1"
import taipy as tp
from my_config import scenario_cfg

if __name__ == "__main__":
    monthly_scenario = tp.create_scenario(scenario_cfg)

    tp.Scheduler.every().second.do(tp.submit, monthly_scenario)

    tp.Scheduler.clear()
```

## Shortcut for scheduling most used Taipy methods

Taipy `Scheduler^` provides shortcut for scheduling popular Taipy methods, including:

- `taipy.create_scenario()`
- `taipy.submit()`
- A combination of `taipy.create_scenario()` and `taipy.submit()`

Instead of using the `do()` method and specifying the Taipy method to schedule, you can directly call the following method from the scheduler.

```python linenums="1"
import taipy as tp
from my_config import scenario_cfg

if __name__ == "__main__":
    # Creating a new scenario every month using the scenario_cfg
    tp.Scheduler.every().months.do_create(scenario_cfg)

    # Submit the monthly_scenario every month
    monthly_scenario = tp.create_scenario(scenario_cfg)
    monthly_submit_method = tp.Scheduler.every().months.do_submit(monthly_scenario)

    # Create a new scenario every month using the scenario_cfg
    # and submit it immediately
    tp.Scheduler.every().months.do_create_and_submit_scenario(scenario_cfg)

    tp.Scheduler.clear()
```
