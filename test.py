#!/usr/bin/python

# from contextlib import contextmanager
#
#
# class TestClass(object):
#
#     def __new__(cls, *args, **kwargs):
#         if all((('A' in arg or 'B' in arg) for arg in args)):
#             return super().__new__(cls)
#         else:
#             return object
#         # if (len(args) == 2) and ("C" in args):
#         #     return object
#         # if ((len(args) == 1) and (("A" in args) or ("B" in "args"))) or \
#         #         ((len(args) == 2) and (("A" in args) and ("B" in "args"))):
#         #     return super().__new__(cls)
#         # raise RuntimeError("Unable to specify class instance to return.")
#
#     def __init__(self, *args, **kwargs):
#         print("Create Object {}".format(self))
#
#
#
# if __name__ == '__main__':
#     mc1 = TestClass("A")
#     mc2 = TestClass("A", "B")
#     not_mc1 = TestClass("C")
#     not_mc2 = TestClass("B", "C")


import json
import argparse
from pprint import pprint

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="JSON file path")
    args = parser.parse_args()
    with open(args.file_path, encoding="utf-8") as fd:
        content = fd.read()
        json_obj = json.loads(content)

    pprint(json_obj)
