"""
Animal shelter.
"""

from collections import deque


class Animal(object):
    def __init__(self, name: str) -> None:
        self.order = None
        self.name = name

    def is_older_than(self, a) -> bool:
        return self.order < a.order


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class AnimalQueue:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueue(self, a: Animal):
        a.order = self.order
        self.order += 1
        if isinstance(a, Cat):
            self.cats.append(a)
        elif isinstance(a, Dog):
            self.dogs.append(a)

    def dequeue_any(self):
        if not self.cats:
            return self.dogs[-1]
        elif not self.dogs:
            return self.cats[-1]
        cat = self.cats[-1]
        dog = self.dogs[-1]
        if dog.is_older_than(cat):
            return self.dogs.pop()
        else:
            return self.cats.pop()

    def dequeue_dogs(self):
        return self.dogs.pop()

    def dequeue_cats(self):
        return self.cats.pop()

    def peek_dogs(self):
        return self.dogs[-1]

    def peek_cats(self):
        return self.cats[-1]


if __name__ == "__main__":
    animals = AnimalQueue()
    animals.enqueue(Cat("Callie"))
    animals.enqueue(Cat("Kiki"))
    animals.enqueue(Dog("Fido"))
    animals.enqueue(Dog("Dora"))
    animals.enqueue(Cat("Cari"))
    animals.enqueue(Dog("Dexter"))

    print(animals.dequeue_any().name)
    print(animals.dequeue_dogs().name)
    print(animals.dequeue_cats().name)
