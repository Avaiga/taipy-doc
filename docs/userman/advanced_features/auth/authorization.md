---
title: Authorization and Roles
---

!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

Authorization is the process of driving the application logic differently
depending on the user using it: after a user is identified (see
the [Authentication section](authentication.md)), several roles may have
been assigned to that user, in a `Credentials^` object.

In Taipy Enterprise, authorization deals with ensuring a given user
is granted some access rights to a given resource, or that different
pages are displayed depending on that user's profile.


# Role Traits

Role traits are features associated to a role or a combination of roles.
They can be any object the application needs to adapt its logic to a given
configuration of roles for a given authenticated user.<br/>
A *Role Traits* can be any value an application may use to drive
its logic. Traits are defined by the application and are selected using
role traits filters given an authenticated user with a specific role
set configuration.

## Basic example

Say your application needs to test if some group of users (identified by
their credentials) is allowed to perform a given task. This group is
given a specific role: "MagicRole".<br/>
The application should allow users that have the "MagicRole" role to
do something, and prevent the others from doing so.

We can create a role traits filter that does just that:
```
access_filter = AnyOf("MagicRole", True, False)
```
Calling the `(RoleTraits.)get_traits()^` method of this filter
with credentials that hold the "MagicRole" role will return the value
True (the *success* value).<br/>
False (the *failure* value) is returned if the credentials do not have the
"MagicRole" role.

Let's create a user and see what happens:
```
user = login("<username>", "<password>")
if access_filter.get_traits(user):
    # Access is granted
else:
    # Access is denied
```
The test is straightforward because the traits are as simple as a Boolean value.<br/>
Depending on the user identity, the application follows one path or
the other.

## Access control

A typical use case where role traits are valuable is access control. Role traits filters
can be combined to provide a value for role traits depending on the roles assigned to
users.

Let's imagine that your application needs to manipulate two types of
resources: *Document* et *Post*. Resources have access rights
specific to their nature.

A *Document* can be read or modified.
```
class Document(Resource):
    CAN_READ = 1
    CAN_MODIFY = 2
```
We create two integer values that can be combined to represent the
access rights users may be granted for that resource type.

A *Post* can be published or deleted.
```
class Post(Resource):
    CAN_PUBLISH = 1
    CAN_DELETE = 2
```

In this situation, the role traits are a combination of
access right flags, for each resource type.<br/>
Here are the roles that we plan to handle:

   - "publisher": can read documents and can publish or delete posts.
   - "editor": can read and write documents but has no access to posts.
   - "reviewer": can read documents and delete posts.

No access rights are granted if a user has none of these three roles.

Here is how we could define the role traits filters for these two resource
types, based on the requirements above:
```
class Document(Resource):
    ...
    access_filter = AnyOf(["publisher", "reviewer"], CAN_READ,
                          AnyOf("editor", CAN_READ|CAN_MODIFY, 0))

class Post(Resource):
    ...
    access_filter = AnyOf("publisher", CAN_PUBLISH|CAN_DELETE,
                          AnyOf("reviewer", CAN_DELETE, 0))
```
Access rights are combined at the resource level so the role traits reflect
what roles are granted what access rights as a combination of flags.

In the body of the functions that perform the protected operation, we can
check if users have the relevant access rights:
```
class Document(Resource):
    ...
    def read(self, credentials, ...):
        if Document.access_filter.get_traits(credentials) & Document.CAN_READ:
            # Grant access
        else:
            # Access is prohibited
    def modify(self, credentials, ...):
        if Document.access_filter.get_traits(credentials) & Document.CAN_MODIFY:
            # Grant access
        else:
            # Access is prohibited

class Post(Resource):
    ...
    def publish(self, credentials, ...):
        if Post.access_filter.get_traits(credentials) & Post.CAN_PUBLISH:
            # Grant access
        else:
            # Access is prohibited
    def delete(self, credentials, ...):
        if Post.access_filter.get_traits(credentials) & Post.CAN_DELETE:
            # Grant access
        else:
            # Access is prohibited
```

You can then invoke `Document.read()`, `Document.modify()`, `Post.publish()` or
`Post.delete()` with the credentials of the user that is using the application.
The proper logic will be applied depending on the user's roles.

## Role traits value

Role traits can be any sort of value, even functions.

Here is some code to demonstrate this:
```
us_figure = ...
emea_figure = ...
apac_figure = ...

def results_for_exec():
  return f"Worldwide: {us_figure+emea_figure+apac_figure}"

def results_for_sales():
  return f"US: {us_figure}, EMEA: {emea_figure}, APAC: {apac_figure}"

def results_for_others():
  return f"This information is not available"

result_filter = AnyOf("exec", results_for_exec,
                      AnyOf("sales", results_for_sales, results_for_others))
```

We define three different functions, that return a string representing
figures for a company, in different regions.

Users are registered so that the company executives, and only them, are assigned
the "exec" role. Every member of the Sales team has the "sales" role.

The company executives really care about the overall figures, may be not
the regional data at this point. So the information is just the aggregation
of the regional figures.<br/>
The *result_filter* role traits filter indicates that if a user has
the "exec" role, the informative string should be the result of calling
*results_for_exec*.

Other users, if they have the "sales" role will see the result of calling
*results_for_sales*.

Finally, users that have neither the "exec" nor the "sales" roles will be
presented the result of the *results_for_others* function.

Now if a user is authenticated with the *user* credentials, printing
the relevant information is done with the following code:
```
print(f"Results: {result_filter.get_traits(user)()}")
```
The role traits are retrieved from the filter for that particular user.
Because we know these traits are a function, we evaluate it, so we get the
expected string at the end of the journey.

Note that is a user has both the "exec" and the "sales" roles (the CSO, COO
or CFO might), the filter is built so that this user only gets the Exec level
information output.

# Role Traits for GUI pages

Taipy GUI Enterprise edition uses role traits to select pages that user can display.

The `AuthorizedPage^` class lets you specify a role traits filter where both the
*success* and *failure* cases must be a page renderer (an instance of `Markdown^`,
`Html^`, or `(taipy.)gui.builder.Page^` instance - see the
[section on Page Renderers](../../gui/pages/index.md#defining-the-page-content) for more
information).<br/>
Instead of calling `Gui.add_page()` for the page renderer, you will use the same API,
providing the defined `AuthorizedPage^` instance.</br>
When the requested page is an `AuthorizedPage^`, the role traits filter is triggered
so that the relevant page renderer is used to display the page that the user can see
and interact with.

The documentation for `AuthorizedPage^` shows an example of how to use
this functionality.

# Permissions for Scenario and Data Management

You can control the access to the functionalities exposed by The Taipy entities
(Data nodes, Tasks, scenarios, ...).

Taipy Scenario and Da uses four predefined user roles names that can be assigned to users.
Each of these predefined roles provide a different set of capabilities and are described
in details below.

!!! note
    "Caution: If the application relies on the LDAP authentication, note that Taipy does
    not provide functions to populate the predefined user roles to the user's LDAP server.
    The user is expected to populate the roles themselves."

## "TAIPY_READER"

- A *reader* ("TAIPY_READER" role) has the permission to view the various entities and
  related data in a data node.
- A *reader*, however, cannot create, edit, delete an entity or edit the data in a data
  node manually. Readers are not permitted to submit tasks, sequences, or scenarios,
  subscribe or unsubscribe to an execution or cancel, pause or resume any job.

## "TAIPY_EDITOR"

- An *editor* ("TAIPY_EDITOR" role) has the permission to view, create, edit and delete
  the various entities and related data in data node.
- An *editor*, however, cannot execute any task, sequence, or scenario, subscribe or
  unsubscribe to an execution or cancel, pause or resume any job.

## "TAIPY_EXECUTOR"

- An *executor* ("TAIPY_EXECUTOR" role) has the permission to view the various entities,
  and related data in the data node, submit tasks, sequences or scenarios for execution,
  subscribe or unsubscribe an execution, and cancel, pause or resume any job.
- An *executor*, however, cannot create, edit or delete the various entities, and
  related data in data node.

## "TAIPY_ADMIN"

- An *admin* ("TAIPY_ADMIN" role) is not restricted at all.<br/>
  An *admin* is able to perform all actions available to other roles with no
  restrictions.
