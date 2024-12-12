class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() method.")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance

s1 = ClassicSingleton.get_instance()
s2 = ClassicSingleton.get_instance()

print(type(s1))
print(s1)
print(id(s1))

print("")

print(type(s2))
print(s2)
print(id(s2))