def square_calculations(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area
side = int(input("Введите длину стороны квадрата: "))
p, s = square_calculations(side)
print("Периметр:", p)
print("Площадь:", s)


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2
side = int(input("Введите длину стороны квадрата: "))
sq = Square(side)
print("Периметр:", sq.perimeter())
print("Площадь:", sq.area())

#Периметр и площадь окружности

import math

def circle_calculations(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return perimeter, area
r = float(input("Введите радиус окружности: "))

p, s = circle_calculations(r)
print("Длина окружности:", p)
print("Площадь круга:", s)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
s1 = Student("Aruzhan", 19)
s1.introduce()

class PrimeNumbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(self):
        return [num for num in self.numbers if self.is_prime(num)]

nums = input("Введите числа через пробел: ")
numbers = [int(x) for x in nums.split()]

prime_finder = PrimeNumbers(numbers)
prime_numbers = prime_finder.get_primes()

print("Простые числа из списка:", prime_numbers)


# Словарь переводов
dictionary = {
    "cat": "кот",
    "dog": "собака",
    "sun": "солнце",
    "moon": "луна"
}

word = input("Введите английское слово: ")

# Проверяем
match word.lower():
    case "cat" | "dog" | "sun" | "moon":
        print("Перевод:", dictionary[word.lower()])
    case _:
        print("Слова нет в словаре.")


words = input("Введите слова через пробел: ").split()
print("Список:", words)

def update_salary(salary):
    if salary > 2500:
        return salary
    else:
        return salary * 1.1

salary = float(input("Введите зарплату: "))
new_salary = update_salary(salary)

print("Новая зарплата:", new_salary)




def update_salaries(employees):
    updated = {}
    for name, salary in employees.items():
        if salary > 2500:
            updated[name] = salary
        else:
            updated[name] = salary * 1.1
    return updated


# словарь сотрудников
workers = {
    "Иван": 2000,
    "Мария": 2500,
    "Петр": 2800,
    "Анна": 1800
}

new_workers = update_salaries(workers)

print("Новые зарплаты:", new_workers)