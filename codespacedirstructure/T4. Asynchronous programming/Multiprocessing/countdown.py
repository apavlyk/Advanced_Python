# countdown.py
#
# Example of launching a process with the multiprocessing module

import time
import multiprocessing
import threading


class CountdownProcess(multiprocessing.Process):
    def __init__(self, count):
        multiprocessing.Process.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            print("Counting down", self.count, threading.current_thread().name)
            time.sleep(2)
            self.count -= 1
        return


if __name__ == '__main__':
    p1 = CountdownProcess(10)  # Create the process object
    p1.start()  # Launch the process
    print(p1.is_alive())

    p2 = CountdownProcess(20)  # Create another process
    p2.start()  # Launch

    # [CountdownProcess(i).start() for i in range(100000)]


for i in range(101):
    sys.stdout.write("Read ")
    sys.stdout.flush()
    time.sleep(0.5)
