#!/usr/bin/python

import threading
import time
import queue
import sys

items = queue.Queue()


def enter_data():
    val = input("Insert something: ")
    items.put(val)
    # while True:
    #     val = input("Insert something: ")
    #     items.put(val)
    #     time.sleep(2)


def script_exit():
    print("I'm a consumer", threading.currentThread().name)
    while True:
        if items and items.get() == 'exit':
            sys.exit(0)
        time.sleep(1)


def start():
    print("I'm a consumer", threading.currentThread().name)
    while True:
        if items:
            print(threading.currentThread().name, "got", items.get())
        time.sleep(1)


if __name__ == '__main__':
    exit_thread = threading.Thread(target=exit)
    start_thread = threading.Thread(target=start)

    exit_thread.start()
    start_thread.start()
    while True:
        enter_data()

