---
hide:
  - navigation
---

# Installation

## Prerequisite

To run Taipy, Python (version 3.8 or above) and [pip][https://pip.pypa.io] are required. If you don't have `pip` installed, this [Python installation guide][http://docs.python-guide.org/en/latest/starting/installation/] can guide you through the process, or you can follow the [official installation page][https://pip.pypa.io/en/latest/installation/] of `pip`.

You can also install `pip` in a [Conda][https://docs.conda.io/projects/conda/en/latest/index.html] environment by using the following command:
``` console
$ conda install pip
```

## Stable release

To install Taipy, run this command in your terminal:

``` console
$ pip install taipy
```

!!! info "This is the preferred method to install Taipy, as it will always install the most recent stable release."

### Installing Taipy in a Conda environment

Taipy can also be installed and used in a `Conda` environment, run this command in your terminal:
``` console
$ conda create -n env-name
$ conda activate env-name
$ pip install taipy
```

## From source

The source for Taipy can be downloaded from
the [Github repo][https://github.com/Avaiga/taipy].

You can either clone the public repository:

``` console
$ git clone git://github.com/avaiga/taipy
```

Or download the [tarball][https://github.com/Avaiga/taipy/tarball/main]:

``` console
$ curl -OJL https://github.com/avaiga/taipy/tarball/main
```

Once you have a copy of the source, you can install it with:

``` console
$ pip install .
```
