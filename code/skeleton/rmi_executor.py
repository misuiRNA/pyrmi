from code import skeleton as klass_container


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
        inst_args = inst_json["name"]
        klass = getattr(klass_container, klass_name)
        obj = klass(inst_args)
        return obj

    def _parse_function(self, obj: object):
        func = getattr(obj, self._required["function"])
        return func

    def _parse_args(self):
        kwargs = self._required["args"]
        return kwargs
