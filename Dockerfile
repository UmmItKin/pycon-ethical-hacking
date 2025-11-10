FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app
COPY . /app

RUN uv sync --frozen

EXPOSE 8080

CMD ["uv", "run", "python", "app.py"]
