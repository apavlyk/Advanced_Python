import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()  # remove lock for example
        balance.value = balance.value + 10
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value - 20
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))
    w.daemon = True
    d.daemon = True
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
