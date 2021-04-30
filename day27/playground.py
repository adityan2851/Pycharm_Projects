def add(*args):
    summ = 0
    for n in args:
        summ += n
    return summ


print(add(4, 3, 4, 6, 7, 8))


def calculator(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculator(5, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
