class SingletonMeta(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):

    def some_operation(self) -> None:
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