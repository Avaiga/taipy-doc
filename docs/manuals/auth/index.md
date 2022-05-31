!!! warning "Reminder: Authorization and Authentication is only available in the Enterprise version"

# Pre-requisites

An LDAP server must be set up by the user. Taipy provides no support for setting up the server.

# Configuration

You must configure how Taipy connects to the LDAP server using the Taipy `Config^` features. Here are the configurable properties you can use:

- **Config.global_config.ldap_server**: The url of the LDAP server.
- **Config.global_config.ldap_base_dn**: The base DN that the LDAP server uses to search for users authentication.
- **Config.global_config.jwt_secret**: The secret that will be used to generate the access token
- **Config.global_config.jwt_expire**: The period after which the JWT token provided by Taipy will be expired.
- **Config.global_config.auth_enabled**: The field to enable or disable Taipy authentication and authorization. Its default value is True, meaning that the enterprise version, by default, will have authentication and authorization feature enabled.

Here is an example of configuring LDAP server connection in Taipy:


=== "Python configuration"

    ```
    Config.configure_global_app(ldap_server="ldap://0.0.0.0",
                                ldap_base_dn="dc=example,dc=org",
                                jwt_secret = "my-ultra-secure-and-ultra-long-secret",
                                jwt_expire = 600   # 60 seconds is 10 minutes,
                                auth_enabled = True)
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"

    [TAIPY]

    ldap_server="ldap://0.0.0.0"
    ldap_base_dn="dc=example,dc=org"
    jwt_secret = "my-ultra-secure-and-ultra-long-secret"
    jwt_expire = 600   #for 10 minutes
    auth_enabled = True
    ```

# Roles

Taipy has four predefined user roles names that can be assigned to users. Each of these predefined roles provide a different set of capabilities and will be described in details below.

## TAIPY_READER

- A reader (TAIPY_READER) has the permission to view the various entities, and related data in a data node
- A reader, however, cannot create, edit, delete an entity or edit the data in a data node manually. Readers are not permitted to submit tasks, pipelines or scenarios, subscribe or unsubscribe to an execution or cancel, pause or resume any job

## TAIPY_EDITOR

- An editor (TAIPY_EDITOR) has the permission to view, create, edit and delete the various entities and related data in data node
- An editor, however, cannot execute any task, pipeline or scenario, subscribe or unsubscribe to an execution or cancel, pause or resume any job

## TAIPY_EXECUTOR

- An executor (TAIPY_EXECUTOR) has the permission to view the various entities, and related data in data node, submit tasks, pipelines or scenarios for execution, subscribe or unsubscribe an execution, and cancel, pause or resume any job
- An executor, however, cannot create, edit or delete the various entities, and related data in data node

## TAIPY_ADMIN

- An admin (TAIPY_ADMIN) is not restricted at all. An admin be able to perform all actions available to other roles with no restrictions


# UI page access

TODO
