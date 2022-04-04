# Prepare your application for deployment

To be able to deploy a Taipy application - some options must be specified in the Service (`Gui` or `Rest`).

These options can be provided from the environment or hard coded.

Taipy is based on [Flask](https://flask.palletsprojects.com/) and allows customer to
access to it for customization.

## Options

- **port:** Binding port for your application. By default, Taipy used the port `5000`.
- **host:** Allows Taipy to listen to a public IP.
- Other Flask options: https://flask.palletsprojects.com/en/2.1.x/config/

## Example

In your Taipy application, you should have something that looks like:
```python
import taipy as tp

#
# Your code
#

rest = tp.Rest()
gui = tp.Gui(md=md)

tp.run(rest, gui, title="Taipy Demo")
```

To be able to run in the Heroku remote environment, you should update your _run_ method by adding
the _host_ and _port_ required by Heroku:
```python
import os
import taipy as tp

#
# Your code
#

rest = tp.Rest()
gui = tp.Gui(md=md)

tp.run(
    title="Taipy Demo",
    host='0.0.0.0',
    port=os.environ.get('PORT', '5000'),
)
```
