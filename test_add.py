import unittest
import add

class testAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add.sum(10, 5), 15)
        self.assertEqual(add.sum(-2, 3), 1)
        self.assertEqual(add.sum(2, 5), 7)
        self.assertEqual(add.sum(0, 7), 7)
        self.assertEqual(add.sum(10, 9), 19)
        

unittest.main()