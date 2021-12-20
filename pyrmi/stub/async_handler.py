from pyrmi.stub.rmi_stub import RmiStub


class AsyncHandler:

    _inst = None

    @classmethod
    def instance(cls):
        if not cls._inst:
            cls._inst = cls()
        return cls._inst

    def __init__(self):
        self._hook_map = {}

    def register(self, invoke_key: str, callback_method):
        self._hook_map.update({
            invoke_key: callback_method
        })

    def dispatch(self, invoke_key, rmi_result):
        callback_method = self._hook_map.pop(invoke_key)
        callback_method(rmi_result)

    @classmethod
    def async_exec(cls, func, param_list, hook_func):
        """
        :param func:
        :param param_list:
        :param hook_func: hook_func 的形参列表必须是一个json参数，hook_func函数自行根据需要解析具体参数
        :return:
        """
        stub = func.__self__
        if not isinstance(stub, RmiStub):
            raise Exception(f"object '{stub}' is not a RmiStub")

        import uuid
        invoke_id = str(uuid.uuid4())
        cls.instance().register(invoke_id, hook_func)
        stub.invoker.set_invoke_id(invoke_id)
        func(*param_list)

    @classmethod
    def callback(cls, hook_data):
        invoke_key = hook_data["invoke_id"]
        rmi_result = hook_data["rmi_result"]
        cls.instance().dispatch(invoke_key, rmi_result)
