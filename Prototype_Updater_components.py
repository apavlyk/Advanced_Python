#!/usr/bin/python

import copy


class Updater():

    def start(self):
        print("Start {}".format(id(self)))

    def check_data(self, data):
        print("Data for id {}".format(id(self)))

    def run(self, component_update=False, component_list=False):
        if component_update:
            print("Run {}".format(id(self)))
            return 0
        if component_list:
            for c in component_list:
                print("-"*20, c, "-"*20)
                c = self.clone()
                c.start()
                c.check_data(id(self))
                c.run(component_update=True)

    def clone(self):
        return copy.copy(self)


if __name__ == '__main__':
    updater = Updater()
    updater.start()
    updater.check_data("data")
    updater.run(component_list=list(range(5)))
