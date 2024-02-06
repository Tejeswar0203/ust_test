import unittest

def function1(a):
    return a+2

def function2(b):
    return b*2

class test_allfunctions(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(function1(2),4)
        self.assertEqual(function1(1), 4)

    def test_function2(self):
        self.assertEqual(function2(2), 4)
        self.assertEqual(function2(1), 4)


obj=test_allfunctions()
print(obj.test_function1())
print(obj.test_function2())


