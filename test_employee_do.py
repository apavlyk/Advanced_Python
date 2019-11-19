#!/usr/bin/python

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("Invoke setUp")
        self.employee_1 = Employee("John", "Smith", 5000)
        self.employee_2 = Employee("Jim", "Kitting", 10000)

    def test_full_name(self):
        self.assertEqual(self.employee_1.fullname, "John Smith")
        self.assertEqual(self.employee_2.fullname, "Jim Kitting")

    def test_apply_raise(self):
        self.employee_2.apply_raise()
        self.assertEqual(self.employee_2.pay, 10500)


if __name__ == '__main__':
    unittest.main()
