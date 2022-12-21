import unittest
from projects.calculator.calculator import Calculator

class TestSum(unittest.TestCase):
    def test_sum(self):
         calculator = Calculator()
         self.assertEqual(calculator.add(2, 2), 4)

if __name__ == '__main__':
    unittest.main()