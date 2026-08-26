# docs/07/scripts/locustfile.py
from locust import HttpUser, task, between

class LojaUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def ver_produto(self):
        self.client.get("/produtos/1")

    @task(1)
    def comprar(self):
        self.client.post("/checkout", json={"item": 1, "qtd": 2})

