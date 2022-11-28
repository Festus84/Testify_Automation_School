import unittest
import challenge2


class Testchallenge2(unittest.TestCase):
    def test_power(self):
        self.assertEqual(challenge2.power_of_number(3, 2), 9)

if __name__ == '__main__':
        unittest.main()
