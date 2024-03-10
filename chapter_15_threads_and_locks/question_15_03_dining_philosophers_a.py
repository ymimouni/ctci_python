from threading import Lock, Thread
from time import sleep
from random import randrange


class Chopstick:
    def __init__(self):
        self.lock = Lock()

    def pick_up(self):
        return self.lock.acquire()

    def put_down(self):
        self.lock.release()


class Philosopher(Thread):
    def __init__(self, i, left, right):
        Thread.__init__(self)
        self.index = i
        self.left = left
        self.right = right
        self.bites = 3
        self.max_pause = 100

    def run(self):
        for _ in range(self.bites):
            self.eat()

    def eat(self):
        print(f'Philosopher {self.index}: start eating')
        if self.pick_up():
            self.chew()
            self.put_down()
            print(f'Philosopher {self.index}: done eating')
        else:
            print(f'Philosopher {self.index}: gave up on eating')

    def pick_up(self):
        self.pause()
        if not self.left.pick_up():
            return False
        self.pause()
        if not self.right.pick_up():
            self.left.put_down()
            return False
        self.pause()
        return True

    def pause(self):
        sleep(randrange(0, self.max_pause) / 100)

    def chew(self):
        print(f'Philosopher {self.index}: eating')
        self.pause()

    def put_down(self):
        self.right.put_down()
        self.left.put_down()


if __name__ == "__main__":
    size = 5

    chopsticks = [Chopstick() for _ in range(size)]

    philosophers = [Philosopher(i, chopsticks[i], chopsticks[(i + 1) % size]) for i in range(size)]

    for philosopher in philosophers:
        philosopher.start()
