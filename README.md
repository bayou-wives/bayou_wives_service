# bayou_wives_service
Serves the bayou wives app

## Dependencies

This app requires Python, Poetry, Environment variables, and Docker.

### Python

This app requires Python 3.12 which can be downloaded [here](https://www.python.org/downloads/).

### Poetry

This app uses [Poetry](https://python-poetry.org/docs/) for virtual environment 
and dependency management.

**Note**: If you are using Windows, we'll create a virtual environment that uses Python 3.12
prior to using Poetry. To do this, run the following command in the root directory:

```bash
py -3.12 -m venv .venv
```

Activate this virtual environment by running:

```commandline
source .venv/Scripts/activate
```

Install poetry with the following command:

```commandline
pip install poetry
```

To activate a virtual environment, run the following command from the root directory:

```commandline
poetry shell
```

To **add** a python library to the dependencies, you must have the virtual environment activated.
After confirming the virtual environment is active, run the following command:

```bash
poetry add <python_library>
```

To **remove** a python library to the dependencies, you must have the virtual environment activated.
After confirming the virtual environment is active, run the following command:

```bash
poetry remove <python_library>
```

### Environment

Add a `.env` file to the root directory. 
Add the following environment variables to the `.env` file:

```txt
ENV=local
# DB
POSTGRES_SERVER=host.docker.internal
POSTGRES_PORT=5432
POSTGRES_USER=db_user
POSTGRES_PASSWORD=<your_db_password>
POSTGRES_DB=db
# password hashing
HASHING_SECRET_KEY=<your_secret_key>
HASHING_ALGORITHM=HS256
```

Note: you can generate a `HASHING_SECRET_KEY` by running the following command in your terminal:

```commandline
opensll rand -hex 32
```

### Docker

This app uses Docker containers for local development. Therefore, you will need to download 
[Docker Desktop](https://www.docker.com/products/docker-desktop/) or a similar tool.

### Database Migrations

This app uses [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) 
for database migrations. See the [tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) 
for basic functionality and usage.

#### Generating Running Database Migrations Locally

**Note**: Prior to generating or running a database migration, you must have the database container running 
which allows us to connect to the database. You also will likely need to update your `POSTGRES_SERVER`
environment variable to `localhost`.

To generate a database migration after making changes to the `app.db.models`, 
run the following command from the root directory:

```commandline
alembic revision --autogenerate -m "description of your changes"
```

To run your database migrations, run the following command from the root directory:

```commandline
alembic upgrade head
```

## Running the app

Build and start the app by running the following command from the root directory:

```commandline
docker compose up --build d
```

Stop and remove the containers by running the following command from the root directory:

```commandline
docker compose down
```
