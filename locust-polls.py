from random import randint
from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    @task(1)
    def vote_random(self):
        response = self.client.get("/polls/1/", name="Open first poll form")
        csrftoken = response.cookies['csrftoken']
        self.client.post(
            "/polls/1/vote/",
            {"choice": str(randint(1, 4)), "csrfmiddlewaretoken": csrftoken},
            headers={"X-CSRFToken": csrftoken},
            cookies={"csrftoken": csrftoken},
        )


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 2000