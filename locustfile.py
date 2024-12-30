from locust import HttpUser, task, between, TaskSet


class UserBehavior(TaskSet):
    @task
    def get_h102_menu(self):
        self.client.get("/api/v1/menu/h102")

    @task
    def get_notice(self):
        self.client.get("/api/v1/notice")


class LocustUser(HttpUser):
    host = "http://127.0.0.1:8000"
    tasks = [UserBehavior]
    wait_time = between(1, 4)
