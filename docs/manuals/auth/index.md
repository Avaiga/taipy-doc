!!! warning: "Only available in enterprise version"

# Taipy's Authentication and Authorization

## Pre-requisite

An LDAP server must be setup

## Config

Set up connection to your LDAP server with Taipy Config. Here are the configurable properties you can use:

- **Config.global_config.ldap_server**: The url of the ldap server.
- **Config.global_config.ldap_base_dn**: The base DN that the LDAP server uses to search for users authentication.
- **Config.global_config.jwt_secret**: The secret for the JWT token.
- **Config.global_config.jwt_expire**: The period after which the JWT token provided by Taipy will be expired.
- **Config.global_config.auth_enabled**: The field to enable/disable Taipy authentication and authorization. Its default value is `True`, meaning that the enterprise version, by default, will have authentication and authorization feature enabled.

Example of configuring LDAP server connection in Taipy:

```
Config.global_config.ldap_server = "ldap://0.0.0.0"
Config.global_config.ldap_base_dn = "dc=example,dc=org"
Config.global_config.jwt_secret = "my-32-character-ultra-secure-and-ultra-long-secret"
Config.global_config.jwt_expire = 600   #for 10 minutes
Config.global_config.auth_enabled = True
```

## Roles

Explain different roles in Taipy


### Taipy.READER

If the authorization feature is activated:
- A reader (TAIPY_READER) should have the right to view the various entities, and related data in a data nodes.
- A reader, however, cannot create, edit, delete an entity, or edit the data in a data node manually. They also cannot execute tasks, pipelines or scenarios, subscribe/unsubscribe to an execution, and cancel, pause or resume any jobs.


### Taipy.EDITOR

If the authorization feature is activated
- An editor (TAIPY_EDITOR) should have the right to view, create, edit or delete the various entities, and related data in data nodes.
- An editor, however, cannot execute any tasks, pipelines or scenarios, subscribe/unsubscribe to an execution, and cancel, pause or resume any jobs.


### Taipy.EXECUTIONER

If the authorization feature is activated:
- An executor (TAIPY_EXECUTOR) should have the right to view the various entities and related data in data nodes, submit tasks, pipelines or scenarios for execution, subscribe/unsubscribe an execution, and cancel, pause or resume any jobs.
- An executor, however, cannot create, edit or delete the various entities, and related data in data nodes.


### TAIPY.ADMIN

If the authorization feature is activated, a TAIPY_ADMIN should not be restricted at all. He/she should be able to perform all actions available to other roles with no restriction.


## UI page access
