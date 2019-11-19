#!/usr/bin/python


import os




class BaseNewLine():

    def __init__(self, name, *args, **kwargs):
        super().__init__()
        self._name = name

    @property
    def data(self):
        return

    @property
    def os(self):
        return self._name


class DebianNewLine(BaseNewLine):

    @property
    def data(self):
        return "LF"


class WinNewLine(BaseNewLine):

    @property
    def data(self):
        return "CRLF"


class MacNewLine(BaseNewLine):

    @property
    def data(self):
        return "CR"


OS_DICT = {
    "Debian": DebianNewLine,
    "Windows": WinNewLine,
    "Mac": MacNewLine
}


class NewLine():

    def __new__(cls, os_name, *args, **kwargs):
        pass

        # if os_name == 'Debian':
        #     return DebianNewLine(os_name, *args, **kwargs)
        # elif os_name == 'Windows':
        #     return WinNewLine(os_name, *args, **kwargs)
        # elif os_name == 'Mac':
        #     return MacNewLine(os_name, *args, **kwargs)
        # else:
        #     raise RuntimeError("Unable to create object for {} OS. Available OS".format(os_name))


if __name__ == '__main__':
    new_line = NewLine("Win")
    print(new_line.data)
    print(new_line.os)
