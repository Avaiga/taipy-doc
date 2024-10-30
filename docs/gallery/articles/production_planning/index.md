---
title: Production Planning
category: decision_support
data-keywords: optimization scenario cycle comparison enterprise
short-description: Simulate manufacturing scenarios and optimize production quantities to reduce production costs.
order: 8
img: production_planning/images/production-planning-data-visualization.png
---

All manufacturers must generate a production plan over a given horizon (here, several
months). The objectives are to produce an optimized plan that respects the plant's
capacity constraints. The Optimization step ensures that the plan meets as much of the
demand as possible while minimizing production costs.

Although small, this example perfectly illustrates the basic requirements. The
application presented here can easily be extended to cater to more complex real use cases.


!!! note "Taipy Enterprise edition"

    Taipy provides robust, business-focused applications tailored for enterprise environments. To
    maintain standards of security and customization, these applications are proprietary like this
    application. If you’re looking for solutions that are immediately deployable and customizable
    to your business needs, we invite you to try them out and contact us for more detailed
    information.

    [Try it live](https://production-planning.taipy.cloud/Data-Visualization){: .tp-btn target='blank' }
    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

![New scenario](images/production-planning-Scenario-Manager-new-scenario.png){width=90% : .tp-image-border }

# Understanding the Application

The application consists of five pages accessible via the left panel by expanding the menu list.
The problem revolves around planning production for two finished products:
FPA (a wooden table) & FPB (a wooden stool). Each Finished Product is crafted
from two raw products: RPA (oak wood) and RPB (pine planks).
In this demo, an optimization algorithm, based on the PuLP open-source math solver,
determines the optimal production levels for FPA & FPB, minimizing costs while
adhering to specific production constraints (explained below).

## Page 1: Data Visualization

The primary chart depicts future demand for finished products A (FPA)
and B (FPB) over the next 11 months, with the current month marked as month 0.

![Data Visualization](images/production-planning-data-visualization.png){width=90% : .tp-image-border }

Just above the chart, by clicking "Expand here," you can access an you can
access an expandable block containing the initial production data at time
0 (current month): stock & production levels, incoming raw material orders,
and demand, all presented in a table.

## Page 2: Scenario Manager

Create, configure, and optimize production scenarios.
This is the application's main page, where users can create new scenarios,
adjust scenario parameters (on the 'Scenario Configuration' side of the page),
and re-submit scenarios for re-optimization based on modified parameters.
Initially, no scenario is available, and the Year/Month corresponds to the current month.


![No scenario](images/production-planning-Scenario-Manager-no-scenario.png){width=90% : .tp-image-border }

### Creating scenarios

The purpose of the model is to generate a production plan (level of production
for both products) for the next 11 months in order to:
- Meet the demand for the finished product
- Respect the Capacity Constraints
- Minimize 2 cost functions:
    - Back ordering costs: the costs of not meeting the demand on time
    - Stock costs: costs of storing raw and finished products.
It is worth noting that these 2 cost functions are kind of opposite:
if I have a lot of stock, I should easily meet the demand. Conversely,
a low inventory may put the demand in jeopardy.
When creating a first scenario, two key indicators , "Back Order Cost"
and "Stock Cost," appear above an empty main chart (no plan generated yet)..


![New scenario](images/production-planning-Scenario-Manager-new-scenario.png){width=90% : .tp-image-border }

Click on "New Scenario" to launch the optimization algorithm, which
quickly finds the optimal production levels, respecting the capacity
constraints and optimizing costs.
Results can be displayed as time series or pie charts, and different
graphs can be selected by choosing the data to display (costs, productions, etc.).


### Editing parameters

On the right-hand side of this panel, you can modify various parameters categorized into
three sections:

- **Capacity Constraints**: Modify capacity values for different products (finished and raw).
- **Objectives Weights**: Emphasize minimizing a specific cost (stock or backordering).
- **Initial Parameters**: Modify other parameters like Initial Stock and Unit Cost.
By "Playing" with these parameters, you can create several scenarios.

## Page 3: Compare Scenarios

To Compare two scenarios, select them then click on the "compare scenario" button.
You can select different comparison metrics  such as costs, purchases, and production levels, etc.


![Compare scenario](images/production-planning-Compare-Scenario.png){width=90% : .tp-image-border }

## Page 4: Compare Cycles

This demo also introduces the concept of ‘Cycles".
In this manufacturing context, the cycle is monthly.
This implies that scenarios are created each month.
Only one of the generated scenarios will be chosen as the
‘official scenario’, this scenario is referred as the "Primary" scenario.

This demo already contains many scenarios generated from the
previous months. The "Evolution of costs" bar chart displays
the performance for every single "primary’ scenario generated
every month for the past few years. Compare monthly stock and
backorder costs from January 2021 to the present month using stacked bar charts.


![Compare Cycles](images/production-planning-Compare-Cycles.png){width=90% : .tp-image-border }

## Page 5: Data sources

Access and display various tables associated with a selected scenario.
Conveniently download data tables in CSV format.

![Databases](images/production-planning-databases.png){width=90% : .tp-image-border }
