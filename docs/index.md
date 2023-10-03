---
hide:
  - navigation
  - toc
---

# Welcome to Taipy Documentation!

Taipy is an open-source library to easily develop data-driven web applications in pure Python.

Taipy is a versatile tool suitable for developers and businesses, regardless of their coding 
expertise. Taipy covers both front-end and back-end requirements to expedite application 
development, from initial prototypes to production ready solutions.

- **User interface creation:** 
  Design user interfaces effortlessly. You don't need prior web design knowledge to create 
  interactive multi-page applications. With extended Markdown syntax, you can craft dynamic 
  web pages with ease. No knowledge of web development is required!

- **Pipeline orchestration:**
  With data caching, parallel task execution, and data source scoping Taipy makes it efficient 
  for developers to model complex pipelines and for end-users to visualize, run, and monitor them.

- **Scenario and data management:**
  Taipy is designed specifically for data-driven applications. Setting up scenarios, orchestrating 
  data flows and pipelines, and accessing data requires minimal Python setup.

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
        In this guide, you will build a complete Taipy web application step by step. It covers 
some of the important concepts in Taipy. It's useful for both beginners and experienced Python 
programmers who are trying out Taipy for the first time.
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
        This is Taipy GUI user manual. It describes the concepts and elements you need to create 
strong web apps quickly. From GUI pages, controls, blocks, visual elements, binding Python 
variables, callbacks, styling, extending Taipy, etc. Also, for our users working on Notebooks, 
we do provide information on how to run Taipy from Notebooks.
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
        One crucial part of Taipy's graphical user interface (GUI) is its graphing library. This 
library offers a wide range of customizable ways to visualize data.
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
        Taipy Scenario represents a specific business problem (modeled as a pipeline) that you 
solve using data and different sets of parameters. Scenarios let you create different versions 
of the same problem with different assumptions, which is really helpful for making decisions 
when you need to analyze the potential impact of different scenarios.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>
</div>

## Build your UI with dozens of visual elements

Taipy provides many GUI components (referred to as "Taipy Controls") that are the essential 
bricks for building web applications. Below, you'll find a clear explanation of each term, 
explained in the context of the Taipy web application builder.

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
        <p>
          A table presents data in rows and columns, often used in web applications for structured 
          data display and interaction.
        </p>
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
