from test.sample_sync.client.prox_class.animal_stub import AnimalStub


def _after_invoke(message):
    print(f"result: {message}")


def _sync_call():
    print("================ sync call ===================")
    animal = AnimalStub()
    res = animal.say_hello("cat, it is sync call")
    _after_invoke(res)
    print("================ sync done ===================")


if __name__ == "__main__":
    _sync_call()
