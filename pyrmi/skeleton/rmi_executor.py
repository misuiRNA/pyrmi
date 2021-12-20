from pyrmi import skeleton as klass_container
from pyrmi.common.serializable import Serializable


class RmiExecutor:

    def __init__(self, required):
        self._required = required

    def exec(self):
        obj = self._parse_object()
        func = self._parse_function(obj)
        kwargs = self._parse_args()
        res = func(**kwargs)

        res_json = {
            "invoke_id": self._required["invoke_id"],
            "rmi_result": res
        }
        return res_json

    def _parse_object(self):
        klass = self._parse_class()

        if issubclass(klass, Serializable):
            inst_json = self._required["instance"]
            inst = klass.load(inst_json)
        else:
            raise Exception(f"{klass} is not a Serializable class")

        return inst

    def _parse_class(self):
        klass_name = self._required["class"]
        klass = getattr(klass_container, klass_name)
        return klass

    def _parse_function(self, obj: object):
        func = getattr(obj, self._required["function"])
        return func

    def _parse_args(self):
        kwargs = self._required["args"]
        return kwargs
