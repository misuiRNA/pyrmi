import os
from types import MethodType, FunctionType


class StubCoder:

    def __init__(self, org_klass):
        self._org_klass: type = org_klass
        self._klass_name: str = f"{org_klass.__name__}Stub"
        self._indentation: int = 0

    def generate_code_file(self, path: str = "./"):
        code_txt = ""
        code_txt += self.code_dependency()
        code_txt += self.code_class()

        for attr_name, attr in self._org_klass.__dict__.items():
            # stub只代理自定义方法（函数），不关注内置方法和私有方法
            if isinstance(attr, MethodType) or isinstance(attr, FunctionType) and attr_name.find("_") > 0:
                method = attr
                method_args = list(method.__code__.co_varnames)
                code_line_list = ["res = self._invoker.invoke()", "return res"]
                code_txt += self.code_method(method.__name__, method_args, code_line_list)

        code_txt += self.code_method("dump", ["self"], ["# TODO 补充持久化代码", "pass"])
        self._indent_left()
        self._write_to_file(self._klass_name, path, code_txt)

    def code_dependency(self, dependency_list=None):
        code_txt = ""

        default_dependency_list = ["from pyrmi.common.serializable import Serializable",
                                   "from pyrmi.stub.rmi_stub import RmiStub"]
        dependency_list = default_dependency_list + (dependency_list or [])

        for dependency in dependency_list:
            code_txt += self._code_line(dependency)
        code_txt += "\n\n"
        return code_txt

    def code_class(self):
        code_txt = ""

        code_txt += self._code_line(f"class {self._klass_name}(RmiStub, Serializable):")
        self._indent_right()

        method = self._org_klass.__init__
        method_args = list(method.__code__.co_varnames)
        code_line_list = ["super().__init__(None)", "# TODO 补充初始化代码"]
        code_txt += self.code_method(method.__name__, method_args, code_line_list)
        return code_txt

    def code_method(self, method_name, arg_name_list, code_line_list=None):
        code_txt = ""

        arg_names_str = ", ".join(arg_name_list)
        code_txt += self._code_line(f"def {method_name}({arg_names_str}):")
        self._indent_right()
        if code_line_list:
            for line in code_line_list:
                code_txt += self._code_line(line)
        code_txt += "\n"
        self._indent_left()
        return code_txt

    def _code_line(self, txt_str: str):
        indent = " " * self._indentation
        code_txt = f"{indent}{txt_str}\n"
        return code_txt

    def _indent_right(self, step: int = 4):
        self._indentation += step

    def _indent_left(self, step: int = 4):
        self._indentation -= step

    @staticmethod
    def _write_to_file(file_name, path, code_txt):
        file_path = os.path.join(path, f"{file_name}.py")
        with open(file_path, "w") as f:
            f.write(code_txt)
            f.close()
