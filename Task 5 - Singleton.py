# Реализация через декоратор
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
            print(instances)
        return instances[cls]
    return getinstance


@singleton
class MyClass:
    pass


a = MyClass()
print(a)
b = MyClass()
print(b)


# Реализация с помощью мета класса
class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            print(cls.instances)
        return cls.instances[cls]


class MyClass(metaclass=Singleton):
    pass


a = MyClass()
print(a)
b = MyClass()
print(b)
