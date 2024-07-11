import unittest

from main import residue

class TestMath(unittest.TestCase):
    def test_residue(self):
        self.assertEqual(residue(10, 2), 0)
        self.assertEqual(residue(6, 4), 2)
        self.assertEqual(residue(7, 3), 1)

        self.assertNotEqual(residue(4, 3), 2)
        self.assertNotEqual(residue(8, 5), 1)
        self.assertNotEqual(residue(3, 2), 2)

    def test_residue_by_zero(self):
        self.assertRaises(ValueError, residue, 8, 0)

if __name__ == '__main__':
    unittest.main()