!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

Authentication is the process that makes sure a given user exists and
that the password that is provided when logging in matches the expected
one. This process ensures that a user that logs in really is who she or
he claims to be.

In Taipy Enterprise, the authentication process is achieve by the
`Authenticator^` class and indirectly by the `login()^` function:
this function creates and returns a `Credentials^` object that
represents the user in the application.</br>
The returned `Credentials^` instance contains the set of roles assigned to
the user in the authentication system.

The programmer can create an authenticator manually (see 
[`Authenticator` constructor](Authenticator.__init__()^) for more information)
if the kind of authenticator needed by the application is known
(that is, what authentication protocol the application plans to rely on). The
programmer can alternatively use the `login()^` function that will create
an `Authenticator^` the first time it is invoked.

Taipy Enterprise supports three authentication protocols:

   - "none": The *None* authenticator does not check the user password in
      `login()` and always validates the login process by creating a `Credentials^`
      instance that holds an empty role set.<br/> 
      See the [*None* Authenticator](#none-authenticator) below for more information.

   - "Taipy": The *Taipy* authenticator makes sure users actually are declared, can
     retrieve role sets for those users and can check passwords if required.<br/>
     See the [Taipy Authenticator](#taipy-authenticator) below for more information.

   - "LDAP": The *LDAP* authenticator is an implementation of the LDAP protocol. It
     requires a connection to a directory service.<br/>
     See the [LDAP Authenticator](#ldap-authenticator) below for more information.


!!! Note "Default authenticator"
    Most applications will use a single authenticator. This authenticator is called
    the *default authenticator* and is created
    automatically when `login()^` is called for the first time or when any
    `Authenticator^` for any protocol is created, whichever comes first.

    You can retrieve the default authenticator using the function
    `Authenticator.get_default()^`.

    If `login()^` or `Authenticator.get_default()^` are called before any authenticator
    was created, Taipy looks in the current directory for a file called
    *taipy&#x5F;auth&#x5F;&lt;protocol&gt;.json* where *&lt;protocol&gt;*
    is "none", "taipy" or "ldap",
    indicating the type of default authenticator the application will use use.<br/>
    This file, if present, is read as a JSON data file. This should result in a dictionary
    that is sent as the *config* argument to the constructor of `Authenticator^`.

    To summarize:

    - The first `Authenticator^` that is created becomes the application's
      default authenticator.
    - When `login()^` is called:

        - A default authenticator is created if there is none, based on files
          that may be sitting in the current directory or the application's
          [Global Configuration](../core/config/global-config.md).
        - If Taipy could not find the configuration allowing to create such a default
          authenticator, a *None* authenticator is created and set as the default 
          authenticator.
        - The default authenticator's `(Authenticator.)login()^` function is invoked
          with the arguments that were provided to `login()^`.
    

Beside their specific parameters, all authenticators have two parameters that you
can provide in the [`Authenticator` constructor](Authenticator.__init__()^):

- *secret_key*: a string that is used to encrypt the user credentials. Because
  credentials are transmitted back and fourth when running Taipy on a server
  (when a REST or a GUI application runs), this information is encrypted. You
  can provide an encryption key, or let Taipy create one for you.
- *auth_session_duration*: how long in seconds should the credentials created
  by this authenticator be considered valid. 

!!! Note "Global configuration"
    If you are using Taipy Core (the `taipy.core` package), these parameters can also
    be set in the [Taipy Global Configuration](../core/config/global-config.md).

    The global configuration properties related to the default authentication
    are used if the parameters are not loaded from a
    *taipy&#x5F;auth&#x5F;&lt;protocol&gt;.json* file.

    Here is how you cound use the _**Config.global_config.secret_key**_ and
    _**Config.global_config.auth_session_duration**_ properties of the
    global configuration:

    === "Python configuration"

        ```
        Config.configure_global_app(secret_key = "my-ultra-secure-and-ultra-long-secret",
                                    auth_session_duration = 600)  # 60 seconds = 10 minutes
        ```

    === "TOML configuration"

        ```toml title="config.toml"

        [TAIPY]
        secret_key = "my-ultra-secure-and-ultra-long-secret"
        auth_session_duration = 600   # 60 seconds = 10 minutes,
        ```


## 'None' Authenticator

The *None* authenticator does not check for user declaration or password match.
It is designed so that developers can start building secure applications before
the actual authentication system and processes are defined or deployed.

When the *None* authenticator `(Authenticator.)login()^` method is called, it always
returns a valid `Credentials^` object, no matter what user name and password
are provided.

To create a *None* authenticator, you can instantiate an `Authenticator^` object
setting the *protocol* argument of the constructor (or
) to "none".

## Taipy Authenticator

The Taipy Authenticator is an internal authenticator originally designed for
testing purposes, so an application can test authentication and authorization features
without having to install and deploy a real authentication server.

A Taipy Authenticator is created by the
[`Authenticator` constructor](Authenticator.__init__()^) when invoked with the
*protocol* argument set to "taipy".

You can set the *roles* argument to a dictionary that associates a set of role
names to every user name you want to grant login access to.<br/>
Here is how you typically create a Taipy authenticator:
```
from taipy.auth import Authenticator
roles={
  "user1": "role1",
  "user2": "role2",
  "user3": ["role1", "role2"]
}
authenticator = Authenticator("taipy", roles=roles)
```
This creates an authenticator that allows three users log in,
associating the indicated roles to them.

The previous example declares no passwords. In order to log in, the password must be set
to the user name when calling `Authenticator.login()^`:

   - `authenticator.login("user1", "user1")` will successfully create and return a valid
     `Credentials^` instance.
   - `authenticator.login("user1", "anything_else")` will raise the `InvalidCredentials^`
     exception, rejecting the login attempt.

Here is an example of using the
[Taipy Global Configuration](../core/config/global-config.md), to configure the
Taipy Authenticator with two users, with and without assigned roles:

=== "Python configuration"

    ```
    Config.configure_global_app(auth_protocol="taipy",
                                auth_roles={
                                    "user1": ["role1", "role2"],
                                    "user2": []
                                    }
                                )
    ```

=== "TOML configuration"

    ```py
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml title="config.toml"

    [TAIPY]
    auth_protocol="taipy"

    [TAIPY.auth_roles]
    user1 = [ "role1", "role2",]
    user2 = []
    ```

### Password-protected authentication

The Taipy Authenticator can password-protect the creation of credentials,
using the *passwords* argument of the
[`Authenticator` constructor](Authenticator.__init__()^). This argument expects a
dictionary that associates a user name with a password. However, in order not to
expose these passwords, the password values need to be hashed before they are given
to the application (in the `Authenticator^` constructor -- using the *passwords* or
*config* parameters -- or in the 'taipy_auth_taipy.json' file).<br/>
In the *passwords* argument, the dictionary actually associates a user name
with a hashed value for the password. See the
[section below](#creating-hashed-passwords)
to learn how to create hashed password values.

You can indicate what are the declared users' passwords:
```
from taipy.auth import Authenticator
passwords={
  "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
  "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
}
authenticator = Authenticator("taipy", passwords=passwords)
```
Note that these values are the one resulting from the example of  the
[creating hashed passwords](#creating-hashed-passwords) section below.

Calling `login("user1", "pass123")^` will result in a valid `Credentials^` 
instance where the assigned roles is an empty set.

Of course you can combine both roles and password for any given user, using
both the *roles* and *passwords* arguments of the
[`Authenticator` constructor](Authenticator.__init__()^), or using its
*config* argument:
```
users={
    "roles": {
      "user1": "role1",
      "user2": "role2",
      "user3": ["role1", "role2"]
    },
    "passwords": {
        "user1": "eSwebyvpEElWbZNTNqpW7rNQPDPyJSm",
        "user2": "JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe"
    }
}
auth = Authenticator("taipy", config=users)
```

With this authenticator, if you run the code:
```
user1 = auth.login("user1", pass1)
print(f"user1 - Logged in. Roles={user1.get_roles()}")
user2 = auth.login("user2", pass2)
print(f"user2 - Logged in. Roles={user2.get_roles()}")
user3 = auth.login("user3", "user3")
print(f"user3 - Logged in. Roles={user3.get_roles()}")
```
You get the following output:
```
user1 - Logged in. Roles={'role1'}
user2 - Logged in. Roles={'role2'}
user3 - Logged in. Roles={'role1', 'role2'}
```

Note that, because "user3" was not constrained by any password, we need
to use the user name as the password value for this user.

### Creating hashed passwords

Taipy provides two ways of creating a hashed password provided the plain text
representation of the password:

   - API: You can use function `hash_taipy_password()^` that, given a plain
     text string, returns the hashed value for it.

   - CLI: The `taipy.auth` module has an entry point that can be invoked from
     the CLI, using -t `-m` option of Python, and the `-p` option of the
     `taipy.auth` module. Below is an example of how to use the CLI option.

Note that only the first 16 characters of the plain text password are
used when creating the hashed password.

Before you use any of these two ways for creating hashed passwords, you must come
up with a secret hash value. This value is used to generate unique hashed passwords.
This value must be set to the 'TAIPY_AUTH_HASH' environment variable in
order to generate hashed passwords, as well as when running the application,
so passwords can be verified.<br/>
The value of 'TAIPY_AUTH_HASH' can be any string value.</br>
Obviously, the value of 'TAIPY_AUTH_HASH' must be the same when generating the
hashed passwords and when running the application that invokes the `login()^`
function.

!!! example "Create a hashed password using the API"
    Here is an example of how you can create a hashed password using
    the Taipy API.

    We assume that the environment variable 'TAIPY_AUTH_HASH' is set
    to "Taipy".

    ```
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
    Here is an example of how you can create hashed passwords using
    the Taipy CLI.

    Here again, we assume that the environment variable 'TAIPY_AUTH_HASH' is
    set to "Taipy".

    ```
    <b>$ </b>python -m taipy.auth -p pass123 pass1234
    ```
    Produces the following output:
    ```
    hash(pass123)=eSwebyvpEElWbZNTNqpW7rNQPDPyJSm
    hash(pass1234)=JQlZ4IXorPcJYvMLFWE/Gu52XNfavMe
    ```

    Note that the hashed values are the same as in the first example. This is
    entirely due to the fact that we have used the same secret hashing value
    in 'TAIPY_AUTH_HASH'.

## LDAP Authenticator

Taipy also provide support for LDAP authentication.

The LDAP authenticator has two specific parameters that need to be provided in order
to properly connect to the directory service:

- *server*: the URL of the LDAP server that we want to connect to.<br/>
  If you are using the Taipy Core configuration, the value for this argument
  is retrieved if needed from _**Config.global_config.ldap_server**_.
- *base_dn*: the base distinguished name for that LDAP server.<br/>
  If you are using the Taipy Core configuration, the value for this argument
  is retrieved if needed from _**Config.global_config.ldap_base_dn**_.

Here is an example of using the
[Taipy Global Configuration](../core/config/global-config.md), to configure the
connection of Taipy Enterprise edition to an LDAP server, which would be relevant
if you are using Taipy Core (the `taipy.core` package):

=== "Python configuration"

    ```
    Config.configure_global_app(auth_protocol="ldap",
                                ldap_server="ldap://0.0.0.0",
                                ldap_base_dn="dc=example,dc=org",
                                secret_key = "my-ultra-secure-and-ultra-long-secret",
                                auth_session_duration = 600,)   # 60 seconds is 10 minutes
    ```

=== "TOML configuration"

    ```py
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml title="config.toml"

    [TAIPY]
    auth_protocol="ldap"
    ldap_server="ldap://0.0.0.0"
    ldap_base_dn="dc=example,dc=org"
    secret_key = "my-ultra-secure-and-ultra-long-secret"
    auth_session_duration = 600   # 60 seconds is 10 minutes,
    ```

!!! important "LDAP server support"
    Using the LDAP authentication protocol assumes that an LDAP server is set up.
    Taipy provides no support for setting up the server.
