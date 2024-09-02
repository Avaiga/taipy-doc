In a typical web application, user actions often trigger server-side functions that can take considerable time to complete. For example, consider a scenario where a user requests a complex data analysis that could take several minutes. If the server processes this task synchronously (i.e., on the main thread), the application can become unresponsive, leaving the user without feedback until the task is done. This frustrates users and increases the risk of communication timeouts, leading to incomplete tasks or errors.

[View Example Code](./src/long_callbacks.py){: .tp-btn target='blank'}

To address this challenge, Taipy provides a feature known as "long-running callbacks." This feature enables the server to handle resource-intensive processes in the background while keeping the user interface responsive.

# Running Functions in the Background

Imagine a scenario where a callback initiates a task requiring significant resources and time. Taipy allows you to manage this easily with a straightforward approach:

```python
from taipy.gui import State, invoke_long_callback, notify

def heavy_function(...):
    # Perform resource-intensive operations
    ...

def on_action(state):
    notify(state, "info", "Heavy function started")
    invoke_long_callback(state, heavy_function, [...heavy_function arguments...])
```

### Key Components:

- **`invoke_long_callback()`**: This function is central to implementing asynchronous callbacks in Taipy. It runs `heavy_function` in a separate thread, ensuring the main application remains responsive.
- **`notify()`**: This function sends messages to the user interface, informing the user about the task's progress. This example notifies the user that the heavy task has started.

In the example above, the `invoke_long_callback()` function in Taipy manages the resource-intensive task by running it in a background thread. This allows the application to remain interactive, even as the heavy function executes. The `on_action()` function is triggered by a user action, such as clicking a button.

## Example 1: Basic Asynchronous Callback

Let's explore a simple example where a button click initiates a long-running task that runs asynchronously, allowing the user to continue interacting with the application.

### Code Example:

```python
from taipy.gui import Gui, State, invoke_long_callback, notify

def heavy_function():
    # Simulate a time-consuming task
    import time
    time.sleep(10)  # Sleep for 10 seconds

def on_action(state):
    notify(state, "info", "Heavy task started...")
    invoke_long_callback(state, heavy_function)

if __name__ == "__main__":
    gui = Gui("<|Start Task|button|on_action=on_action|>")
    gui.run()
```

### How It Works:

- **`heavy_function()`** simulates a long-running task by pausing for 10 seconds.
- When the user clicks the "Start Task" button, **`on_action()`** is triggered. It sends a notification and starts `heavy_function` asynchronously using `invoke_long_callback()`.

### Result:

The user interface immediately informs the user that the task has started, and the application remains responsive while `heavy_function` runs in the background.

## Example 2: Updating the UI After Task Completion

In many cases, you'll want to update the user interface based on whether the task completed successfully or encountered an error.

### Code Example:

```python
from taipy.gui import Gui, State, invoke_long_callback, notify

def heavy_function():
    # Simulate a time-consuming task
    import time
    time.sleep(10)  # Sleep for 10 seconds
    return True  # Simulate success

def heavy_function_status(state, status):
    if status:
        notify(state, "success", "Task completed successfully!")
    else:
        notify(state, "error", "Task failed.")

def on_action(state):
    notify(state, "info", "Heavy task started...")
    invoke_long_callback(state, heavy_function, status_callback=heavy_function_status)

if __name__ == "__main__":
    gui = Gui("<|Start Task|button|on_action=on_action|>")
    gui.run()
```

### How It Works:

- **`heavy_function()`** simulates a successful task by returning `True`.
- **`heavy_function_status()`** is a callback function that updates the user interface after `heavy_function` completes, indicating success or failure.
- **`invoke_long_callback()`** now includes a `status_callback` parameter, specifying the function to call upon task completion.

### Result:

After `heavy_function` finishes, the user interface updates to indicate whether the task succeeded or failed.

## Regular Progress Updates

In scenarios where regular updates are needed during a long-running task, Taipy allows you to specify time intervals for these updates.

### Code Example:

```python
from taipy.gui import Gui, State, invoke_long_callback, notify

def heavy_function():
    # Simulate a time-consuming task
    import time
    for _ in range(10):
        time.sleep(1)  # Sleep for 1 second

def heavy_function_status(state, status):
    if isinstance(status, bool):
        if status:
            notify(state, "success", "Task completed successfully!")
        else:
            notify(state, "error", "Task failed.")
    else:
        notify(state, "info", f"Task is still running... {status}s elapsed")

def on_action(state):
    notify(state, "info", "Heavy task started...")
    invoke_long_callback(state, heavy_function, status_callback=heavy_function_status, period=1000)

if __name__ == "__main__":
    gui = Gui("<|Start Task|button|on_action=on_action|>")
    gui.run()
```

### How It Works:

- **`heavy_function()`** simulates ongoing work by running a loop that sleeps for 1 second at a time.
- **`heavy_function_status()`** updates the user interface with progress information or final status.
- **`invoke_long_callback()`** is called with a `period` parameter, specifying that `heavy_function_status()` should be called every second.

### Result:

The user interface is regularly updated with the task's progress, keeping users informed in real-time.


## Tracking Function Progress

In some cases, it may be beneficial to trigger updates directly from within the `heavy_function`. This can be done using `invoke_callback` to send updates to the client during task execution.

For example:

```python
{%
include-markdown "./src/trigger_update.py"
comments=false
%}
```

In this example, `heavy_function` uses `invoke_callback` to send progress updates to `user_status` at different stages. The `user_status` function appends these updates to the `logs` state variable, which is then displayed in the user interface.

### Key Components:
1. **`heavy_function`**: Calls `invoke_callback` at various stages to send progress updates.
2. **`user_status`**: Updates the `logs` state variable with progress information.
3. **`status_fct`**: Updates the `result` state variable with the final result of `heavy_function`.
4. **`respond`**: Initiates the long-running task by calling `invoke_long_callback` with `heavy_function` and associated status functions.

By using this approach, you can provide real-time updates directly from within `heavy_function`, keeping users informed about the progress of long-running tasks and enhancing their overall experience.


## Advanced Usage: Manual Thread Management

While `invoke_long_callback()` is convenient, there are situations where you might need more control over the execution of long-running tasks. In such cases, you can manually create and manage threads.

### Code Example:

```python
from taipy.gui import Gui, State, get_state_id, notify
from threading import Thread

def heavy_function():
    # Simulate a time-consuming task
    import time
    time.sleep(10)  # Sleep for 10 seconds

def heavy_function_done(state: State):
    notify(state, "info", "Heavy task completed!")

def heavy_function_in_thread(state_id: str):
    heavy_function()
    invoke_callback(gui, state_id, heavy_function_done)

def on_action(state: State):
    notify(state, "info", "Heavy task started...")
    thread = Thread(target=heavy_function_in_thread, args=(get_state_id(state),))
    thread.start()

if __name__ == "__main__":
    gui = Gui("<|Start Task|button|on_action=on_action|>")
    gui.run()
```

### How It Works:

- **`heavy_function_in_thread()`** runs `heavy_function` in a separate thread.
- After `heavy_function` completes, **`heavy_function_done()`** is called using `invoke_callback()`, which updates the user interface.
- **`on_action()`** starts the new thread manually, providing complete control over the execution.

### Result:

This approach gives you finer control over task execution and the application’s response upon completion, useful in more complex scenarios.

## Handling Function Results

To update the application state with the result of `heavy_function()`, modify `heavy_function_status()` as follows:

```python
def heavy_function_status(state, status, result):
    if status:
        notify(state, "success", "The heavy function has finished!")
        # Update the State with the function result
        state.result = result
    else:
        notify(state, "error", "The heavy function has failed")
```

Ensure that `heavy_function()` returns a value:

```python
def heavy_function(...):
    ...
    return result
```

By updating the state with the result of `heavy_function()`, you can display the outcome to the user or use it in other parts of your application, enhancing the user experience.