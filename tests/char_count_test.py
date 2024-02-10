import unittest

from StringCount import Count


class TestCharCount(unittest.TestCase):

    def setUp(self):
        self.count = Count('panda')

    def test_count_letters(self):
        actual_count = self.count.count_letters()
        expected_count = {'p': 1, 'a': 2, 'n': 1, 'd': 1}
        self.assertEqual(actual_count, expected_count)

    def test_count_letters_negative(self):
        actual_count = self.count.count_letters()
        expected_count = {'p': 1, 'a': 1, 'n': 1, 'd': 1}
        self.assertNotEqual(actual_count, expected_count)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCharCount)
unittest.TextTestRunner(verbosity=2).run(suite)
