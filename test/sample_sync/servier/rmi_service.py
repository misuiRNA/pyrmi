import json

from flask import Flask, request

from pyrmi.skeleton import register_real_class
from pyrmi.skeleton.rmi_executor import RmiExecutor
from test.sample_sync.servier.real_class.animal import Animal

app = Flask(__name__)


@app.route("/call", methods=["POST"])
def call():
    required = request.get_json()
    if not required:
        raise Exception("invalid required!")
    print(f"\033[33mrequired:\033[0m{required}")

    res = RmiExecutor(required).exec()
    return json.dumps({"result": res["rmi_result"]}, ensure_ascii=False)


if __name__ == "__main__":
    register_real_class(Animal)

    try:
        app.run(port=58080, host="0.0.0.0", debug=False)
    except Exception as e:
        print(e)
