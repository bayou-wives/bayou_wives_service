FROM python:3.12

WORKDIR /bayou_wives_service
COPY . /bayou_wives_service/
# install poetry and dependencies
RUN pip install poetry
RUN poetry install
# TODO: figure out a way to run db migrations via docker
# RUN poetry run alembic upgrade head
# run app
CMD ["poetry", "run", "fastapi", "run", "app/main.py", "--port", "80"]
