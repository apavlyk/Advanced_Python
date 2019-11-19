#!/usr/bin/python


class A(object):
    pass


class B(A):
    pass


if __name__ == '__main__':
    print(B.__mro__)
    print(B.__dict__)
    print(type(B))
