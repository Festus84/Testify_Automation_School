import unittest
import challenge10


class Testchallenge10(unittest.TestCase):

    def test_convert_string_uppercase(self):
        self.assertEqual(challenge10.sentencecase("house"), 'House')


if __name__ == '__main__':
    unittest.main()
