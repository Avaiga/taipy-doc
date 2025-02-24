!!! note "Available in Taipy Enterprise edition"

    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise).

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

During the development process of a Taipy application, adding a login page is a common requirement for the user to authenticate and access the application.

To reduce the development time, Taipy provides a login page template, which is designed as a best practice page for authenticating in a Taipy application.

<figure>
  <img src="../img/login_template_dark.jpeg" class="visible-dark" />
  <img src="../img/login_template_light.jpeg" class="visible-light"/>
  <figcaption>Out-of-the-box Taipy login page</figcaption>
</figure>

Out-of-the-box, the login page provides a login form that allows the user to enter their credentials and authenticate to access the application.

# How to create a page

To create a page from the login template, change to the folder of the application in
which you want to create the page and run `taipy create --page login` from the CLI. Then
answer a few questions to customize your page.

```console
$ taipy create --page login
  [1/2] Page name (login_page):
  [2/2] Page folder (pages):

The new Taipy login page has been created at pages/login_page
Please import the new login page in your main application to use it.
```

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the page. The following
sections describe each question in detail.

1. Page name

- Specifies the name of the page.
- The default value is "login_page".

2. Page folder

- Specifies the path of the folder that contains the generated page.
- The path is relative to the current working directory. The folder will be created if not exist.
- The default value is "pages".

# Page description

The generated page has the following folder structure:

```plaintext
pages/
├──── login_page/
│   ├──── __init__.py
│   └──── login.py
│
└──── __init__.py
```

Your page's folder structure may vary depending on the answers you provided during the
creation process. Here is a brief overview of the key components:

- `pages/`: The folder that contains the page specified in the second question.
    - `login_page/login.py` contains the login form. It includes a [login](../../refmans/gui/viselements/generic/login.md) control.
    - `\_\_init\_\_.py` is the file that imports the newly created page in the `pages` package.

# Customizing the page

Everything in the generated page can be updated to precisely fit your specific requirements.

The login form can be customized via the [`login`](../../refmans/gui/viselements/generic/login.md)
visual element.

Out-of-the-box, pressing the "Login" button will trigger the *on_login()* function. You can modify
the definition of this function to handle the authentication logic, such as checking the user's credentials
and redirecting the user to the appropriate page based on the authentication result.

```python title="login.py"
import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import navigate, notify


def on_login(state, id, login_args):
    state.username, password = login_args["args"][:2]

    if state.username is None or password is None:  # The user canceled the login request
        notify(state, "error", "Login canceled!")
        state.username = "Guess"
        navigate(state, "", force=True)
        return

    try:
        state.credentials = tp.enterprise.gui.login(state, state.username, password)
        navigate(state, state.current_page, force=True)
    except Exception:
        notify(state, "error", "Login failed!")
        state.username = "Guess"
        navigate(state, "login", force=True)


with tgb.Page() as login_page:
    tgb.login("Login", on_action=on_login)
```

In the example above, when the "Login" button is pressed:

- If the user cancels the login request, a notification is displayed, and the user is redirected
    to the root page.
- If the user enters the wrong credentials, a notification is displayed, and the user is redirected
    to the login page.
- If the user enters the correct credentials, the user is authenticated, and the user is redirected
    to the current page.

You can also add more content to the page such as descriptions, or other
[visual elements](../../refmans/gui/viselements/index.md) provided by Taipy to enrich the
user experience.

# How to use the page

To use the login page in your application, import the page in the main application file along with
other pages and add it to the page list given to the `Gui^` service.

For more details on Taipy authentication, please refer to
[Authentication](../../userman/advanced_features/auth/authentication.md).

```python title="main.py"
from taipy import Config, Gui
from pages import root_page, login_page

roles = {
    "admin": ["TAIPY_ADMIN"],
    "user_1": ["TAIPY_READER"],
    "user_2": ["TAIPY_EXECUTOR"],
}

Config.configure_authentication("taipy", passwords=passwords, roles=roles)

pages = {
    "/": root_page,
    "login": login_page,
}

if __name__ == "__main__":
    gui = Gui(pages=pages)
    gui.run()
```
