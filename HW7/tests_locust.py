from locust import HttpUser, TaskSet, task, between


# for https://www.rzd.ru/
class IOSUserBehavior(TaskSet):
    @task(1)
    def on_start(self):
        r = self.client.get("/")

    def on_stop(self):
        r = self.client.get("ru/9838")
        assert (r.status_code == 200)

    def on_next(self):
        r = self.client.get("/page/103290?id=18047")
        assert (r.status_code == 200)


# for https://www.rzd.ru/
class AndroidUserBehavior(TaskSet):

    def on_start(self):
        r = self.client.get("/")

    @task(3)
    def on_stop(self):
        r = self.client.get("ru/9284?rubricator_id=63")
        assert (r.status_code == 200)


# for https://apply.innopolis.ru/get-in
class InnoAuthor(TaskSet):

    @task
    def on_start(self):
        data = {
            "AUTH_FORM": "Y",
            "TYPE": "AUTH",
            "backurl": "/get-in/",
            "USER_LOGIN": "anlvovskay@mail.ru",
            "USER_PASSWORD": "Anastya040901",
            "Login": "Войти"
        }
        r = self.client.post("/?login=yes", data)
        assert (r.status_code == 200)


class WebsiteUser(HttpUser):
    tasks = [InnoAuthor]
    wait_time = between(1, 2)