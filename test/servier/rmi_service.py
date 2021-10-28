import json

from flask import Flask, request

from code.skeleton import register_real_class
from code.skeleton.rmi_executor import RmiExecutor
from test.servier.real_class.animal import Animal

app = Flask(__name__)


@app.route("/call", methods=["POST"])
def call():
    required = request.get_json()
    if not required:
        raise Exception("invalid required!")
    print(f"\033[33mrequired:\033[0m{required}")

    res = RmiExecutor(required).exec()
    return json.dumps({"result": res["rmi_result"]}, ensure_ascii=False)


def register_rmi_klass(klass):
    register_real_class(klass)


if __name__ == "__main__":
    register_rmi_klass(Animal)

    try:
        app.run(port=58080, host="0.0.0.0", debug=False)
    except Exception as e:
        print(e)
