This page explains how to use scenario comparators to compare alternative data between
scenarios.

# Main principles

In Taipy, comparing a scenario means comparing their data nodes. The global idea is to
use a user defined function that takes list of data to compare and returns a comparison
result. The function can return any data type, but the best is to format the comparison
results in a way it can easily be used in a visual element.

1. **Define a comparison function:**
    You can define a comparison function to compare specific data nodes of a scenario. For example
    a data node representing a KPI. The comparison function takes as input parameters the list of
    the data referred by the data nodes to compare and returns a comparison result.

2. **Configure the scenario comparator:**
    The comparison function is then added to the scenario configuration as a scenario comparator.
    For more details on how to configure scenarios, see the
    [scenario configuration](../sdm/scenario/scenario-config.md) page.

3. **Compare scenarios:**
    At runtime, you can compare the scenarios using the `taipy.compare_scenarios()` function. This
    function takes as input parameters the list of scenarios to compare and returns the comparison
    results.

4. **Visualize the comparison results:**
    The comparison results can be visualized using the various visual elements.
    For more details on how to configure scenarios, see the
    [visual elements](../gui/viselements/index.md) page. <br>

# Example

TODO

## User define function

TODO

## Configuration

TODO

## Comparison

TODO

## User interface

TODO
