#Locust Script to do test HPA

from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(2) 
    def get_root(self):
        self.client.get("/")

    @task(1)
    def get_data(self):
        self.client.get("/data")

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:64210" 
    tasks = [UserBehavior]
    wait_time = between(1, 5)
