from code.stub.rmi_invoker import RmiInvoker
from test.client.http_invoke import http_invoke


class AnimalStub:

    def __init__(self):
        self._name = "Proxy No.1"

    def say_hello(self, peer_name):
        res = RmiInvoker(http_invoke).invoke(self, self.say_hello, peer_name=peer_name)
        return res

    def dump(self):
        json_data = {
            "name": self._name,
        }
        return json_data
