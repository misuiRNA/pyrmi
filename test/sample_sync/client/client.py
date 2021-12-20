from test.sample_sync.client.prox_class.animal_stub import AnimalStub


if __name__ == "__main__":
    print("================ sync call ===================")
    animal = AnimalStub()
    res = animal.say_hello("cat, it is sync call")
    print(f"result: {res}")
    print("================ sync done ===================")
