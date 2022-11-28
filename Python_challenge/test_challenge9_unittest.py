import unittest
import challenge9


class Testchallenge9(unittest.TestCase):

    def test_convert_string_uppercase(self):
        self.assertEqual(challenge9.convert("street"), 'STREET')
        # self.assertEqual(challenge9.uppercase("boss"), 'BOSS')


if __name__ == '__main__':
    unittest.main()
