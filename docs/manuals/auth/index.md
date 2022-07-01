!!! warning "Available in Taipy Enterprise edition"

    This chapter is relevant only to the Enterprise edition of Taipy.

The Enterprise edition of Taipy has additional features that let applications
authentify users and behave differently depending on the identify of the
end-user.

The process of changing the application logic depending on the identify of
the user using the application is two-fold:

   - Authentication: the process that verifies that a user is known to
     the system. This is perform by a *login* step, that creates an instance
     of the `Credentials^` class. That instance holds all the information relevant
     for a given user, whose identity has been usually verified using a password.<br/>
     Credentials hold a set of roles, identified as strings, that the application
     can use to change its logic.

   - Authorization: Once a user is identified, the application can use the
     roles that are assigned to the user in order to change its logic, such
     as allowing a set of operations or preventing the user from performing
     certain tasks.

Please refer to the following section to get more information:

[:material-arrow-right: Authentication in Taipy Enterprise](authorization.md)

[:material-arrow-right: Authorization in Taipy Enterprise](authorization.md)


# Roles

Taipy has four predefined user roles names that can be assigned to users. Each of these predefined roles provide a different set of capabilities and will be described in details below.

!!! warning
    "Caution: Please note that Taipy does not provide functions to populate the predefined user roles to the user's LDAP server. The user is expected to populate the roles themselves."

## "TAIPY_READER"

- A reader ("TAIPY_READER") has the permission to view the various entities, and related data in a data node
- A reader, however, cannot create, edit, delete an entity or edit the data in a data node manually. Readers are not permitted to submit tasks, pipelines or scenarios, subscribe or unsubscribe to an execution or cancel, pause or resume any job

## "TAIPY_EDITOR"

- An editor ("TAIPY_EDITOR") has the permission to view, create, edit and delete the various entities and related data in data node
- An editor, however, cannot execute any task, pipeline or scenario, subscribe or unsubscribe to an execution or cancel, pause or resume any job

## "TAIPY_EXECUTOR"

- An executor ("TAIPY_EXECUTOR") has the permission to view the various entities, and related data in data node, submit tasks, pipelines or scenarios for execution, subscribe or unsubscribe an execution, and cancel, pause or resume any job
- An executor, however, cannot create, edit or delete the various entities, and related data in data node

## "TAIPY_ADMIN"

- An admin ("TAIPY_ADMIN") is not restricted at all. An admin be able to perform all actions available to other roles with no restrictions


# UI page access

TODO
