# countdown.py
# An example of defining a thread as a class

import time
import threading


class CountdownThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            print("Counting down", self.count)
            self.count -= 1
            time.sleep(0.5)
        raise RuntimeError("Done")
        # return self.count


# Sample execution
start_time = time.time()
t1 = CountdownThread(10)
t2 = CountdownThread(20)
t1.start()
t2.start()
# t1.join()
# t2.join()
end_time = time.time()
print(end_time - start_time)
print(50000000)
