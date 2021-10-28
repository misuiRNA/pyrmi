import requests

from test.client.prox_class.animal_stub import AnimalStub


def _after_invoke(message):
    print(f"result: {message}")


def _sync_call():
    print("================ sync call ===================")
    animal = AnimalStub()
    res = animal.say_hello("cat, it is sync call")
    _after_invoke(res)
    print("================ sync done ===================")


def do_test_callback():
    url = "http://localhost:58081/async_call_test"
    resp = requests.post(url, json={"msg": "cat, it is sync call\nI am very happy\nhia hia hia hia"})
    print(resp)
    return resp


if __name__ == "__main__":
    _sync_call()
    # do_test_callback()
