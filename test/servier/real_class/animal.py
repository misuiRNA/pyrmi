class Animal:

    def __init__(self, name):
        self._name = name

    def say_hello(self, peer_name):
        res = f"hello \033[34m{peer_name}\033[0m, I am \033[34m{self._name}\033[0m ..."
        return res
