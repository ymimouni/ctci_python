from threading import Lock, Thread
from time import sleep
from random import randrange


class Chopstick:
    def __init__(self, n):
        self.number = n
        self.lock = Lock()

    def pick_up(self):
        return self.lock.acquire()

    def put_down(self):
        self.lock.release()

    def get_number(self):
        return self.number


class Philosopher(Thread):
    def __init__(self, i, left, right):
        Thread.__init__(self)
        self.index = i
        self.bites = 3
        self.max_pause = 100
        if left.get_number() < right.get_number():
            self.lower = left
            self.higher = right
        else:
            self.lower = right
            self.higher = left

    def run(self):
        for _ in range(self.bites):
            self.eat()

    def eat(self):
        print(f'Philosopher {self.index}: start eating')
        self.pick_up()
        self.chew()
        self.put_down()
        print(f'Philosopher {self.index}: done eating')

    def pick_up(self):
        self.pause()
        self.lower.pick_up()
        self.pause()
        self.higher.pick_up()
        self.pause()

    def pause(self):
        sleep(randrange(0, self.max_pause) / 100)

    def chew(self):
        print(f'Philosopher {self.index}: eating')
        self.pause()

    def put_down(self):
        self.higher.put_down()
        self.lower.put_down()


if __name__ == "__main__":
    size = 5

    chopsticks = [Chopstick(i) for i in range(size)]

    philosophers = [Philosopher(i, chopsticks[i], chopsticks[(i + 1) % size]) for i in range(size)]

    for philosopher in philosophers:
        philosopher.start()
