---
hide:
  - navigation
---

# Welcome to Taipy

Taipy is a helpful open-source Python library for improving both the front-end and back-end of your applications. It's designed to make it easy to create interactive, multi-page dashboards with enhanced Markdown content. Even if you're not an expert in web development, you can use this web application builder to create dynamic interfaces quickly and easily.

At the same time, Taipy is designed specifically for creating data-driven back-end applications. It comes with built-in components that make it easy to organize and control how data is accessed and managed. This feature, called "Scenario Management," requires very little setup in Python.

With Taipy Studio, a graphical configuration editor, setting up your scenarios (which include data flows and pipelines) has become much simpler. This tool offers a user-friendly interface where you can easily drag and drop elements, customize layouts, and integrate features effortlessly.

Taipy is a versatile tool that enables both individuals and businesses to create applications without needing advanced coding skills. One of its key benefits is how it speeds up development for both the front-end and back-end aspects, covering everything from initial prototypes to fully scalable, ready-to-use applications.

**Front-End Functionalities:**

- Creating a user interface requires a solid grasp of Python programming fundamentals.
- Taipy is purposefully engineered to prioritize user-friendliness, resulting in a straightforward and intuitive process of user interface creation.
- No prior knowledge of web design is necessary, and it eradicates the need for any prerequisites related to CSS and HTML.
- Leveraging augmented Markdown syntax, Taipy GUI aids users in seamlessly generating their desired web pages.

**Back-End Functionalities:**

- Taipy provides extensive support for establishing resilient pipelines capable of managing diverse scenarios.
- The process of modeling Directed Acyclic Graphs (DAGs) is simplified through Taipy Studio.
- Enhancing the overall performance of Taipy applications, data caching, parallel executions of tasks, data source scoping are all integrated.
- Providing a registry of pipeline executions.
- Enabling pipeline versioning.
- Taipy equips users with the ability to monitor and assess the performance of their applications using the KPI tracking tool.
- Furthermore, Taipy offers  built-in graphical explorers  for visualizing your ‘executed’ pipelines and their associated data.

## Overview of Taipy

The subsequent schematic diagram illustrates the complete sequence encompassing all stages within the Taipy flow.

  <div class="tp-col-12 tp-col-md-auto">
    <figure align="center">
      <img alt="Taipy structure" src="images/taipy-flow-updated.png" >
    </figure>
  </div>

## Quick Access

These frequently visited topics have been highlighted for your quick reference.

<div class="tp-row tp-row--gutter-sm">
  <div class="tp-col-12 tp-col-md-6 d-flex">
    <a class="tp-content-card" href="getting_started/">
      <header class="tp-content-card-header">
        <img class="tp-content-card-icon icon-light" src="images/icons/flag-w.svg">
        <img class="tp-content-card-icon icon-dark" src="images/icons/flag.svg">
        <h3>Getting Started</h3>
      </header>
      <p>
        This guide covers all the important steps and concepts in Python web application development. It's useful for both beginners and experienced Python programmers who are trying out Taipy for the first time.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>
  <div class="tp-col-12 tp-col-md-6 d-flex">
    <a class="tp-content-card" href="manuals/gui/">
      <header class="tp-content-card-header">
        <img class="tp-content-card-icon icon-light" src="images/icons/dashboard-w.svg">
        <img class="tp-content-card-icon icon-dark" src="images/icons/dashboard.svg">
        <h3>User interface</h3>
      </header>
      <p>
        Taipy GUI gives you the tools and elements you need to create strong web apps quickly. It empowers developers by offering a powerful tool for visually designing user interfaces. You can organize user interface elements and use style kits to make your apps look great.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>
  <div class="tp-col-12 tp-col-md-6 d-flex">
    <a class="tp-content-card" href="manuals/gui/viselements/chart/">
      <header class="tp-content-card-header">
        <img class="tp-content-card-icon icon-light" src="images/icons/bar-chart-w.svg">
        <img class="tp-content-card-icon icon-dark" src="images/icons/bar-chart.svg">
        <h3>Charts</h3>
      </header>
      <p>
        One crucial part of Taipy's graphical user interface (GUI) is its graphing library. This library offers a wide range of customizable ways to visualize data. You can access these features through Taipy's chart control, which is closely connected to how it's implemented behind the scenes.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>
  <div class="tp-col-12 tp-col-md-6 d-flex">
    <a class="tp-content-card" href="manuals/core/concepts/scenario/">
      <header class="tp-content-card-header">
        <img class="tp-content-card-icon icon-light" src="images/icons/menu_book-w.svg">
        <img class="tp-content-card-icon icon-dark" src="images/icons/menu_book.svg">
        <h3>Scenario</h3>
      </header>
      <p>
        Taipy Scenario represents a specific business problem that you solve using data and different sets of parameters. This feature lets you create different versions of the same problem with different assumptions, which is really helpful for making decisions when you need to analyze the potential impact of different scenarios.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>  
</div>

## Build your UI with dozens visual elements

Taipy provides components in open-source Python libraries that are important for building web applications.
Below, you'll find a clear explanation of each term, explained in the context of the Taipy web application builder.

<ul class="tp-pills-list">
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/chart/">
      <span>Chart</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/chart-d.png"/>
        <p>A chart visually depicts data through graphs, charts, or plots.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/table/">
      <span>Table</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/table-d.png"/>
        <p>A table presents data in rows and columns, often used in web applications for structured data display and interaction.</p>
      </div>
    </a>
  </li> 
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/button/">
      <span>Button</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/button-d.png" alt="">
        <p>You can employ this class name to target the buttons on your page and apply styling.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/input/">
      <span>Input</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/input-d.png"/>
        <p>A control that displays some text that can potentially be edited.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/slider/">
      <span>Slider</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/slider-d.png"/>
        <p>Displays and allows the user to set a value within a range.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/controls/">
      <span>…</span>
      <div class="tp-tooltip">
        <p>Browse the complete list of visual elements.</p>
      </div>
    </a>
  </li>
</ul>

## Main Taipy functionalities

<ul class="tp-pills-list">
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/blocks/">
      <span>Structure Pages</span>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/core/config/scenario-config/#from-task-configs">
      <span>Configure Scenario</span>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/core/entities/scenario-creation/">
      <span>Instantiate Scenario</span>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/core/entities/orchestrating-and-job-execution/#submit-a-scenario-sequence-or-task/">
      <span>Submit Scenario</span>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/core/versioning/">
      <span>Manage versions</span>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/cli/">
      <span>Taipy command-line interface (CLI)</span>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/rest/">
      <span>Expose Taipy's REST APIs</span>
    </a>
  </li>
    <li>
    <a class="tp-pill" href="manuals/about/">
      <span>…</span>
      <div class="tp-tooltip">
        <p>Browse the complete list of features.</p>
      </div>
    </a>
  </li>
</ul>
