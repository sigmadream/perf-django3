## Setup

```bash
$ copy config\django\example.env config\django\.env
$ copy config\postgres\example.env config\postgres\.env

$ docker-compose up --build
$ docker-compose run djangoapp python manage.py migrate
$ docker-compose run djangoapp python manage.py collectstatic --no-input -v 2

$ docker-compose run djangoapp /bin/sh -c "python manage.py flush; python manage.py migrate; python manage.py loaddata potter-fixture.json"
$ docker-compose run djangoapp python manage.py createsuperuser
```

### Error Logs

```bash
docker-compose logs nginx
docker-compose logs djangoapp
```

## Cleanup

```bash
docker system prune -f
docker system prune -f --volumes
```
