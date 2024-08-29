Although Taipy applications are regular Python applications, there are
many use cases that you, as an application developer, can face when it comes
to developing, debugging, testing, and deploying.

The [section on Running a Taipy application](run/index.md) describes different
situations that you might be facing:

- Your application may be a one-shot run, computing a result dataset given input data
  to work on.<br/>
  This application would typically be a Python script that one can run when needed
  or executed by a job scheduler such as the Unix `cron` command.
- Your application may be running as a service: it then can be invoked multiple times,
  hosted by a server of some sort.
- Your application may be developed in a Notebook context, where pieces of code
  (*cells*) can be executed in a different order.

When you have decided how your application should be executed, you will undoubtedly
want to expose it to users.<br/>
The [section on Deploying a Taipy application](deploy/index.md) is here to help you
configure the system where you want the application to run:

- The application can run locally on your machine.<br/>
  It can, however, be exposed to external users through the Internet if that is something
  you need.
- Vendors provide different services that deal with computing, storage, database, and networking
  management.<br/>
  These offers can also be relevant to host your Taipy applications and
  provide them to external users.

## [Running a Taipy application](run/index.md)

## [Deploying a Taipy application](deploy/index.md)
