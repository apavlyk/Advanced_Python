import requests
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("first", help = 'help str1')
# parser.add_argument("last", help = 'help str2')
# parser.add_argument("-p", "--pay", default=1211, dest='EPAY', metavar='PAY', type=int, help = 'help str3')
# parser.add_argument("--secret", help=argparse.SUPPRESS)
#
# mgrp = parser.add_mutually_exclusive_group()
# mgrp.add_argument('--xml', action='store_true', help="Get xml data")
# mgrp.add_argument('--html', action='store_true', help="Get html data")
# mgrp.add_argument('--yaml', action='store_true', help="Get yaml data")
# mgrp.add_argument('--json', action='store_true', help="Get json data")
#
# args = parser.parse_args()
# args.first, args.last, args.pay


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    # def __init__(self, first, last, pay):
    def __init__(self):

        self.parser = argparse.ArgumentParser(description="Employee date", epilog="This is the end!")

        self.parser.add_argument("first_name", help="Employee first name")
        self.parser.add_argument("last_name", help="Employee last_name")
        self.parser.add_argument("--p",  "--payment", dest="pay", type=float, default=10000, help=argparse.SUPPRESS)

        self.args = self.parser.parse_args()
        self.first = self.args.first_name
        self.last = self.args.last_name

        self. pay = self.args.pay

        print(self.__dict__)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


if __name__ == "__main__":
    # first, last, pay = args.first, args.last, args.EPAY
    # emp = Employee(first, last, pay)
    emp = Employee()
    emp.apply_raise()
    print(emp.pay)
