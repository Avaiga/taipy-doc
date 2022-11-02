---
hide:
  - navigation
---


# Welcome to Taipy Documentation!

Taipy is an innovative **low-code** package to create complete applications.

This documentation is divided in three main sections:

- [**"Getting Started"**](getting_started/index.md) provides a step-by-step introduction to Taipy. Taipy features are leveraged as the application becomes more and more complex.
- [**"User Manual"**](manuals/about.md) describes the main concepts for Taipy GUI, Taipy Core and Taipy REST. It also  provides information on the deployment of your Taipy app.
- [**"Reference Manual"**](manuals/reference) documents all the Taipy APIs.

Taipy requires *Python 3.8* or newer.

## Quick access

These topics are the most visited ones, we thought you’d like to have a glance at them!

<div class="tp-row tp-row--gutter-sm">
  <div class="tp-col-12 tp-col-md-6 tp-col-lg-4 d-flex">
    <a class="tp-content-card" href="getting_started/">
      <img class="tp-content-card-icon icon-light" src="images/icons/flag-w.svg">
      <img class="tp-content-card-icon icon-dark" src="images/icons/flag.svg">
      <h3>Getting started</h3>
      <p>
        This tour shows you how to create an entire application using the two main components of Taipy.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>
  <div class="tp-col-12 tp-col-md-6 tp-col-lg-4 d-flex">
    <a class="tp-content-card" href="manuals/about/">
      <img class="tp-content-card-icon icon-light" src="images/icons/menu_book-w.svg">
      <img class="tp-content-card-icon icon-dark" src="images/icons/menu_book.svg">
      <h3>Reference Manual</h3>
      <p>
        Get your hands on using Taipy, guided by examples.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>
  <div class="tp-col-12 tp-col-md-6 tp-col-lg-4 d-flex">
    <a class="tp-content-card" href="manuals/gui/">
      <img class="tp-content-card-icon icon-light" src="images/icons/dashboard-w.svg">
      <img class="tp-content-card-icon icon-dark" src="images/icons/dashboard.svg">
      <h3>User interface</h3>
      <p>
        Taipy GUI provides controls and other elements to create powerful Web apps in minutes.
      </p>
      <span class="tp-content-card-readmore">Read more</span>
    </a>
  </div>
</div>

## Browse dozens of controls to build your UI!

<ul class="tp-pills-list">
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/button/">
      <span>Button</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/button-d.png" alt="">
        <p>A control that can trigger a function when pressed.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/chart/">
      <span>Chart</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/chart-d.png"/>
        <p>Displays data sets in a chart or a group of charts.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/date/">
      <span>Date</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/date-d.png"/>
        <p>A control that can display and specify a formatted date, with or without time.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/image/">
      <span>Image</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/image-d.png"/>
        <p>A control that can display an image.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/viselements/indicator/">
      <span>Indicator</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/indicator-d.png"/>
        <p>Displays a label on a red to green scale at a specific position.</p>
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
    <a class="tp-pill" href="manuals/gui/viselements/menu/">
      <span>Menu</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/menu-d.png"/>
        <p>Shows a left-side menu.</p>
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
    <a class="tp-pill" href="manuals/gui/viselements/table/">
      <span>Table</span>
      <div class="tp-tooltip">
        <img src="manuals/gui/viselements/table-d.png"/>
        <p>Displays a data set as tabular data.</p>
      </div>
    </a>
  </li>
  <li>
    <a class="tp-pill" href="manuals/gui/controls/">
      <span>…</span>
      <div class="tp-tooltip">
        <p>Browse the complete list of visual elements.</p>
      </div>
    </a>
  </li>
</ul>

## How does it work?

Taipy is composed of two main independent components: **Taipy Core** and **Taipy GUI**. You can use either component independently. However, as you will see, they are incredibly efficient when combined.

<div class="tp-row" style="margin-top: 2rem; margin-bottom: 2rem">
  <div class="tp-col-12 tp-col-md">
    <article class="tp-content-card">
      <h3>Taipy GUI</h3>
      <p>
        The <strong>Graphical User Interface</strong> of Taipy allows anyone with basic knowledge of Python to create a beautiful and interactive interface. It is a simple and intuitive way to create a GUI. No need to know how to design web pages with CSS or HTML. Taipy uses an augmented Markdown syntax to create your desired Web page.
      </p>
    </article>
    <article class="tp-content-card">
      <h3>Taipy Core</h3>      
      <p>
        A simple yet powerful <strong>pipeline orchestration</strong> package.<br>
        Some of the key features:
      </p>
      <ul>
        <li>Intuitive DAG modeling</li>
        <li>Smart scheduling</li>
        <li>Powerful data caching</li>
        <li>Scenario enabled pipelines</li>
        <li>KPI Tracking</li>
      </ul>
    </article>
  </div>

  <div class="tp-col-12 tp-col-md-auto">
    <figure align="center">
      <img alt="Taipy structure" src="images/taipy-structure-vector.svg" width="350">
    </figure>
  </div>

</div>

Other packages offer additional functionality, such as a **REST API** that allows for deploying Taipy Core applications as a Web service.
