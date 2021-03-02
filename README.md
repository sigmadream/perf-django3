# Django3 + Gunicorn 을 사용한 벤치마크

`Gunicorn` 성능을 확인하기 위해 벤치마크 입니다. Django에서 제공하는 [Polls](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)을 기반으로 진해하였습니다.

## getting start

### Django 프로젝트

```bash
$ copy config\django\example.env config\django\.env
$ copy config\postgres\example.env config\postgres\.env
$ docker-compose up --build
$ docker-compose run djangoapp python manage.py migrate
$ docker-compose run djangoapp python manage.py collectstatic --no-input -v 2
$ docker-compose run djangoapp /bin/sh -c "python manage.py flush; python manage.py migrate; python manage.py loaddata potter-fixture.json"
$ docker-compose run djangoapp python manage.py createsuperuser
```

### 테스트

```
$ python -m venv venv
$ .\venv\Scripts\activate
$ (venv) pip install -r requirements.txt
$ locust -f .\locust-polls.py
```

`http://localhost:8089`에 접속해서 테스트 진행
