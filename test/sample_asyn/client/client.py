import requests


if __name__ == "__main__":
    url = "http://localhost:58081/async_call_test"
    resp = requests.post(url, json={"msg": "cat, it is sync call\nI am very happy\nhia hia hia hia"})
    print(resp)
