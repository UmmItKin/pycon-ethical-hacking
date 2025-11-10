FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app
COPY . /app

RUN uv sync --frozen

RUN chmod +x entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["bash", "entrypoint.sh"]
CMD ["uv", "run", "python", "app.py"]
