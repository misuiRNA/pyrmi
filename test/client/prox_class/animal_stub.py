from code.common.serializable import Serializable
from code.stub.rmi_invoker import RmiInvoker
from test.client.http_invoke import http_invoke


class AnimalStub(Serializable):

    def __init__(self):
        self._name = "Proxy No.1"

    def say_hello(self, peer_name):
        res = RmiInvoker(http_invoke).invoke()
        return res

    def dump(self):
        json_data = {
            "name": self._name,
        }
        return json_data
