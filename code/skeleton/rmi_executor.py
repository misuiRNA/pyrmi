from code import skeleton as klass_container
from code.common.serializable import Serializable


class RmiExecutor:

    def __init__(self, required):
        self._required = required

    def exec(self):
        obj = self._parse_object()
        func = self._parse_function(obj)
        kwargs = self._parse_args()
        res = func(**kwargs)
        return res

    def _parse_object(self):
        inst_json = self._required["instance"]
        klass_name = inst_json["class"]
        klass = getattr(klass_container, klass_name)

        if issubclass(klass, Serializable):
            inst = klass.load(inst_json)
        else:
            raise Exception(f"{klass} is not a Serializable class")

        return inst

    def _parse_function(self, obj: object):
        func = getattr(obj, self._required["function"])
        return func

    def _parse_args(self):
        kwargs = self._required["args"]
        return kwargs
