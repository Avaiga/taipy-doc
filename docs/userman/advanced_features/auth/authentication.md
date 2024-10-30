!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

Authentication is the process to secure user identity in an application.

# Authentication process

In Taipy Enterprise, the authentication process requires an *authenticator* to be configured.
It validates the user's identity and retrieves the roles associated with the user.

1. Configure an *authenticator*.<br/>
    An `Authenticator^` implements an *authentication protocol* (`taipy`, `ldap`, `entra-id`,
    etc.), defining how the user's identity is verified and how the roles are retrieved. The
    authenticator can be created by Taipy directly based on the authentication configuration
    or manually calling the `Authenticator` constructor (`Authenticator.__init__^`()).

2. Login the user.<br/>
    The `(auth.)login()^` function takes a username and a password as arguments and delegates
    to the authenticator (`(Authenticator.)login()^` method) the user's identity validation.
    If the username and password are valid, the function creates and returns a `Credentials^`
    object that represents the user in the application with its roles. It raises an
    `InvalidCredentials^` exception otherwise.

3. Use the `Credentials^` object.<br/>
    To check if a user has a specific role, you can use the `Credentials^` object returned by
    the `(auth.)login()^` function. It has a `Credentials.get_roles()^` method that
    returns the roles associated with the user. For more details on how to use the `Credentials^`
    and the roles, please refer to the [Authorization and Roles](authorization.md) section.

# Create Authenticators and Login

You can use the `Config.configure_authentication()^` method to create an authenticator.
Taipy automatically instantiates the authenticator based on the configuration attributes.
Alternatively, you can manually create an authenticator by calling the `Authenticator`
constructor (`Authenticator.__init__^`()).

??? tip "Having different authenticators in different environments"

    Using the `Config.configure_authentication()^` method to create an authenticator is a good
    practice since it allows you to benefit from the Taipy configuration system to set up
    different authenticators in different environments. <br/>
    For instance, you may want to use a *Taipy* protocol in local so you can run and test your
    application locally. Then you can switch to an *LDAP* protocol when deploying your application
    to a server without having to change your code base. You just need to use the TOML
    configuration file to override the default configuration. Please refer to the
    [advanced configuration](../configuration/advanced-config.md#override-with-file-in-env-variable)
    section.

Each `Authenticator^` implements an *authentication protocol* among the ones supported by Taipy:

- *none*: The None authenticator does not check the user password in `(auth.)login()^` and always
    validates the login process by creating a `Credentials^` instance that holds an empty role set.
    This protocol is basically used when the authentication is de-activated.<br/>
    See the [None Authenticator](#none-protocol) section below for more information.

- *Taipy*: The Taipy authenticator makes sure users are declared, can retrieve role sets for those
    users and can check passwords if required.<br/>
    This protocol is used for testing purposes, so an application can test its features without
    having to install and deploy a real authentication server.<br/>
    See the [Taipy Authenticator](#taipy-protocol) section below for more information.

- *LDAP*: The LDAP authenticator is an implementation of the LDAP protocol. It requires a
    connection to a directory service.<br/>
    See the [LDAP Authenticator](#ldap-protocol) section below for more information.

- *Entra ID*: The Entra ID authenticator is an implementation of the Microsoft Entra ID protocol.
    It requires a connection to the Microsoft Entra ID application.<br/>
    See the [Entra ID Authenticator](#microsoft-entra-id-protocol) section below for more
    information.

Besides their specific parameters, all authenticators have two parameters that you
can provide in the `Authenticator.__init__^`(`Authenticator` constructor):

- *secret_key*: a string that is used to encrypt the user credentials. Because
  credentials are transmitted back and forth when running Taipy on a server
  (when a REST or a GUI application runs), this information is encrypted. You
  can provide an encryption key, or let Taipy create one for you.
- *auth_session_duration*: how long in seconds should the credentials created
  by this authenticator be considered valid.

??? note "Multiple Authenticators in a single application"

    An application can have multiple authenticators, each implementing a different authentication
    protocol. When the `(auth.)login()^` function is called, it tries to authenticate the user
    with each authenticator in the order they were created or configured. The first authenticator
    that returns a valid `Credentials^` object is used to create the `Credentials^` instance.

## 'None' protocol

An authenticator with a *None* protocol does not check for user declaration or password match.
It is designed so that you can start building applications before the actual authentication system
is in place.

When the *None* authenticator's `(Authenticator.)login()^` method is called, it always
returns a valid `Credentials^` object, no matter what username and password are provided.

The *None* protocol is the default protocol created by Taipy when no authentication configuration
is provided. You can also create a `none` authenticator with the authentication configuration
either in Python or TOML or with the `Authenticator^` constructor:

!!! usage "Configure an authenticator and login"

    === "Using Python configuration"
        ```python title="main.py"
        Config.configure_authentication(protocol="none")
        taipy.auth.login("whatever_username", "any_pwd")  # always returns valid Credentials
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION.none]
        protocol = "none"
        ```

        ```python title="main.py"
        Config.load("config.toml")
        taipy.auth.login("whatever_username", "any_pwd")  # always returns valid Credentials
        ```

    === "Using Authenticator constructor"
        ```python title="main.py"
        authenticator = Authenticator(protocol="none")
        authenticator.login("whatever_username", "any_pwd")  # always returns valid Credentials
        ```

## Taipy protocol

A *Taipy* authenticator is an embedded authenticator originally designed for testing purposes, so an
application can test its features with authentication and authorization without having to install
and deploy a real authentication server.

To use the Taipy authenticator, you need to declare the users and their roles. You can set the
*roles* to a dictionary that associates a set of role names to every username you want to grant
login access to. Here is an example of a role dictionary:

```python
roles={
  "user1": ["role1", "TAIPY_READER"],
  "user2": ["role2", "TAIPY_ADMIN"],
  "user3": ["role1", "role2", "TAIPY_ADMIN"]
}
```

You can create a `Taipy` authenticator with the authentication configuration
either in Python or TOML or with the `Authenticator^` constructor:

!!! usage "Configure an authenticator and login"

    === "Using Python configuration"
        ```python title="main.py"
        roles={
            "user1": ["role1", "TAIPY_READER"],
            "user2": ["role2", "TAIPY_ADMIN"],
            "user3": ["role1", "role2", "TAIPY_ADMIN"]
        }
        Config.configure_authentication(protocol="taipy", roles=roles)
        taipy.auth.login("user1", "user1")  # returns valid Credentials
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION.taipy]
        protocol="taipy"

        [AUTHENTICATION.taipy.roles]
        user1 = ["role1", "TAIPY_READER",]
        user2 = ["role2", "TAIPY_ADMIN"],
        user3 = ["role1", "role2", "TAIPY_ADMIN"]
        ```

        ```py title="main.py"
        Config.load("config.toml")
        taipy.auth.login("user1", "user1")  # returns valid Credentials
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

    === "Using Authenticator constructor"
        ```python title="main.py"
        roles={
            "user1": ["role1", "TAIPY_READER"],
            "user2": ["role2", "TAIPY_ADMIN"],
            "user3": ["role1", "role2", "TAIPY_ADMIN"]
        }
        authenticator = Authenticator("taipy", roles=roles)
        authenticator.login("user1", "user1")  # returns valid Credentials
        authenticator.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

### Password-protected authentication

Similarly to the roles, you can also provide passwords for the users in the Taipy authenticator
to password-protect the creation of credentials.

You can set the *passwords* to a dictionary that associates a password to every username. In order
not to expose them, the password values need to be hashed before they are given to the application.

Here is an example of a dictionary with hashed passwords:

```python title="main.py"
passwords={
  "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
  "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
}
```

Note that, because "user3" has no declared password, The *Taipy* protocol considers the username
and password to be the same. This means that the user can log in with the username as the password.

See the [section below](#creating-hashed-passwords) to learn how to create hashed password values.

!!! usage "Configure an authenticator and login"

    === "Using Python configuration"
        ```python title="main.py"
        passwords={
            "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm", # This is the hashed value of "pass123"
            "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
        }
        Config.configure_authentication(protocol="taipy", passwords=passwords)
        taipy.auth.login("user1", "pass123")  # returns valid Credentials
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION.taipy]
        protocol="taipy"

        [AUTHENTICATION.taipy.passwords]
        user1 = "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm"
        user2 = "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
        ```

        ```py title="main.py"
        Config.load("config.toml")
        taipy.auth.login("user1", "pass123")  # returns valid Credentials
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

    === "Using Authenticator constructor"
        ```python title="main.py"
        passwords={
            "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm", # This is the hashed value of "pass123"
            "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
        }
        authenticator = Authenticator("taipy", passwords=passwords)
        authenticator.login("user1", "user1")  # returns valid Credentials
        authenticator.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

??? example "Combining roles and passwords"

    Of course, you can combine both roles and password for any given user, using both the *roles*
    and *passwords* dictionnaries. Here is an example of how you can do it:

    === "Using Python configuration"
        ```python title="main.py"
        roles={
            "user1": "role1",
            "user2": ["role2", "TAIPY_ADMIN"],
            "user3": ["role1", "role2", "TAIPY_ADMIN"]},
        passwords={
            "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
            "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"}
        Config.configure_authentication(protocol="taipy", roles=roles, passwords=passwords)
        taipy.auth.login("user1", "pass123")  # returns valid Credentials
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION.taipy]
        protocol="taipy"

        [AUTHENTICATION.taipy.roles]
        user1 = "role1"
        user2 = ["role2", "TAIPY_ADMIN"],
        user3 = ["role1", "role2", "TAIPY_ADMIN"]

        [AUTHENTICATION.taipy.passwords]
        user1 = "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm"
        user2 = "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
        ```

        ```py title="main.py"
        Config.load("config.toml")
        taipy.auth.login("user1", "pass123")  # returns valid Credentials
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

    === "Using Authenticator constructor"
        ```python title="main.py"
        roles={
            "user1": "role1",
            "user2": ["role2", "TAIPY_ADMIN"],
            "user3": ["role1", "role2", "TAIPY_ADMIN"]},
        passwords={
            "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
            "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"}
        authenticator = Authenticator("taipy", roles=roles, passwords=passwords)
        authenticator.login("user1", "pass123")  # returns valid Credentials
        authenticator.login("user1", "anything_else")  # raises an InvalidCredentials exception
        ```

### Creating hashed passwords

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

!!! example "Create a hashed password"

    Here is an example of how you can create a hashed password. We assume that the environment
    variable 'TAIPY_AUTH_HASH' is set to "Taipy".

    === "Using the API"

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

    === "Using the CLI"
        ```sh
        $ python -m taipy.auth -p pass123 pass1234
        ```
        Produces the following output:
        ```
        hash(pass123)=eSwebyvpEElWbZNTNqpW7rNQPDPyJSm
        hash(pass1234)=JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe
        ```

## LDAP protocol

Taipy also provide support for LDAP authentication.

An authenticator with the *LDAP*  protocol has two specific parameters that need to be provided
in order to properly connect to the directory service:

- *server*: the URL of the LDAP server that we want to connect to.<br/>
- *base_dn*: the base distinguished name for that LDAP server.<br/>

??? note "LDAP server management"

    Using the LDAP authentication protocol assumes that an LDAP server is already set up. Taipy
    do not manage the LDAP server, and provides no support for setting up the server.

You can create an `LDAP` authenticator with the authentication configuration
either in Python or TOML or with the `Authenticator^` constructor:

!!! usage "Configure an authenticator and login"

    === "Using Python configuration"
        ```python title="main.py"
        Config.configure_authentication(protocol="ldap",
                                        server="ldap://0.0.0.0",
                                        base_dn="dc=example,dc=org",
                                        secret_key = "my-ultra-secure-and-ultra-long-secret",
                                        auth_session_duration = 600)  # 10 minutes
        taipy.auth.login("user1", "pass123") # returns Credentials if password "pass123" is validated by the LDAP server
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception otherwise
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION.ldap]
        protocol="ldap"
        server="ldap://0.0.0.0"
        base_dn="dc=example,dc=org"
        secret_key = "my-ultra-secure-and-ultra-long-secret"
        auth_session_duration = 600  # 10 minutes,
        ```

        ```py title="main.py"
        Config.load("config.toml")

        taipy.auth.login("user1", "pass123") # returns Credentials if password "pass123" is validated by the LDAP server
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception otherwise
        ```

    === "Using Authenticator constructor"
        ```python title="main.py"
        authenticator = Authenticator(protocol="ldap",
                                      server="ldap://
                                      base_dn="dc=example,dc=org",
                                      secret_key = "my-ultra-secure-and-ultra-long-secret",
                                      auth_session_duration = 600)  # 10 minutes
        taipy.auth.login("user1", "pass123") # returns Credentials if password "pass123" is validated by the LDAP server
        taipy.auth.login("user1", "anything_else")  # raises an InvalidCredentials exception otherwise
        ```

## Microsoft Entra ID protocol

Taipy also provides support for Microsoft Entra ID authentication.

An authenticator using the *Entra ID* protocol has two specific parameters that need to be provided
in order to properly connect to the Microsoft Entra ID service:

- *client_id*: The client ID of the Entra ID application. The application must be registered in the
    Azure Entra ID portal and have the required permissions including the "User.Read" and
    "GroupMember.Read.All" permissions.
- *tenant_id*: The tenant ID of the Entra ID organization.

??? note "Entra ID application management"

    Using the Entra ID authentication protocol assumes that an Entra ID application is already set up
    with the required permissions. Taipy don't manage the Entra ID application.

    First, you need to
    [create an application in the Microsoft Azure portal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)
    within your organization.
    Make sure that the Redirect URI of the application is set to `http://localhost`
    or the URI of your Taipy application.

    The application needs to be [assigned permissions](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#assign-a-role-to-the-application).
    The required permissions are:

    - `User.Read` for accessing the logged in user email from the Microsoft Graph API.
    - `GroupMember.Read.All` for accessing the groups the user is a member of. The groups
        are used to assign roles to the user.

    From the Entra ID application, [create a new secret in the Azure portal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#assign-a-role-to-the-application).

    The secret is only shown once, so make sure to store it in a safe place.
    You then need to set the `ENTRA_CLIENT_SECRET` environment variable to the secret value.
    This environment variable is required for logging in with Microsoft Entra ID accounts.

    Taipy provides no support for setting up the application.

!!! usage "Configure an authenticator and login"

    To create an authenticator as an Entra ID authenticator, you can use the authentication
    configuration either in Python or TOML:

    === "Using Python configuration"
        ```python title="main.py"
        Config.configure_authentication(protocol="ldap",
                                        client_id="my-client-id",
                                        tenant_id="my-tenant-id",
                                        secret_key = "my-ultra-secure-and-ultra-long-secret",
                                        auth_session_duration = 600)  # 10 minutes
        ```

    === "Using TOML configuration"
        ```toml title="config.toml"
        [AUTHENTICATION.entra_id]
        protocol="entra_id"
        client_id="my-client-id"
        tenant_id="my-tenant-id"
        secret_key = "my-ultra-secure-and-ultra-long-secret"
        auth_session_duration = 600 # 10 minutes
        ```

        ```py title="main.py"
        Config.load("config.toml")

        taipy.auth.login()
        # Returns a valid Credentials instance if you have logged in with valid Microsoft account
        # in your current browser. Raises an InvalidCredentials exception otherwise.
        ```

    === "Using Authenticator constructor"
        ```python title="main.py"
        authenticator = Authenticator(protocol="entra_id",
                                      client_id="my-client-id",
                                      tenant_id="my-tenant-id",
                                      secret_key = "my-ultra-secure-and-ultra-long-secret",
                                      auth_session_duration = 600)  # 10 minutes
        taipy.auth.login()
        # Returns a valid Credentials instance if you have logged in with valid Microsoft account
        # in your current browser. Raises an InvalidCredentials exception otherwise.
        ```
