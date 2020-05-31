from threading import Thread
from threading import current_thread


class MyTask(Thread):

    def __init__(self, name="Akash New", args=(3, 5)):
        # The two args will not get passed to the overridden
        # run method.
        Thread.__init__(self, name=name, args=args)

    def run(self):
        print(self._name)
        print(self._args)
        print("{0} is executing".format(current_thread().getName()))


myTask = MyTask(name="Aksh", args=(3,5))

myTask.start()  # start the thread

myTask.join()  # wait for the thread to complete

print("{0} exiting".format(current_thread().getName()))
