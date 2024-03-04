!!! warning "Available in Taipy Enterprise edition"

    This chapter is relevant only to the Enterprise edition of Taipy.

The Enterprise edition of Taipy has additional features that let applications
authenticate users and behave differently depending on the identity of the
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

[:material-arrow-right: Authentication in Taipy Enterprise](authentication.md)

[:material-arrow-right: Authorization in Taipy Enterprise](authorization.md)
