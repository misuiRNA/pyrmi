import inspect

from code.common.serializable import Serializable


class RmiInvoker:

    def __init__(self, communicate):
        self._communicate = communicate

    def invoke(self):
        f_back = inspect.currentframe().f_back
        kwargs = f_back.f_locals
        caller = kwargs.pop("self")
        func_name = f_back.f_code.co_name

        if isinstance(caller, Serializable):
            inst_json = caller.dump()
        else:
            raise Exception(f"{caller} is not a Serializable")
        inst_json.update({
            "class": caller.__class__.__name__.replace("Stub", ""),
        })
        req_data = {
            "instance": inst_json,
            "function": func_name,
            "args": kwargs
        }

        res = self._communicate(req_data)
        return res
