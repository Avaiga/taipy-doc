!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

Authentication is the process that makes sure a given user exists and
that the password provided when logging in matches the expected
one. This process ensures that a user that logs in really is who she or
he claims to be.

In Taipy Enterprise, the authentication process is achieve by the
`Authenticator^` class and indirectly by the `(auth.)login()^` function:
this function creates and returns a `Credentials^` object that
represents the user in the application.</br>
The returned `Credentials^` instance contains the set of roles assigned to
the user in the authentication system.

The programmer can create an authenticator manually (see the
`Authenticator.__init__^`(`Authenticator` constructor) for more information)
if the kind of authenticator needed by the application is known
(that is, what authentication protocol the application plans to rely on). The
programmer can alternatively use the `(auth.)login()^` function that will create
an `Authenticator^` the first time it is invoked.

Each kind of `Authenticator^` implements an *authentication protocol* that provides
services that allows for creating credentials and retrieve the roles associated
to a user.

Taipy Enterprise edition supports three authentication protocols:

   - "none": The *None* authenticator does not check the user password in
      `(auth.)login()^` and always validates the login process by creating a `Credentials^`
      instance that holds an empty role set.<br/>
      See the [*None* Authenticator](#none-authenticator) below for more information.

   - "Taipy": The *Taipy* authenticator makes sure users actually are declared, can
     retrieve role sets for those users and can check passwords if required.<br/>
     See the [Taipy Authenticator](#taipy-authenticator) below for more information.

   - "LDAP": The *LDAP* authenticator is an implementation of the LDAP protocol. It
     requires a connection to a directory service.<br/>
     See the [LDAP Authenticator](#ldap-authenticator) below for more information.


!!! note "Default authenticator"
    Most applications will use a single authenticator. This authenticator is called
    the *default authenticator* and is created automatically when `(auth.)login()^` is called
    for the first time or when any `Authenticator^` for any protocol is created,
    whichever comes first.

    You can retrieve the default authenticator using the function `Authenticator.get_default()^`.

    If `(auth.)login()^` or `Authenticator.get_default()^` are called before any authenticator
    was created, Taipy looks for an `AUTHENTICATION` config section (see `AuthenticationConfig^`
    for more details).
    This config section, if present, is used to instantiate the *default Authenticator*.

    To summarize:

    - The first `Authenticator^` that is created becomes the application's
        default authenticator.
    - When `login()^` is called:

        - A default authenticator is created if there is none, based on the authentication
            configuration.
        - If Taipy could not find the configuration allowing to create such a default
            authenticator, a *None* authenticator is created and set as the default
            authenticator.
        - The default authenticator's `(Authenticator.)login()^` method is invoked
            with the arguments that were provided to `(auth.)login()^`.


Besides their specific parameters, all authenticators have two parameters that you
can provide in the `Authenticator.__init__^`(`Authenticator` constructor):

- *secret_key*: a string that is used to encrypt the user credentials. Because
  credentials are transmitted back and forth when running Taipy on a server
  (when a REST or a GUI application runs), this information is encrypted. You
  can provide an encryption key, or let Taipy create one for you.
- *auth_session_duration*: how long in seconds should the credentials created
  by this authenticator be considered valid.

# 'None' Authenticator

The *None* authenticator does not check for user declaration or password match.
It is designed so that developers can start building secure applications before
the actual authentication system and processes are defined or deployed.

When the *None* authenticator's `(Authenticator.)login()^` method is called, it always
returns a valid `Credentials^` object, no matter what username and password
are provided.

To create a *None* authenticator, you can instantiate an `Authenticator^` object
setting the *protocol* argument of the constructor to "none".

!!! note "Using Taipy configuration to set default authenticator"
    To set the *default authenticator* to `none` you can use the authentication configuration
    either in Python or TOML:

    === "Using Python configuration"
        ```python title="main.py"
        Config.configure_authentication(protocol="none")
        taipy.auth.login("whatever_username", "any_password")  # always returns a valid Credentials instance
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION]
        protocol = "none"
        ```

        ```python title="main.py"
        Config.load("config.toml")
        taipy.auth.login("whatever_username", "any_password")  # always returns a valid Credentials instance
        ```

# Taipy Authenticator

The Taipy Authenticator is an internal authenticator originally designed for
testing purposes, so an application can test authentication and authorization features
without having to install and deploy a real authentication server.

A Taipy Authenticator is created by the `Authenticator.__init__^`(`Authenticator` constructor)
when invoked with the *protocol* argument set to "taipy".

You can set the *roles*' argument to a dictionary that associates a set of role
names to every username you want to grant login access to.<br/>
Here is how you typically create a Taipy authenticator:
```python
from taipy.auth import Authenticator
roles={
  "user1": ["role1", "TAIPY_READER"],
  "user2": ["role2", "TAIPY_ADMIN"],
  "user3": ["role1", "role2", "TAIPY_ADMIN"]
}
authenticator = Authenticator("taipy", roles=roles)
```
This creates an authenticator that allows three users log in,
associating the indicated roles to them.

The previous example declares no passwords. In order to log in, the password must be set
to the username when calling `Authenticator.login()^`:

   - `authenticator.login("user1", "user1")` will successfully create and return a valid
     `Credentials^` instance.
   - `authenticator.login("user1", "anything_else")` will raise the `InvalidCredentials^`
     exception, rejecting the login attempt.

!!! note "Using Taipy configuration to set default authenticator"
    To set the *default authenticator* to a Taipy authenticator with roles, you can use the
    authentication configuration either in Python or TOML:

    === "Using Python configuration"
        ```python title="main.py"
        Config.configure_authentication(protocol="taipy",
                                        roles={
                                            "user1": ["role1", "TAIPY_READER"],
                                            "user2": ["role2", "TAIPY_ADMIN"],
                                            "user3": ["role1", "role2", "TAIPY_ADMIN"]})
        taipy.auth.login("user1", "user1")  # returns a valid Credentials instance
        taipy.auth.login("user1", "anything_else")  # raise an InvalidCredentials exception
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION]
        protocol="taipy"

        [AUTHENTICATION.roles]
        user1 = ["role1", "TAIPY_READER",]
        user2 = ["role2", "TAIPY_ADMIN"],
        user3 = ["role1", "role2", "TAIPY_ADMIN"]
        ```

        ```py title="main.py"
        Config.load("config.toml")
        taipy.auth.login("user1", "user1")  # returns a valid Credentials instance
        taipy.auth.login("user1", "anything_else")  # raise an InvalidCredentials exception
        ```
## Password-protected authentication

The Taipy Authenticator can password-protect the creation of credentials, using the *passwords*'
argument of the `Authenticator.__init__^`(`Authenticator` constructor). This argument expects
a dictionary that associates a username with a password. However, in order not to expose these
passwords, the password values need to be hashed before they are given to the application (in the
`Authenticator^` constructor -- using the *passwords* or in the authentication configuration).<br/>
In the *passwords* argument, the dictionary actually associates a username with a hashed value
for the password. See the [section below](#creating-hashed-passwords) to learn how to create
hashed password values.

You can indicate what are the declared users' passwords:
```python title="main.py"
from taipy.auth import Authenticator
passwords={
  "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
  "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
}
authenticator = Authenticator("taipy", passwords=passwords)
```
Note that these values are the one resulting from the example of  the
[creating hashed passwords](#creating-hashed-passwords) section below.

Calling `(auth.)login("user1", "pass123")^` will result in a valid `Credentials^` instance where
the assigned roles is an empty set.

!!! note "Using Taipy configuration to set default authenticator"

    To set the *default authenticator* to a Taipy authenticator with passwords, you can use the
    authentication configuration either in Python or TOML:

    === "Using Python configuration"
        ```python title="main.py"
        Config.configure_authentication(protocol="taipy",
                                        passwords={
                                            "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
                                            "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"})
        taipy.auth.login("user1", "pass123")  # returns a valid Credentials instance
        taipy.auth.login("user1", "anything_else")  # raise an InvalidCredentials exception
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"

        [AUTHENTICATION]
        protocol="taipy"

        [AUTHENTICATION.passwords]
        user1 = "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm"
        user2 = "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
        ```

        ```py title="main.py"
        Config.load("config.toml")
        taipy.auth.login("user1", "pass123")  # returns a valid Credentials instance
        taipy.auth.login("user1", "anything_else")  # raise an InvalidCredentials exception
        ```

Of course, you can combine both roles and password for any given user, using both the *roles*
and *passwords* arguments of the `Authenticator.__init__^`(`Authenticator` constructor), or
using its *config* argument:
```python title="main.py"
users={
    "roles": {
        "user1": "role1",
        "user2": ["role2", "TAIPY_ADMIN"],
        "user3": ["role1", "role2", "TAIPY_ADMIN"]
    },
    "passwords": {
        "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
        "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
    }
}
authenticator = Authenticator("taipy", config=users)
```

With this authenticator, if you run the code:
```python
user1 = authenticator.login("user1", pass1)
print(f"user1 - Logged in. Roles={user1.get_roles()}")
user2 = authenticator.login("user2", pass2)
print(f"user2 - Logged in. Roles={user2.get_roles()}")
user3 = authenticator.login("user3", "user3")
print(f"user3 - Logged in. Roles={user3.get_roles()}")
```
You get the following output:
```
user1 - Logged in. Roles={'role1'}
user2 - Logged in. Roles={'role2', 'TAIPY_ADMIN'}
user3 - Logged in. Roles={'role1', 'role2', 'TAIPY_ADMIN'}
```

Note that, because "user3" was not constrained by any password, we need to use the username as
the password value for this user.

!!! note "Using Taipy configuration to set default authenticator"

    To set the *default authenticator* to a Taipy authenticator with roles and passwords, you
    can use the authentication configuration either in Python or TOML:

    === "Using Python configuration"
        ```python title="main.py"
        Config.configure_authentication(protocol="taipy",
                                        roles={
                                            "user1": "role1",
                                            "user2": ["role2", "TAIPY_ADMIN"],
                                            "user3": ["role1", "role2", "TAIPY_ADMIN"]},
                                        passwords={
                                            "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
                                            "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"})

        taipy.auth.login("user1", "pass123")  # returns a valid Credentials instance
        taipy.auth.login("user1", "anything_else")  # raise an InvalidCredentials exception
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION]
        protocol="taipy"

        [AUTHENTICATION.roles]
        user1 = "role1"
        user2 = ["role2", "TAIPY_ADMIN"],
        user3 = ["role1", "role2", "TAIPY_ADMIN"]

        [AUTHENTICATION.passwords]
        user1 = "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm"
        user2 = "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
        ```

        ```py title="main.py"
        Config.load("config.toml")
        taipy.auth.login("user1", "pass123")  # returns a valid Credentials instance
        taipy.auth.login("user1", "anything_else")  # raise an InvalidCredentials exception
        ```

## Creating hashed passwords

Taipy provides two ways of creating a hashed password provided the plain text representation of
the password:

- API: You can use the function `hash_taipy_password()^` that, given a plain text string, returns
    the hashed value for it.

- CLI: The `taipy.auth` module has an entry point that can be invoked from
    the CLI, using the `-m` option of Python, and the `-p` option of the
    `taipy.auth` module. Below is an example of how to use the CLI option.

Note that only the first 16 characters of the plain text password are used when creating the
hashed password.

Before you use any of these two ways for creating hashed passwords, you must come up with a
secret hash value. This value is used to generate unique hashed passwords. This value must be
set to the 'TAIPY_AUTH_HASH' environment variable in order to generate hashed passwords, as well
as when running the application, so passwords can be verified.<br/>
The value of 'TAIPY_AUTH_HASH' can be any string value.</br>
The value of 'TAIPY_AUTH_HASH' **must** be the same when generating the hashed passwords and
when running the application that invokes the `(auth.)login()^` function.

!!! example "Create a hashed password using the API"

    Here is an example of how you can create a hashed password using the Taipy API.

    We assume that the environment variable 'TAIPY_AUTH_HASH' is set to "Taipy".

    ```python
    from taipy.auth import hash_taipy_password

    pass1 = "pass123"
    hashed_pass1 = hash_taipy_password(pass1)
    print(f"Password 1: {hashed_pass1}")
    pass2 = "pass1234"
    hashed_pass2 = hash_taipy_password(pass2)
    print(f"Password 2: {hashed_pass2}")
    ```
    Produces the output:
    ```
    Password 1: eSwebyvpEElWbZNTNqpW7rNQPDPyJSm
    Password 2: JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe
    ```

!!! example "Create a hashed password using the CLI"

    Here is an example of how you can create hashed passwords using the Taipy CLI.

    Here again, we assume that the environment variable 'TAIPY_AUTH_HASH' is set to "Taipy".

    ```sh
    $ python -m taipy.auth -p pass123 pass1234
    ```
    Produces the following output:
    ```
    hash(pass123)=eSwebyvpEElWbZNTNqpW7rNQPDPyJSm
    hash(pass1234)=JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe
    ```

    Note that the hashed values are the same as in the first example. This is entirely due to
    the fact that we have used the same secret hashing value in 'TAIPY_AUTH_HASH'.

# LDAP Authenticator

Taipy also provide support for LDAP authentication.

The LDAP authenticator has two specific parameters that need to be provided in order to properly
connect to the directory service:

- *server*: the URL of the LDAP server that we want to connect to.<br/>
    If you are using the Taipy configuration, the value for this argument
    is retrieved if needed from _**Config.AUTHENTICATION.server**_.
- *base_dn*: the base distinguished name for that LDAP server.<br/>
    If you are using the Taipy configuration, the value for this argument
    is retrieved if needed from _**Config.AUTHENTICATION.base_dn**_.

??? note "LDAP server support"

    Using the LDAP authentication protocol assumes that an LDAP server is set up. Taipy provides
    no support for setting up the server.

!!! note "Using Taipy configuration to set default authenticator"

    To set the *default authenticator* to an LDAP authenticator you can use the authentication
    configuration either in Python or TOML:

    === "Python configuration"
        ```python title="main.py"
            Config.configure_authentication(protocol="ldap",
                                            server="ldap://0.0.0.0",
                                            base_dn="dc=example,dc=org",
                                            secret_key = "my-ultra-secure-and-ultra-long-secret",
                                            auth_session_duration = 600,)   # 60 seconds is 10 minutes

        ```

    === "TOML configuration"
        ```toml title="config.toml"

        [AUTHENTICATION]
        protocol="ldap"
        server="ldap://0.0.0.0"
        base_dn="dc=example,dc=org"
        secret_key = "my-ultra-secure-and-ultra-long-secret"
        auth_session_duration = 600   # 60 seconds is 10 minutes,
        ```

        ```py title="main.py"
        Config.load("config.toml")

        taipy.auth.login("user1", "pass123")
        # Returns a valid Credentials instance if the LDAP server validates the password
        # "pass123" for user "user1". Raises an InvalidCredentials exception otherwise.
        ```

# Microsoft Entra ID Authenticator

Taipy provides support for Microsoft Entra ID authentication.

An authenticator using the *Entra ID* protocol has two specific parameters that need to be provided
in order to properly connect to the Microsoft Entra ID service:

- *client_id*: The client ID of the Entra ID application. The application must be registered in the
    Azure Entra ID portal and have the required permissions including the "User.Read" and
    "GroupMember.Read.All" permissions.
- *tenant_id*: The tenant ID of the Entra ID organization.

??? note "Entra ID application management"

    Using the Entra ID authentication protocol assumes that an Entra ID application is already set
    up with the required permissions. Taipy doesn't manage the Entra ID application.

    First, you need to
    [create an application in the Microsoft Azure portal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)
    within your organization.<br/>
    Make sure that the Redirect URI of the application is set to `http://localhost`
    or the URI of your Taipy application.

    The application needs to be
    [assigned permissions](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#assign-a-role-to-the-application).<br/>
    The required permissions are:

    - `User.Read` for accessing the logged in user email from the Microsoft Graph API.
    - `GroupMember.Read.All` for accessing the groups the user is a member of. The groups
        are used to assign roles to the user.

    From the Entra ID application,
    [create a new secret in the Azure portal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#assign-a-role-to-the-application).

    The secret is only shown once, so make sure to store it in a safe place.
    You then need to set the `ENTRA_CLIENT_SECRET` environment variable to the secret value.
    This environment variable is required for logging in with Microsoft Entra ID accounts.

    Taipy provides no support for setting up the application.

!!! usage "Configure an authenticator and login"

    To create an authenticator as an Entra ID authenticator, you can use the authentication
    configuration either in Python or TOML:

    === "Using Python configuration"
        ```python title="main.py"
        Config.configure_authentication(protocol="entra_id",
                                        client_id="<client-id>",
                                        tenant_id="<tenant-id>",
                                        secret_key = "<secure-secret-key>",
                                        tenant_id="my-tenant-id",
                                        secret_key = "my-ultra-secure-and-ultra-long-secret",
                                        auth_session_duration = 600)  # 10 minutes
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION.entra_id]
        protocol="entra_id"
        client_id="<client-id>"
        tenant_id="<tenant-id>"
        secret_key = "<secure-secret-key>"
        tenant_id="my-tenant-id"
        secret_key = "my-ultra-secure-and-ultra-long-secret"
        auth_session_duration = 3600 # 1 hour
        ```

        ```py title="main.py"
        Config.load("config.toml")

        taipy.auth.login()
        # Returns a valid Credentials instance if you have logged in with valid Microsoft account
        # in your current browser. Raises an InvalidCredentials exception otherwise.
        ```
