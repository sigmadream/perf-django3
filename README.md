## getting start

```bash
$ copy config\django\example.env config\django\.env
$ copy config\postgres\example.env config\postgres\.env

$ docker-compose up --build
$ docker-compose run djangoapp python manage.py migrate
$ docker-compose run djangoapp python manage.py collectstatic --no-input -v 2

$ docker-compose run djangoapp /bin/sh -c "python manage.py flush; python manage.py migrate; python manage.py loaddata potter-fixture.json"
$ docker-compose run djangoapp python manage.py createsuperuser
```
