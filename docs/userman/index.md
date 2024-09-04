This User Manual covers all the topics and concepts that you can find in Taipy. For each topic,
we are trying to provide as many examples as possible so that you as a Taipy user can perform a
specific task.

If you are just starting with Taipy, you may want to look at the
[Getting Started](../tutorials/getting_started/index.md) in order to see a step-by-step example of a
complete Taipy application.

!!! note "Supported Python versions"

    Taipy requires **Python 3.8** or newer.

# Quick Access

These topics are the most visited ones, we thought you’d like to have a glance at them!

<div class="tp-row tp-row--gutter-sm">
  <div class="tp-col-12 tp-col-md-6 d-flex">
    <a class="tp-content-card tp-content-card--beta" href="../refmans/gui/viselements/">
      <header class="tp-content-card-header">
        <img class="tp-content-card-icon" src="../images/icons/visual-element-w.svg">
        <h3>Visual elements</h3>
      </header>
      <p>
        Browse dozens of Taipy GUI controls to build your UI
      </p>
    </a>
  </div>
  <div class="tp-col-12 tp-col-md-6 d-flex">
    <a class="tp-content-card tp-content-card--alpha" href="../refmans/gui/viselements/generic/chart/">
      <header class="tp-content-card-header">
        <img class="tp-content-card-icon" src="../images/icons/bar-chart-w.svg">
        <h3>Charts</h3>
      </header>
      <p>
        An important component of Taipy GUI with almost infinite possibilities right at your fingertips.
      </p>
    </a>
  </div>
</div>

# Graphical User Interface (GUI)

As part of Taipy, the `taipy.gui` package allows you to design an effective Graphical User Interface.
It provides many interactive widgets, controls, and visual elements to enhance the
user’s experience.

[:material-arrow-right: GUI User Manual](gui/index.md)

# Scenario features

Taipy is a Python library designed to build powerful and customized data-driven applications.
In particular, it provides the necessary tools to help Python developers transform their
data science analysis and algorithms into complete full stack applications.

As part of Taipy, the `taipy.core` package brings algorithm management to another level
speeding the developer work and empowering its end-users letting them manage their
user-defined scenarios with interactive data and smart job orchestration.

[:material-arrow-right: Data integration](scenario_features/data-integration/index.md),

[:material-arrow-right: Task orchestration](scenario_features/task-orchestration/index.md),

[:material-arrow-right: What-if-analysis](scenario_features/what-if-analysis/index.md)

[:material-arrow-right: Scenario and data management](scenario_features/sdm/index.md)

The `taipy.rest` package allows you to access some Taipy functionalities such as
scenarios management, sequences and task orchestration, data management, etc. through
a dedicated REST API.
This feature to provides a solution to easily integrate Taipy applications with other IT
systems. The API comes with multiple endpoints for you to work with Scenario and data
management conveniently and efficiently.

[:material-arrow-right: Taipy REST User Manual](advanced_features/rest/index.md)

# Authentication and Role

Taipy Enterprise Edition provides a simple and secure way to authenticate users and
manage their roles.

[:material-arrow-right: Authentication and Roles](advanced_features/auth/index.md)
