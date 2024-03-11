from threading import Thread, Lock
from time import sleep


# Unlike Java, a thread can release a Lock owned by another thread.
class Foo:
    def __init__(self):
        self.pause_time = 1
        self.lock_1 = Lock()
        self.lock_2 = Lock()
        self.lock_1.acquire()
        self.lock_2.acquire()

    def first(self):
        print('Started Executing 1')
        sleep(self.pause_time)
        print('Finished Executing 1')
        self.lock_1.release()

    def second(self):
        self.lock_1.acquire()
        self.lock_1.release()
        print('Started Executing 2')
        sleep(self.pause_time)
        print('Finished Executing 2')
        self.lock_2.release()

    def third(self):
        self.lock_2.acquire()
        self.lock_2.release()
        print('Started Executing 3')
        sleep(self.pause_time)
        print('Finished Executing 3')





class MyThread(Thread):
    def __init__(self, foo, method):  # noqa
        Thread.__init__(self)
        self.method = method
        self.foo = foo

    def run(self):
        if self.method == 'first':
            self.foo.first()
        elif self.method == 'second':
            self.foo.second()
        elif self.method == 'third':
            self.foo.third()


if __name__ == "__main__":
    foo = Foo2()
    thread_1 = MyThread(foo, 'first')
    thread_2 = MyThread(foo, 'second')
    thread_3 = MyThread(foo, 'third')

    thread_1.start()
    thread_2.start()
    thread_3.start()
