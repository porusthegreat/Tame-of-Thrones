import unittest

from Kingdom import Kingdom


class TestKingdom(unittest.TestCase):

    def setUp(self):
        self.kingdom = Kingdom('Air', 'owl')

    def test_get_kingdom_name(self):
        kingdom_name = self.kingdom.get_name()
        self.assertEqual(kingdom_name, 'Air')

    def test_get_emblem(self):
        emblem = self.kingdom.get_emblem()
        self.assertEqual(emblem, 'owl')

    def test_get_emblem_char_count(self):
        actual_char_count = self.kingdom.get_character_count_for_emblem()
        expected_char_count = {'o': 1, 'w': 1, 'l': 1}
        self.assertEqual(actual_char_count, expected_char_count)

    def test_is_kingdom_defeated_positive(self):
        message_count = {'o': 1, 'w': 1, 'l': 1}
        expected_val = self.kingdom.is_kingdom_defeated(message_count)
        self.assertEqual(expected_val, True)

    def test_is_kingdom_defeated_negative(self):
        message_count = {'p': 0, 'a': 2, 'n': 1}
        expected_val = self.kingdom.is_kingdom_defeated(message_count)
        self.assertEqual(expected_val, False)

    def test_get_kingdom_name_if_defeated(self):
        actual_output = self.kingdom.get_kingdom_name_if_defeated({'air': 'owl'}, 'air')
        self.assertEqual('air', actual_output)

    def test_get_kingdom_name_if_defeated_negative(self):
        actual_output = self.kingdom.get_kingdom_name_if_defeated({'air': 'test'}, 'air')
        self.assertEqual(None, actual_output)


suite = unittest.TestLoader().loadTestsFromTestCase(TestKingdom)
unittest.TextTestRunner(verbosity=2).run(suite)
