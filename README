## Build

	$ docker build -t cryptoclass .

## Run

	$ docker run --net=host cryptoclass

Using net=host allows you to see the output in http://localhost:8000.

You can set environment variables for the database:

	$ docker run --net=host -e DB_USER=... DB_PASS=... DB_HOST=... DB_PORT=... cryptoclass

To be able to make changes instantly be changed inside the container, bind
mount your development directory inside /usr/src/app of the container by
passing parameter -v <dev_directory>:/usr/src/app

## Migrations

Migrations run automatically when the container starts. To run them again
manually, run

	$ docker exec <container_name> python manage.py migrate
