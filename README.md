# mironov_blog_pwa

Reworked version of personal blog powered by FastAPI and Angular PWA.

# Running backend app

Before running the backend app, you should create a `.env` and put it in the root of project. This file sould include `DATABASE_URL`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`. `DATABASE_URL` Should be in the following format: `postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}`.

`make init` - initialize docker containers.

`make generate_migrations message={your custom message}` - generate migration.

`make migrate` - apply migrations.

`make run` - run application.
