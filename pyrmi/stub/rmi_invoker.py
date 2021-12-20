import inspect
from pyrmi.common.serializable import Serializable


class RmiInvoker:

    def __init__(self, communicate):
        self._communicate = communicate
        self._req_id = "Rmi-DefaultInvokeId"

    def set_invoke_id(self, invoke_id):
        self._req_id = str(invoke_id)

    def invoke(self):
        f_back = inspect.currentframe().f_back
        kwargs = f_back.f_locals
        caller = kwargs.pop("self")
        func_name = f_back.f_code.co_name

        if isinstance(caller, Serializable):
            inst_json = caller.dump()
        else:
            raise Exception(f"{caller} is not a Serializable")
        klass_name = caller.__class__.__name__.replace("Stub", "")
        req_data = {
            "class": klass_name,
            "function": func_name,
            "instance": inst_json,
            "args": kwargs,
            "invoke_id": self._req_id
        }

        res = self._communicate(req_data)
        return res
