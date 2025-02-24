---
hide:
  - toc
---
When the `Gui^` instance runs, it creates a web server that serves the
registered pages, with the root of the site located where the `__main__`
Python module file is located.<br/>
This allows malicious users to potentially access the files of your
application if those users know their path names: the main file of a Python
application is often called `main.py`, so anyone could request the
`http://<url:port>/main.py` and see your Python source code.<br/>
This can be even more dangerous if your application relies on data files
that are meant to remain private. If a user of your application happens
to discover the path to this file, the application has a security vulnerability
because this file can be directly accessed using the underlying
web server.

The way to solve that issue is to configure the application server to indicate
which requests are safe and which should be blocked.

Taipy GUI, however, comes with a simple feature that makes this configuration
far simpler: Located next to the main module of your application, you can create
a file called `.taipyignore` that lists files or directories that you want
to protect against a direct request.<br/>
The syntax of this text file is identical to the syntax used by Git
for its [`.gitignore`](https://git-scm.com/docs/gitignore) file.

If a user requests a file whose path matches one that appears in `.taipyignore`
then the Taipy web server returns an HTTP error 404 (Not Found), protecting
your file from being downloaded without your consent.
