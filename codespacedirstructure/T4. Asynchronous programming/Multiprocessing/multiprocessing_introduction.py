import time
import os, signal
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))

def calc_cube(numbers):
    time.sleep(10)
    for n in numbers:
        print('cube ' + str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    # p1.join()
    p2.join()

    print(p1.pid)
    # signal.signal(signal.CTRL_C_EVENT, calc_cube)
    # p1.terminate()
    # os.kill(p2.pid, signal.CTRL_C_EVENT)
    time.sleep(5)
    print(p1.exitcode)

    print(p1.pid)
    print(p2.pid)
    print("Done!")