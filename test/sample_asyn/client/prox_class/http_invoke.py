import json
import requests


def http_invoke(req_data):
    url = "http://localhost:58080/call"

    resp = requests.post(url, json=req_data)
    if resp.status_code == 200:
        res = json.loads(resp.content)
    else:
        print(f"\033[30m request by http failed! [code={resp.status_code}]")
        res = {"result", None}
    res = res["result"]
    return res
