class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(type(s1))
print(s1)
print(id(s1))

print("")

print(type(s2))
print(s2)
print(id(s2))