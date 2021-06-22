import unittest
import mul

class testAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mul.mult(10, 5), 50)
        self.assertEqual(mul.mult(-2, 3), -6)
        self.assertEqual(mul.mult(2, 5), 10)
        self.assertEqual(mul.mult(0, 7), 0)
        self.assertEqual(mul.mult(10, 9), 90)
        

unittest.main()