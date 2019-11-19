# lock_ex.py
# A simple example of using a mutex lock for critical sections


import time
import threading

x = 0  # A shared value
x_lock = threading.Lock()  # A lock for synchronizing access to x

COUNT = 1000000


def foo():
    global x
    for i in range(COUNT):
        x_lock.acquire()
        x += 1
        x_lock.release()


def bar():
    global x
    for i in range(COUNT):
        x_lock.acquire()
        x -= 1
        x_lock.release()

t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)
time.clock()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(time.clock())
print(x)
