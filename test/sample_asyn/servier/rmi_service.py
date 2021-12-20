import json
import time
from threading import Thread

import requests
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

    scheduler = Thread(target=_delay_exec_and_callback, args=[required])
    scheduler.start()
    print("done...")
    return json.dumps({"result": "done"}, ensure_ascii=False)


def _delay_exec_and_callback(required):
    time.sleep(1)
    print("start callback...")
    res = RmiExecutor(required).exec()
    _http_callback(res)
    print("callback done...")


def _http_callback(req_data):
    url = "http://localhost:58081/callback"

    resp = requests.post(url, json=req_data)
    if resp.status_code == 200:
        res = str(resp.content)
    else:
        print(f"\033[30m callback by http failed! [code={resp.status_code}]")
        res = {"result", None}
    return res


if __name__ == "__main__":
    register_real_class(Animal)

    try:
        app.run(port=58080, host="0.0.0.0", debug=False)
    except Exception as e:
        print(e)
