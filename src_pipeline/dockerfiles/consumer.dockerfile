FROM python:3.13-slim-bookworm

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev
COPY consumer.py /app/
COPY utils /app/utils

ENV PYTHONUNBUFFERD=1

CMD ["uv", "run", "consumer.py"]