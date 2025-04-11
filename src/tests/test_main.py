import unittest
from src.main import MathematicalOperation

class TestMathematicalOperation(unittest.TestCase):

    def setUp(self):
        self.math_op = MathematicalOperation()

    def test_add(self):
        self.assertEqual(self.math_op.add(1, 2), 3)
        self.assertEqual(self.math_op.add(-1, 1), 0)
        self.assertEqual(self.math_op.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.math_op.subtract(5, 3), 2)
        self.assertEqual(self.math_op.subtract(0, 0), 0)
        self.assertEqual(self.math_op.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.math_op.multiply(3, 4), 12)
        self.assertEqual(self.math_op.multiply(-1, 1), -1)
        self.assertEqual(self.math_op.multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()