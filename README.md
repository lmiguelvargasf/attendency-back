# Attendancy

This is an API to track people attending the meetings of my personal projects.

## Getting Started

### Prerequisites

You need to install the latest version of following software before setting up this project:

* [python][]
* [pyenv][]
* [pyenv-virtualenv][]
* [poetry][]
* [sqlite][]

### Setting Up Project

#### Clone repository

Clone this repository:

```bash
git clone https://github.com/lmiguelvargasf/attendency
```

Navigate inside the project's root directory:

```bash
cd attendency
```

#### Install python

`pyenv` is used to install the specific version of `python` required in this project:

```bash
pyenv install 3.8.2
```

#### Create and activate a virtual environment

`pyenv`'s plugin `pyenv-virtualenv` is used to create a virtual environment:

```bash
pyenv virtualenv 3.8.2 attendancy-venv
```

Now activate the previously created virtual environment:

```bash
pyenv activate attendancy-venv
```

### Install dependencies

`poetry` is used to install and manage dependencies. To install the dependencies for this project run:

```bash
poetry install
```

### Applying migrations

Run the following command in order to apply the migrations:

```bash
python manage.py migrate
```

### Run server

In order to start a lightweight development web server on the local machine, run this command:

```bash
python manage.py runserver
```

Open up your browser at [http://localhost:8080][localhost]. You are all set 🎉!

## Running tests

Execute the following command in order to run the tests:

```bash
pytest
```


[localhost]: http://localhost:8080
[poetry]: https://python-poetry.org/
[pyenv]: https://github.com/pyenv/pyenv
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[python]: https://www.python.org//
[sqlite]: https://www.sqlite.org/index.html
