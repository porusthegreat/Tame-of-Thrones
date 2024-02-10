import unittest

from War import War


class WarTests(unittest.TestCase):

    def setUp(self):
        self.war = War()
        self.input_dict = {'air': 'owl'}

    def test_verify_message_for_all_kingdoms(self):
        self.war.verify_message_for_all_kingdoms(self.input_dict)
        self.assertEqual(self.war.get_allies()[0], 'air')

    def test_verify_message_for_all_kingdoms_negative(self):
        self.war.verify_message_for_all_kingdoms(self.input_dict)
        self.assertNotEqual(self.war.get_allies()[0], 'test')
