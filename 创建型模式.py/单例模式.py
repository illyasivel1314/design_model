class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, a):
        self.a = a

ms1 = MyClass(1)
ms2 = MyClass(2)
print(ms1.a, ms2.a)
print(id(ms1), id(ms2))