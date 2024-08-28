
# `on_change`: Variable Change

The `on_change` callback allows developers to react to changes in application variables. This callback can be triggered in two primary ways:

- **Through Visual Elements**: When a user interacts with a visual element (like a dropdown selector, input field, slider, etc.), the variable associated with that element changes. If no local callback (a callback attached directly to the visual element) hijacks this event, the global on_change callback will be triggered.

- **Through Direct Assignment**: The on_change callback can also be triggered when a variable is programmatically changed within the code using the state object. This allows for powerful, programmatic control over how your application responds to data changes.

## Use Case: Real-Time Data Filtering
In this example, we'll demonstrate how the on_change callback can be used to filter a list of items based on the user's input. The callback is triggered both by user interaction through a selector and by programmatic changes to the filtered_items variable.
```python
def on_change(state, var_name, var_value):
    if var_name == "category":
        items = {
            "Fruits": ["Apple", "Banana", "Cherry"],
            "Vegetables": ["Carrot", "Broccoli", "Spinach"],
            "Dairy": ["Milk", "Cheese", "Yogurt"]
        }
        state.filtered_items = items.get(state.category, [])
    if var_name == "filtered_items":
        notify(state, "info", f"Filtered items: {state.filtered_items}")

Gui(page="""
<|{category}|selector|lov=Fruits;Vegetables;Dairy|>
<|{filtered_items}|text|>
""").run()

```

## Example: Reactive UI Updates

Imagine an e-commerce application where the total price updates automatically when the quantity of items in the cart changes.

```python
def update_total(state, var_name, var_value):
    if var_name in ["item1_qty", "item2_qty"]:
        state.total_price = (state.item1_qty * state.item1_price) + (state.item2_qty * state.item2_price)

Gui(page="""
<|{item1_qty}|number|> x $<|{item1_price}|text|> 
<|{item2_qty}|number|> x $<|{item2_price}|text|> 
Total: $<|{total_price}|text|>
""").run()
```



# `on_init`: Initialize a State

The `on_init` callback is useful for setting up the initial state when a user connects to your application. It ensures that all necessary variables are properly initialized before any interaction occurs.

## Use Case: Database Refresh

Consider an application that requires the latest data from a database every time a user connects. For example, the application might display a dashboard with the most recent sales data, user statistics, or other dynamic content. The `on_init` callback can be used to refresh this data from the database each time a session starts.

### Example: Refreshing Sales Data

In this example, when a user connects, the application retrieves the most recent sales data from the database and stores it in the state. This data is then used to populate the dashboard with up-to-date information.

```python
def on_init(state):
    # Fetch the latest sales data from the database
    state.sales_data = get_latest_sales_data()
    
    # Log or notify the initialization status
    print(f"Sales data refreshed with {len(state.sales_data)} records")

    # Optionally, set other initial states
    state.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Data last updated at {state.last_updated}")

Gui(page="""
## Sales Dashboard

Last updated: <|{last_updated}|text|>

<|{sales_data}|table|>
""").run()
```


# **`on_action`: Handling User Interactions**

The `on_action` callback is invoked when users interact with UI elements like buttons, checkboxes, or any other actionable elements.

## **Use Case: Form Submission**

In a form, `on_action` can handle the submission process, validate the data, and then trigger an appropriate response (e.g., saving data, showing a confirmation message).

```python
def submit_form(state):
    if validate_form(state):
        save_to_database(state.form_data)
        state.message = "Form submitted successfully!"
    else:
        state.message = "Form contains errors. Please fix them."

Gui(page="""
<|Submit|button|on_action=submit_form|>
<|{message}|text|>
""").run()
```

## **Example: Interactive Menus**

`on_action` can also manage more complex interactions, such as navigating through a multi-step process or wizard.

```python
def next_step(state):
    state.current_step += 1

Gui(page="""
<|{current_step}|slider|>
<|Next|button|on_action=next_step|>
""").run()
```

# **`on_navigate`: Page Navigation**

The `on_navigate` callback provides control over what happens when a user navigates between pages. This can be useful for access control, dynamic content loading, or redirecting users.

## **Use Case: Access Control**

You can prevent users from accessing certain pages based on their roles or authentication status.

```python
def on_navigate(state, page_name):
    if not state.user_logged_in and page_name != "login":
        return "login"
    return page_name

Gui(page="""
<|Navigate to Dashboard|button|on_action=lambda state: Gui().go_to('dashboard')|>
""").run()
```

## **Example: Dynamic Content Loading**

Load content dynamically when navigating to a specific page, such as fetching data from an API.

```python
def on_navigate(state, page_name):
    if page_name == "profile":
        state.profile_data = fetch_user_profile(state.user_id)
    return page_name
```

# **`on_exception`: Exception Handling**

The `on_exception` callback allows you to gracefully handle errors that occur within your application, ensuring a better user experience.

## **Use Case: Logging and Notification**

When an exception occurs, log the error and notify the user with a friendly message.

```python
import logging

def on_exception(state, function_name, exception):
    logging.error(f"Error in {function_name}: {exception}")
    state.error_message = "An unexpected error occurred. Please try again later."

Gui(page="""
<|{error_message}|text|>
""").run()
```

## **Example: Fallback Mechanism**

You can implement a fallback mechanism that allows the application to recover from certain types of errors.

```python
def on_exception(state, function_name, exception):
    if isinstance(exception, ConnectionError):
        state.error_message = "Network issue, retrying..."
        retry_connection()
    else:
        state.error_message = "An unexpected error occurred."

Gui(page="""
<|{error_message}|text|>
""").run()
```

# Local Callbacks

### **`on_change` and `on_action` for Visual Elements**

Local callbacks are tied to specific UI controls, providing fine-grained control over user interactions.

#### **`on_change` Example**

```python
def update_celsius(state):
    state.temperature_celsius = (state.temperature_fahrenheit - 32) * 5/9

Gui(page="""<|{temperature_fahrenheit}|slider|on_change=update_celsius|>""").run()
```

#### **`on_action` Example**

```python
def submit_form(state):
    print(f"Form submitted with name: {state.name}")

Gui(page="""<|Submit|button|on_action=submit_form|>""").run()
```
