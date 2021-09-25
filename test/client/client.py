from test.client.prox_class.animal_stub import AnimalStub

animal = AnimalStub()
res = animal.say_hello("cat")


print(f"result: {res}")
