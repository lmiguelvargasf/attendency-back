# Attendency

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is an API to track people attending the meetings of my personal projects.

## Technologies

The main technologies used in this project are:

* [Docker][]
* [PostgreSQL][] (container)
* [Python 3][python] (container)
* [poetry][]
* [Django][]
* [Django REST Framework][DRF]

## Getting Started

### Prerequisites

The application has been containerized using Docker, so you have to [install][install-docker] the latest version of Docker before setting up this project.

### Set Up Project

#### Clone repository

Clone this repo and navigate inside its root directory:

```bash
git clone https://github.com/lmiguelvargasf/attendency-back && cd attendency-back
```

#### Start Services

Start the services defined in [docker-compose.yml][]:

```bash
docker-compose up
```

The previous command will pull and/or build the required images in case they are not found locally.

Open up your browser at [http://localhost:8000/api][api]. You are all set 🎉!

## Testing and Coverage


[`pytest`][pytest] is used for testing, and a test coverage of 100% is expected.

### Run Tests

Execute the following command in order to run the tests:

```bash
docker-compose exec app pytest
```

### Generate Coverage Report

Once you have run the tests, execute the following command in order to generate an html coverage report:

```bash
docker-compose exec app coverage html
```

The report is located at `./htmlcov/index.html` and it could be open in your browser.

## License

Copyright © 2020, [L Miguel Vargas F][M]. This project is licensed under the terms of the [MIT license][license].

[api]: http://localhost:8000/api
[Docker]: https://www.docker.com
[docker-compose.yml]: ./docker-compose.yml
[Django]: https://www.djangoproject.com
[DRF]: https://www.django-rest-framework.org
[install-docker]: https://www.docker.com/get-started
[license]: ./LICENSE
[M]: https://github.com/lmiguelvargasf
[poetry]: https://python-poetry.org
[PostgreSQL]: https://www.postgresql.org
[pytest]: https://docs.pytest.org/en/stable
[python]: https://www.python.org
