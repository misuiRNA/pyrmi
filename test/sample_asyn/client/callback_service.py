from flask import Flask, request

from test.sample_sync.client.client import _after_invoke
from code.stub.async_handler import AsyncHandler
from test.sample_sync.client.prox_class.animal_stub import AnimalStub

app = Flask(__name__)


@app.route("/callback", methods=["POST"])
def callback():
    required = request.get_json()
    if not required:
        raise Exception("invalid required!")
    print(f"\033[33mrequired:\033[0m{required}")

    AsyncHandler.callback(required)
    return "success"


@app.route("/async_call_test", methods=["POST"])
def async_call_test():
    required = request.get_json()
    msg = required["msg"]
    print("================ sync call ===================")
    animal = AnimalStub()
    AsyncHandler.async_exec(animal.say_hello, [msg], _after_invoke)
    print("================ sync done ===================")
    return "done"


if __name__ == "__main__":
    try:
        app.run(port=58081, host="0.0.0.0", debug=False)
    except Exception as e:
        print(e)
