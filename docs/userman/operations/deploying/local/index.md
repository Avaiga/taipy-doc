Deploying your Taipy application on your local machine is an occasional
use case that can be considered if you want to temporarily expose an
application for remote users over the Internet.

An easy path to follow is to use [Ngrok](https://ngrok.com/), which can
open access to remote systems without having to reconfigure the network
settings. It provides a way to expose your local application to the public
Internet. This allows anyone to access your application before deploying it
in your production environment.

# Install Ngrok

Install the `pyngrok` package in your Python environment:

When installing Taipy GUI:
```
$ pip install taipy-gui[pyngrok]
```
or independently:
```
$ pip install pyngrok
```

# Create a Ngrok account

Create an account on the [Ngrok web site](https://ngrok.com/). That drives you
to a page where you can install the *ngrok* executable on your machine. Behind
the scene, Ngrok also sends you a confirmation email providing a link that you
must click to validate the registration and connect to your new account.

Connecting to your account provides you the Ngrok *authtoken*.

# Pass the Ngrok token to the application

Add the NGrok *authtoken* to the call to `(Gui.)run()^`:

```python
...
gui=Gui(...)
...
gui.run(ngrok_token="<ngrok_authtoken>")
...
```

When you run your Taipy script, the console prints out the public URL,
allowing users to connect to it. This has the form `http://<id>.ngrok.io`.

Your Flask server, running locally, will accept and serve connections from all
around the world.

