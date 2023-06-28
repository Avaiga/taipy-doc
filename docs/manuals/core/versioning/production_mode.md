When running a Taipy Core application in `--production` mode, Taipy can access all entities
attached to the current version or another *production* version. It corresponds to the case where
the application is stable and running in a production environment.

In the following, we consider the basic Taipy Core application `main.py` for all our examples:
```python linenums="1" title="main.py"
{%
include-markdown "./code_example/main.py"
comments=false
%}
```

# Convert an experiment version to production

To convert an experiment version to a production, you can run the Taipy application on the CLI with
`--production` option and providing the version name.

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

In the example above, Taipy converted the version 1.0 to a production version before running it.

Without explicitly providing the version name, the latest version of your application is used.
Here is another example:

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

As you can see, we first created an experiment version named 2.0 and there is one scenario is
attached to it. When listing the existing versions, we can see that 2.0 is the latest version used.
Therefore, when running the Taipy application in production mode without providing the version name,
the latest is used and converted to production before running.

Note that once the version is converted to production, the application can access all production
entities, including from older production versions.


# Remove a production version

To remove a production version, you can use the `taipy manage-versions` with the `--delete-production`
option on the Taipy CLI and providing the version name (see the
[Manage versions on Taipy CLI page](../../cli/manage-versions.md) for more details).

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

After running the commands above, version 2.0 is an experiment version again. It is no longer a
production version.
