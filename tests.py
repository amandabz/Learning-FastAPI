#
square_list = [n ** 2 for n in range(5)]

print(square_list)


# class Emp has been defined here
class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hello {self.name}, you are {self.age} years old.")


# Objects of class Emp has been made here
Emps = [Emp("John", 43),
        Emp("Hilbert", 16),
        Emp("Alice", 30)]

# Objects of class Emp has been used here
for emp in Emps:
    emp.info()


# list of numbers
my_list_of_numbers = [10, 20, 30, 40]


# modularization is done by functional approach
def sum_the_list(my_list_of_numbers):
    res = 0
    for value in my_list_of_numbers:
        res += value
    return res


print(sum_the_list(my_list_of_numbers))