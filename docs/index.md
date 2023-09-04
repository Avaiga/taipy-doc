---
hide:
  - navigation
---

# Welcome to Taipy

Taipy, an open-source Python library, is a potent asset for shaping your applications' front-end and back-end facets. Notably, it delivers an uncomplicated syntax designed to expedite the creation of interactive, multi-page dashboards enriched with augmented Markdown. This web application builder empowers the generation of dynamic interfaces without requiring proficiency in web development.

Simultaneously, Taipy is tailor-made to forge influential and tailored data-driven back-end applications. It offers automatic components that facilitate the organization and management of data access and flow orchestration. This capability, aptly termed Scenario Management, necessitates minimal Python configuration.

Employing Taipy Studio, a graphical configuration editor, configuring your scenarios (data flows) has never been more streamlined. This resource provides a user-centric interface that enables seamless drag-and-drop interactions, layout customization, and effortless feature integration.

For data scientists and developers alike, Taipy acts as a catalyst for successful Python endeavors. Whether your aim is a straightforward pilot or a comprehensive application within IDEs or Notebooks, Taipy equips you with all indispensable functionalities. Its architecture is meticulously crafted to truncate both development and deployment timelines significantly.

Taipy is a complete tool that empowers individuals and enterprises to develop applications without extensive coding expertise. A primary advantage of Taipy lies in its ability to expedite development across both front-end and back-end domains, encompassing everything from initial prototypes to fully scalable, production-ready applications.

**Front-End Functionalities:**

- Creating a user interface requires a solid grasp of Python programming fundamentals.
- Taipy is purposefully engineered to prioritize user-friendliness, resulting in a straightforward and intuitive process of user interface creation.
- No prior knowledge of web design is necessary, and it eradicates the need for any prerequisites related to CSS and HTML.
- Leveraging augmented Markdown syntax, Taipy GUI aids users in seamlessly generating their desired web pages.

**Back-End Functionalities:**

- Taipy provides extensive support for establishing resilient pipelines capable of managing diverse scenarios.
- The process of modeling Directed Acyclic Graphs (DAGs) is simplified through Taipy's functionality.
- Enhancing the overall performance of Taipy applications, the data caching feature is integrated.
- Facilitating a registry of pipeline executions.
- Enabling pipeline versioning.
- Taipy equips users with the ability to monitor and assess the performance of their applications using the KPI tracking tool.
- Furthermore, Taipy offers a built-in visualization feature for pipelines and their associated data.

## Overview of the Taipy Flow

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
        This guide comprehensively outlines key steps and concepts in Python web application development, catering to both novices and proficient Python programmers venturing into Taipy for the first time.
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
        Taipy GUI provides controls and other elements to create powerful web apps in minutes. Taipy GUI empowers developers with a robust tool for visually designing user interfaces by organizing user interface block elements and utilizing style kits.
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
        An essential facet of Taipy GUI, offering nearly boundless potential, Plotly is a graphing library that provides an extensive array of customizable visualizations for datasets, with these components accessible through Taipy's chart control, tightly linked to the underlying implementation.
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
        We introduce the essential notion of a Taipy Scenario, representing a singular business problem instance tackled using uniform data and parameter sets, allowing users to instantiate diverse versions of a problem with varying assumptions, an invaluable asset for decision-making in contexts demanding impact and what-if analysis.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>  
</div>

## Build your UI with dozens visual elements

Taipy offers components within open-source Python libraries that are instrumental for web application development.
Below, you'll find a succinct elucidation of each term, contextualized within the framework of the Taipy web application builder.

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
    <a class="tp-pill" href="manuals/core/entities/orchestrating-and-job-execution/#submit-a-scenario-pipeline-or-task/">
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
