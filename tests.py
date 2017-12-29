import unittest
import json

import classes as cls
import calculator as calc
import palandrom as pal
import loops as lp
import exception as exp
import file_input as fi
import filtering as fil


class MyTestCase(unittest.TestCase):

    def test_classes(self):
        emp1 = cls.Employee("luv", 2000)
        self.assertEqual(emp1.name, "luv")
        self.assertEqual(emp1.salary, 2000)

        emp2 = cls.Employee("kush", 5000)
        self.assertEqual(emp2.name, "kush")
        self.assertEqual(emp2.salary, 5000)

        self.assertEqual(cls.Employee.empCount, 2)

    def test_calculator(self):
        self.assertEqual(calc.sum(2, 2), 4)
        self.assertEqual(calc.sub(2, 2), 0)
        self.assertEqual(calc.mul(2, 3), 6)
        self.assertEqual(calc.div(2, 2), 1)

    def test_palindrome(self):
        self.assertEqual(pal.reverse("abc"), "cba")
        self.assertEqual(pal.reverse("aba"), "aba")

        self.assertEqual(pal.is_palindrome("aba"), True)
        self.assertEqual(pal.is_palindrome("abc"), False)

        pal.do_process()

        with open('pala_result.json', 'r') as f:
            items = json.load(f)

        for item in items:
            self.assertEqual(item["is_palindrome"], pal.is_palindrome(item["name"]))

    def test_loops(self):
        self.assertEqual(lp.while_loop(), 9)
        self.assertEqual(lp.for_loop(), 6)
        self.assertEqual(lp.for_loop_list(), 3)
    
    def test_exception(self):
        self.assertEqual(exp.example_try_except_else(), False)

        self.assertEqual(exp.example_finally(), "In Finally")

        self.assertEqual(exp.example_try_except(), None)

    def test_file_input(self):
        fi.example_file_read_write()

        with open('helloworld.txt', 'r') as f:
            content = f.readlines()

        self.assertEqual(len(content), 1)
        self.assertEqual(content[0], "THIS IS TEST TEXT")

        fi.reset()

    def test_filtering(self):
        self.assertEqual(fil.count_cities(), 6)
