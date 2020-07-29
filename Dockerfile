FROM python:slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install and setup poetry
RUN pip install -U pip \
    && apt-get update \
    && apt install -y curl netcat \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"

# Install dependencies
WORKDIR /usr/src/app
# The following RUN commands have been taken and modified from:
# https://github.com/python-poetry/poetry/issues/1301#issuecomment-609009714
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
  && poetry export --without-hashes -f requirements.txt --dev \
  |  poetry run pip install -r /dev/stdin
COPY . .
RUN poetry install --no-interaction --no-ansi

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
