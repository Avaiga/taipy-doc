---
title : Release Notes
hide:
  - navigation
---

This is the list of changes to Taipy releases as they were published.

!!! note "Migration"

    Please refer to the [Migration page](./migration.md) for potential migration paths for your
    applications implemented on legacy Taipy versions.

!!! note "Legacy Releases"

    This page shows the changes that were made in the most recent major release of Taipy.<br/>
    If you are using a legacy version, please refer to the
    [Legacy Release Notes](relnotes-legacy.md) page.


## New Features

<h4><strong><code>taipy-core</code></strong> 3.1.0 </h4>

- The `DataNode.filter()^` method and the indexing/filtering style now also support filtering a
    Numpy array, a list of objects, and a list of dictionaries.<br/>
    For more information, refer to [Filter data node](./manuals/core/entities/data-node-mgt.md#filter-read-results).

- You can now append new data to a data node using the `DataNode.append()^` method. The method is
    available for `CSVDataNode`, `ExcelDataNode`, `JSONDataNode`, `ParquetDataNode`, `SQLDataNode`,
    `SQLTableDataNode`, and `MongoCollectionDataNode`.<br/>
    For more information, refer to [Append new data to a data node](./manuals/core/entities/data-node-mgt.md#append-new-data-to-a-data-node).

- A new class called `Submission^` was added. It holds the meta-data (such as its status or submission date)
    of all entities that are submitted: `Scenario^`, `Sequence^`, and `Task^`.</br>
    The function `taipy.get_latest_submission()^` was also added to retrieve the last submitted entity.
    For more information, refer to [TODO]().

- The `modin` exposed type as been deprecated. When used, a fallback on pandas is applied.
    For more information, refer to [issue #631](https://github.com/Avaiga/taipy/issues/631).

- New S3DataNode.
    For more information, refer to [TODO]().


## Improvements and changes

<h4><strong><code>taipy-core</code></strong> 3.1.0 </h4>

- Running the Core service more than one time will raise an exception to prevent
    multiple instances of the Core service to run at the same time.

## Significant bug fixes

<h4><strong><code>taipy-core</code></strong> 3.1.0 </h4>

- Can not write to a SQLDataNode or a SQLTableDataNode using examples provided by the
    documentation.<br/>
    See [issue #816](https://github.com/Avaiga/taipy-core/issues/816).
