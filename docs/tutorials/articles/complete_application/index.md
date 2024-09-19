---
title: First Realistic application
category: fundamentals
data-keywords: gui vizelement chart state multi-page callback markdown scenario task storage_type scope datanode configuration
short-description: Build a complete realistic application from scratch from back-end to front-end.
order: 3
img: complete_application/step_04/images/result.png
---
!!! note "Supported Python versions"

    Taipy requires **Python 3.9** or newer.

This tutorial guide will walk you through creating a complete application from the front end to
the back end. You don't need any prior knowledge to complete this tutorial.

![Tutorial application](step_01/images/overview.gif){ width=90% : .tp-image-border }

Each step concentrates on fundamental ideas about *Taipy*.

## Objective of the Application

You are about to create a comprehensive multi-page application designed for data visualization,
predictive analytics, and comparative assessment. This app processes sales figures for display.
One of its dedicated pages allows you to use two predictive models where predictions can be
fine-tuned through some parameters. To round it off, the performance page offers a graphical
comparison of various predictive outcomes.

## Before we begin

Three packages have to be installed:

 1. **Taipy** package, it requires Python 3.9 or newer;

 2. **scikit-learn**: A Machine-Learning package that will be used in the Tutorial user code;

 3. **statsmodels**: Another package for statistics also used in the user code.

``` console
$ pip install taipy
$ pip install scikit-learn
$ pip install statsmodels
```

!!! info

    `pip install taipy` is the preferred method to install the latest stable version of Taipy.

    If you don't have [pip](https://pip.pypa.io) installed, this
    [Taipy installation guide](../../getting_started/installation.md)
    can guide you through the process.


Once Taipy is installed, you can use the CLI to scaffold an application folder. Run the create
command line with default application template and answer basic questions as follows:

``` console
> taipy create --application default
Application root folder name [taipy_application]:
Application main Python file [main.py]:
Application title [Taipy Application]:
Page names in multi-page application? []: data_viz scenario performance
Does the application use scenario management or version management? [No]: yes
Does the application use Rest API? [No]: no
```

So, without further delay, let's begin to code!

## Steps

1. [Data Visualization page](step_01/step_01.md)

2. [Algorithms used](step_02/step_02.md)

3. [Scenario Configuration](step_03/step_03.md)

4. [Scenario page](step_04/step_04.md)

5. [Performance page](step_05/step_05.md)
