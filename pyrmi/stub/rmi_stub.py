from pyrmi.stub.rmi_invoker import RmiInvoker


class RmiStub:

    def __init__(self, invoker):
        self._invoker: RmiInvoker = invoker

    @property
    def invoker(self):
        return self._invoker
