
class RmiInvoker:

    def __init__(self, communicate):
        self._communicate = communicate

    def invoke(self, obj, function, **kwargs):
        inst_json = obj.dump()
        inst_json.update({
            "class": obj.__class__.__name__.replace("Stub", ""),
        })
        req_data = {
            "instance": inst_json,
            "function": function.__name__,
            "args": kwargs
        }
        res = self._communicate(req_data)
        return res
