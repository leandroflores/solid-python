class SingletonMeta(type):
    _instances: dict = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):

    def __init__(self):
        ...

s1 = Singleton()
s2 = Singleton()

print(type(s1))
print(s1)
print(id(s1))

print("")

print(type(s2))
print(s2)
print(id(s2))