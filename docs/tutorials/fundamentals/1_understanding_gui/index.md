---
title: Understanding GUI
category: fundamentals
data-keywords: gui vizelement chart navbar table layout part menu state multi-page callback markdown
short-description: Understand basic knowledge of Taipy GUI creating of a multi-page NLP application.
img: 1_understanding_gui/step_07/images/result.png
---
!!! note "Supported Python versions"

    Taipy requires **Python 3.8** or newer.

Welcome to the **Tutorial** for using Taipy frontend. This guide will demonstrate how to utilize
Taipy to build an interactive web application.

![GUI application](step_07/images/result.png){width=90% : .tp-image-border }

Taipy aims to simplify web application development:

- Accelerates application building.

- Streamlines management of variables and events.

- Offers intuitive visualization using Markdown syntax.

In each part of the **"Tutorial"** we'll emphasize the basic principles of *Taipy*. It's
important to note that each step builds on the code from the previous one. By the end of the
final step, you'll be equipped with the ability to create your own Taipy application.

## Before we begin

**Taipy** package requires Python 3.8 or newer;

``` console
$ pip install taipy
```

Once you finish step 5, the application will include a Natural Language Processing (NLP) algorithm
for demonstration purposes. Note that this algorithm is compatible only with Python versions 3.8
to 3.10. To incorporate this NLP feature, you'll need to install Transformers and Torch.
However, if you prefer, you can proceed with the tutorial guide without using this algorithm.

``` console
$ pip install torch
$ pip install transformers
```

!!! info

    `pip install taipy` is the preferred method to install the latest stable version of Taipy.

    If you don't have [pip](https://pip.pypa.io) installed, this
    [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/)
    can guide you through the process.

## Using Notebooks

This **Tutorial** is for Python scripts (*.py*) only. If you want to use **Jupyter Notebooks**,
download this [notebook](./tutorial.ipynb).

## Taipy Studio

[Taipy Studio](../../../manuals/studio/index.md) is a VS Code extension that provides an
auto-completion of Taipy visual elements. Creating a Taipy application can be done more easily
and quickly through Taipy Studio.

So, without further delay, let's begin to code!

## Steps

1. [First Web page](step_01/step_01.md)

2. [Visual elements](step_02/step_02.md)

3. [Interaction](step_03/step_03.md)

4. [Charts](step_04/step_04.md)

5. [Python expression in properties](step_05/step_05.md)

6. [Page layout](step_06/step_06.md)

7. [Multi-pages, navbars, and menus](step_07/step_07.md)
