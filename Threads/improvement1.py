from threading import Thread, Condition
import time

def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_prog:
        cond_var.acquire()
        while not found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()

        if not exit_prog:
            print(prime_holder)

            prime_holder = None
            cond_var.acquire()
            found_prime = False
            cond_var.notify()
            cond_var.release()

def finder_thread_func():
    global prime_holder
    global found_prime

    i = 2
    
    while not exit_prog:

        while not is_prime(i):
            i += 1
        
        prime_holder = i
        cond_var.acquire()
        found_prime = True
        cond_var.notify()
        cond_var.acquire()

        cond_var.acquire()
        while found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()
        
        i += 1



def is_prime(num):
    if num == 2 or num == 3:
        return True
 
    div = 2
 
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
 
    return True


cond_var = Condition()
found_prime = False
prime_holder = None
exit_prog = False
 
printer_thread = Thread(target=printer_thread_func)
printer_thread.start()
 
finder_thread = Thread(target=finder_thread_func)
finder_thread.start()
 
# Let the threads run for 5 seconds
time.sleep(3)
 
# Let the threads exit
exit_prog = True
cond_var.acquire()
cond_var.notifyAll()
cond_var.release()
 
printer_thread.join()
finder_thread.join()