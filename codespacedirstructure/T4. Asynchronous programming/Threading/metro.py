import datetime
import time
import itertools
import random
import threading

lock = threading.Semaphore(1)
stations_opening = datetime.time(5, 45, 0)
stations_closing = datetime.time(23, 50, 0)

hour_min_now = lambda: (time.localtime().tm_hour,
                        time.localtime().tm_min,
                        time.localtime().tm_sec)

print("We are started at {}:{}:{}".format(*hour_min_now()))

intersections = (("Золоті ворота", "Театральна"),("Майдан Незалежності",
                 "Хрещатик"), ("Площа Льва Толстого", "Палац спорту"))

def generate_stations(station_file):
    with open(station_file, encoding='utf8') as line:
        stations = [station.strip() for station in line.readlines()]
    one_station_cycle = itertools.chain(stations, stations[::-1])
    for station in itertools.cycle(one_station_cycle):
        yield station

class RedLine(threading.Thread):

    intersection = False

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for station in generate_stations('red_stations.txt'):
            print("We are on {} station at {}:{}:{}".format(station, *hour_min_now()))
            time.sleep(random.randint(0, 1)*0.2)
            if station in intersections[0] and GreenLine.intersection:
                self.__class__.intersection = True
                print("Going to Green line train")
            elif station in intersections[1] and BlueLine.intersection:
                self.__class__.intersection = True
                print("Going to Blue line train")
            else:
                self.__class__.intersection = False
            time.sleep(random.randint(0, 1) * 0.2)


class BlueLine(threading.Thread):
    intersection = False
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for station in generate_stations('blue_stations.txt'):
            print("We are on {} station at {}:{}:{}".format(station, *hour_min_now()))
            time.sleep(random.randint(0, 1)*0.1)
            if station in intersections and RedLine.intersection:
                self.__class__.intersection = True
                print("Going to Red line train")
            else:
                self.__class__.intersection = False


class GreenLine(threading.Thread):
    intersection = False
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for station in generate_stations('green_stations.txt'):
            print("We are on {} station at {}:{}:{}".format(station, *hour_min_now()))
            time.sleep(random.randint(0, 1)*0.3)
            if station in intersections and RedLine.intersection:
                self.__class__.intersection = True
                print("Going to Red line train")
            else:
                self.__class__.intersection = False

redline_train = RedLine()
blueline_train = BlueLine()
greenline_train = GreenLine()

redline_train.start()
blueline_train.start()
greenline_train.start()

