from code.common.serializable import Serializable


class Animal(Serializable):

    def __init__(self, name):
        self._name = name

    def say_hello(self, peer_name):
        res = f"hello \033[34m{peer_name}\033[0m, I am \033[34m{self._name}\033[0m ..."
        return res

    def async_say_hello(self, peer_name):
        res = f"hello \033[34m{peer_name}\033[0m, I am \033[34m{self._name}\033[0m ..."
        return res

    def dump(self):
        json_data = {
            "name": self._name,
        }
        return json_data

    @classmethod
    def load(cls, json_data):
        name = json_data["name"]
        return cls(name)
