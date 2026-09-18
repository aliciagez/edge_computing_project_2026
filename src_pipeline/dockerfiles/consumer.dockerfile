FROM python:3.13-slim-bookworm

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
COPY pyproject.toml /app/
COPY README.md /app/
COPY src /app/src
RUN uv sync --no-dev
COPY consumer.py /app/
COPY utils /app/utils

ENV PYTHONUNBUFFERED=1

CMD ["uv", "run", "consumer.py"]