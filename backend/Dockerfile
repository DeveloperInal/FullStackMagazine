FROM python:3.10.12-slim as build

ENV POETRY_VERSION=1.8.3

RUN pip install poetry==${POETRY_VERSION}

WORKDIR /app/

COPY . .

RUN poetry install

EXPOSE 8000

CMD [ "poetry", "run", "python", "main.py" ]
