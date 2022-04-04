# Prepare your application for deployment

To be able to deploy a Taipy application you should specify some options for your Service (`Gui` or `Rest`).

These options can be provided from the environment or hard-coded.
Taipy is based on [Flask](https://flask.palletsprojects.com/) and allows customer to
access the Flask application so it can be customized.

## Options

- **port**: Binding port for your application. By default, Taipy uses the port 5000.
- **host**: IP address that the application listens to.
- Other Flask options: See the [Flash configuration](https://flask.palletsprojects.com/en/2.1.x/config/) page.

## Example

In your Taipy application, you should have something that looks like:
```python
import taipy as tp

#
# Your code
#

rest = tp.Rest()
gui = tp.Gui(...)

tp.run(rest, gui, title="Taipy Demo")
```

To run on an Heroku remote environment, you must add the host and port parameters to
the `(taipy.)run()^` function, as required by Heroku:
```python
import os
import taipy as tp

#
# Your code
#

rest = tp.Rest()
gui = tp.Gui(...)

tp.run(
    title="Taipy Demo",
    host='0.0.0.0',
    port=os.environ.get('PORT', '5000'),
)
```
