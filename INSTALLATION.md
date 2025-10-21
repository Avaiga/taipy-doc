# Installation

To see the changes you make to the documentation in a web browser, follow these steps.

### Prerequisites

- Python 3.9+ installed and on PATH
- Git
- An internet connection

### 1. Copy locally the source files from the Taipy repositories

In a terminal at the root of this repository, run:
```bash	
python tools/fetch_source_files.py develop
```

Note: this script requires network access.

### 2. Generate the documentation from the source files

The generation of the documentation requires that you use the Pipenv virtualenv management tool.

```bash
pip install pipenv
pipenv install --dev
pipenv run python tools/setup_generation.py
```

### 3. Launch the web server

```bash
pipenv run mkdocs serve
```

This will launch a web server (default http://127.0.0.1:8000) with the local documentation. The
server automatically reloads when you save files. Stop it with Ctrl+C.
