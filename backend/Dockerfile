FROM python:3.11-slim
WORKDIR /app
RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc python3-dev \
  && rm -rf /var/lib/apt/lists/*
RUN pip install poetry
COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
