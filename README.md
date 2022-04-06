# Taipy Doc

## license
Copyright 2022 Avaiga Private Limited

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at
[http://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

## Usage
- [License](#license)
- [Usage](#usage)
- [Taipy Doc](#what-is-taipy-doc)
- [Installation](#installation)
- [Contributing](#contributing)
- [Code of conduct](#code-of-conduct)
- [Directory Structure](#directory-structure)

## What is Taipy Doc

Taipy is a Python library for creating Business Applications. More information on our
[website](https://www.taipy.io). Taipy is split into multiple repositories to let users
install the minimum they need.

[Taipy Doc](https://github.com/Avaiga/taipy-doc) has the responsibility to hold and build the full Taipy
documentation set. The `taipy-doc` repository uses [MkDocs](https://www.mkdocs.org/) to generate its entire
content.

## Installation

Want to install _Taipy Doc_? Check out our [`INSTALLATION.md`](INSTALLATION.md) file.

## Contributing

Want to help build _Taipy Doc_? Check out our [`CONTRIBUTING.md`](CONTRIBUTING.md) file.

## Code of conduct

Want to be part of the _Taipy Doc_ community? Check out our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) file.

## Directory Structure

- `taipy/core`:
    - `taipy/core`:
        - `_repository`: Internal layer for data storage.
        - `_scheduler`: Internal layer for task scheduling and execution.
        - `common`: Shared data structures, types, and functions.
        - `config`: Configuration definition, management and implementation. `config.config.Config` is the main
          entrypoint for configuring a Taipy Core application.
        - `cycle`: Work cycle definition, management and implementation.
        - `data`: Data Node definition, management and implementation.
        - `exceptions`: _taipy-core_ exceptions.
        - `job`: Job definition, management and implementation.
        - `pipeline`: Pipeline definition, management and implementation.
        - `scenario`: Scenario definition, management and implementation.
        - `task`: Task definition, management and implementation.
        - `taipy`: Main entrypoint for _taipy-core_ runtime features.
    - `tests`: Unit tests following the `taipy/core` structure.
- `CODE_OF_CONDUCT.md`: Code of conduct for members and contributors of _taipy-core_.
- `CONTRIBUTING.md`: Instructions to contribute to _taipy-core_.
- `INSTALLATION.md`: Instructions to install _taipy-core_.
- `LICENSE`: The Apache 2.0 License.
- `Pipfile`: File used by the Pipenv virtual environment to manage project dependencies.
- `README.md`: Current file.
- `setup.py`: The setup script managing building, distributing, and installing _taipy-core_.
- `tox.ini`: Contains test scenarios to be run.

