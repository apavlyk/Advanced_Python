
"""
1. Загрузить из файла uz_bukovel_event.json значения в __dict__ объекта класса Event
. Oни должны быть доступны при таком обращении:
event = Event(path_to_file)
event.summary or event.location  (__getattr__/__getattribute__)
2. Создать установщик новых значений для загруженных аттрибутов.
event.summary = "Заказ ж/д билетов в Харьков" __setattr__
3.1 Добавить метод dump(path_to_modified_file) который будет записывать новый json file
c изменениями из п.2.
3.2 добавить event.run() который принтит "Event started" + event.summary (or something else)
4*. Создать менеджер контекста для Event объета:
with Event(path_to_file) as event:
    event.summary = "Заказ ж/д билетов в Харьков"
    +3 attribute from json

5** Создать новый класс EventScheduler
5.1 Добавить возможность:
 добавления объектов Event к списку(лучше deque) events ов
 удаления объектов Event из списка(лучше deque) events ов
 итерации по списку events ов
 индексации EventScheduler обьекта (EventScheduler[1])
 EventScheduler +- event/EventScheduler2

5.2 Создать методы:
    run(event/s)
    stop(event/s)

5.3
"""

import json


def loader(json_file_path="uz_bukovel_event.json"):
    json_dict_file = open(json_file_path, 'r', encoding='utf8')
    json_dict = json.loads(json_dict_file.read())
    return json_dict


class JEventMeta(type):
    def __new__(cls, cls_name, bases, clsdict):
        clsdict.update(loader())
        clsobj = super().__new__(cls, cls_name, bases, clsdict)
        return clsobj


class JEvent(metaclass=JEventMeta):
    data = 10

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


if __name__ == '__main__':
    event = JEvent()
    print(event.__dict__)
    pass
