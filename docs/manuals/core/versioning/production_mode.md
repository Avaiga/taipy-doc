When running a Taipy Core application in `--production` mode, Taipy can access all entities
attached to the current version or another _production_ version. It corresponds to the case where
the application is stable and running in a production environment.

In the following, we consider the basic Taipy Core application `main.py` for all our examples:
```python linenums="1"
{%
include-markdown "./code_example/main_with_changes.py"
comments=false
%}
```

# Convert an experiment version to production

To convert an _experiment_ version to a _production_, you can run the Taipy application
on your command line interface with `--production VERSION` option providing the version name.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
1.0                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ python main.py --production 1.0
[2023-01-25 13:00:05,333][Taipy][INFO] job JOB_my_print_algo_e25214c4-1047-4136-a5db-c1241a3ddbcf is completed.
nb scenarios: 3

$ taipy manage-versions --list
Version number                         Mode                   Creation date
1.0                                    Production (latest)    2023-01-25 13:00:05
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

In the example above, Taipy converted the version 1.0 to a _production_ version before
running it.

Without explicitly providing the version, the latest version of your application is
used. Here is another example:

```console
$ python main.py --experiment 2.0
[2023-01-25 13:05:17,712][Taipy][INFO] job JOB_my_print_algo_ac79138a-4c3a-4560-bbd4-f4975083bf83 is completed.
nb scenarios: 1

$ taipy manage-versions --list
Version number                         Mode                   Creation date
2.0                                    Experiment (latest)    2023-01-25 13:05:17
1.0                                    Production             2023-01-25 13:00:05
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ python main.py --production
[2023-01-25 13:06:00,871][Taipy][INFO] job JOB_my_print_algo_1fcb6feb-cef1-46e0-a818-4ae2e58df57d is completed.
nb scenarios: 5

$ taipy manage-versions --list
Version number                         Mode                   Creation date
2.0                                    Production (latest)    2023-01-25 13:06:00
1.0                                    Production             2023-01-25 13:00:05
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

As you can see, we first created an _experiment_ version named 2.0. One scenario is
attached to it. When listing the existing versions, we can see that 2.0 is the latest
version used. So when running the Taipy application in _production_ mode without
providing the version, the latest is used and converted to production before running.
Note that once the version is converted to _production_, the application accesses all
_production_ entities, including from older _production_ versions.


# Remove a production version

To remove a _production_ version, you can run on your command line interface a Taipy
application with the `--delete-production VERSION` option providing the version
name.

```console
$ taipy manage-versions --delete-production 2.0
Successfully delete version 2.0 from production version list.

$ taipy manage-versions --list
Version number                         Mode                   Creation date
2.0                                    Experiment (latest)    2023-01-25 13:06:00
1.0                                    Production             2023-01-25 13:00:05
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

After running the commands above, version 2.0 is an _experiment_ version again. It
is no longer a _production_ version.
