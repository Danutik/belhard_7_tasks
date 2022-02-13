"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""

import random


class RandSequence:

    def __init__(self, n):
        self.n = n
        self.sequence = [random.randint(-self.n, self.n) for i in range(self.n)]

    def generate(self, n=0):
        self.sequence = (random.randint(-n, n) for i in range(n))
        return self.sequence

    def print_seq(self):
        print(self.sequence)

    def __repr__(self):
        return f"RandSequence {self.sequence}"
