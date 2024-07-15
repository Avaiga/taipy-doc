---
title: Install Taipy
---

Welcome to the installation section of the Taipy web application builder! This section will
guide you through the seamless and straightforward process of setting up and deploying your own
powerful web applications.

# Prerequisite

Before installing Taipy, ensure you have Python (**version 3.8 or later**) and
[pip](https://pip.pypa.io) installed on your system. If you don't have pip installed, you can
follow these steps to install it:

1. **[Python Installation Guide](http://docs.python-guide.org/en/latest/starting/installation/)**:
    Follow the installation guide to set up Python on your system.
    After the installation, you can open the Command Prompt and type `python --version` to check
    the installed Python version.

2. **[Installing pip](https://pip.pypa.io/en/latest/installation/)**: Pip is included by default
    if you use Python 3.4 or later. Otherwise, you can follow the official
    installation page of pip to install it. To verify the installation, type `pip --version` or
    `pip3 --version`.

Alternatively, if you are using a Conda environment, you can install pip using the following
command:

```console
$ conda install pip
```

To install Taipy, you have several options depending on your needs and preferences.

# Installing Taipy - Stable release

The preferred method to install Taipy is by using **pip**. Open your terminal or command prompt
and run the following command:

```console
$ pip install taipy
```

This command will download and install the most recent stable release of Taipy.


# Installing Taipy with Colab

Google Colab is a popular and free Jupyter notebook environment that requires no setup
and runs entirely in the cloud. To install Taipy in Google Colab, follow these simple
steps:

1. **Open a new Colab notebook**: Visit [Google Colab](https://colab.research.google.com)
and start a new notebook.

2. **Run the installation command**: In a new cell, enter the following command and run
the cell:

    ```python
    !pip install --ignore-installed taipy
    ```

    This command installs the latest stable release of Taipy in your Colab environment.

3. **Start building your app**: Follow this
[tip](../tutorials/integration/2_colab_with_ngrok/index.md) to build and run your Taipy web
application directly within the Colab notebook.

!!! tip
    Remember that Google Colab environments are ephemeral. If you disconnect or restart
    your Colab session, you will need to reinstall Taipy.

# Installing Taipy in a Conda Environment

Conda is an open-source package management system and environment management system that runs on
Windows, macOS, and Linux.

If you prefer to work within a [Conda](https://docs.conda.io/projects/conda/en/latest/index.html)
environment, follow these steps:

1. Create a new **Conda** environment (replace **env-name** with your desired environment name):
    ```console
    $ conda create -n env-name
    ```
2. Activate the newly created environment:
    ``` console
    $ conda activate env-name
    ```
3. Install Taipy within the Conda environment using pip:
    ```console
    $ pip install taipy
    ```

# Installing Taipy from Source

If you want to work with the latest development version or contribute to the project, you can
install Taipy from the source code.

- Clone the public repository from GitHub (you'll need Git installed for this method):
    ```console
    $ git clone git://github.com/avaiga/taipy
    ```

Or,

- Download the tarball directly from GitHub:
    ```console
    $ curl -OJL https://github.com/avaiga/taipy/tarball/main
    ```

Once you have the source code, navigate to the directory containing the Taipy source code and
run the following command:

```console
$ pip install .
```

This will install Taipy from the source code on your system.

!!! info
    The commands mentioned above are for Unix-like systems (Linux, macOS), and you may
    need to adjust them slightly if you are using a different operating system such as Windows.
