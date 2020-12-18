from threading import Thread, current_thread
import time


def thread_task():
    print("{0} executing".format(current_thread().getName()))
 

myThread = Thread(group=None,  # reserved
                target=thread_task(),
                name="childThread")

myThread.start()
print("here")
myThread.join()

