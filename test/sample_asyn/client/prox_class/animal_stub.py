from code.common.serializable import Serializable
from code.stub.rmi_invoker import RmiInvoker
from code.stub.rmi_stub import RmiStub
from test.sample_sync.client.prox_class.http_invoke import http_invoke


class AnimalStub(RmiStub, Serializable):

    def __init__(self):
        super().__init__(RmiInvoker(http_invoke))
        self._name = "Proxy No.1"

    def say_hello(self, peer_name):
        res = self._invoker.invoke()
        return res

    def dump(self):
        json_data = {
            "name": self._name,
        }
        return json_data

    def set_invoker(self, invoker):
        self._invoker = invoker
