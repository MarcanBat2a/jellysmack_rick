# syntax=docker/dockerfile:1
FROM python:3.7 as requirements-stage
WORKDIR /tmp
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN pip install poetry
COPY ./app/pyproject.toml ./app/poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.7
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
WORKDIR /app
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
