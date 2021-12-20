

class Serializable:

    def dump(self):
        raise NotImplemented()

    @classmethod
    def load(cls, json_data):
        raise NotImplemented()
