FROM python:3.9.2-slim-buster AS base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    VENV_PATH=/opt/venv \
    PIP_VERSION=21.0.1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    DEV_REQUIREMENTS_PATH=$HOME/requirements.txt

WORKDIR /project

FROM base AS builder

ENV POETRY_VERSION=1.1.5 \
    POETRY_PATH=/opt/poetry
ENV PATH="$POETRY_PATH/bin:$PATH"

# Prepare system for dependency installation
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    pip install --upgrade pip==$PIP_VERSION && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && \
    mv /root/.poetry $POETRY_PATH && \
    python -m venv $VENV_PATH

# Install packages needed for dependencies in isolated layer
RUN apt-get install -y --no-install-recommends \
    build-essential

# Install dependencies. Create dev requirements.txt to install dev dependencies as needed
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt | pip install -r /dev/stdin && \
    poetry export --dev --without-hashes -f requirements.txt -o $DEV_REQUIREMENTS_PATH

FROM base AS development

COPY --from=builder $VENV_PATH $VENV_PATH
COPY --from=builder $DEV_REQUIREMENTS_PATH $DEV_REQUIREMENTS_PATH

RUN pip install -r $DEV_REQUIREMENTS_PATH

COPY . .

CMD ["tail", "-f", "/dev/null"]

FROM base AS test

COPY --from=builder $VENV_PATH $VENV_PATH
COPY --from=builder $DEV_REQUIREMENTS_PATH $DEV_REQUIREMENTS_PATH

RUN pip install -r $DEV_REQUIREMENTS_PATH

COPY . .

CMD ["pytest", "tests"]

FROM base AS production

COPY --from=builder $VENV_PATH $VENV_PATH

COPY . .

CMD ["tail", "-f", "/dev/null"]
