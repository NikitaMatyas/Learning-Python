def my_decorator(func_to_decorate):
    def wrapper(self, age):
        age -= 5
        print("Already did something before the function")
        return func_to_decorate(self, age)
    return wrapper


class Person:
    def __init__(self):
        self.age = None

    @my_decorator
    def just_function(self, age):
        print("My age is", age)


a = Person()
a.just_function(30)
