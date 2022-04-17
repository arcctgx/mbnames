#!/usr/bin/env python3

"""Tests of names module."""

import unittest
from names import asciify, is_typographic, remove_featured


class TestTypographyNormalization(unittest.TestCase):

    test_data = [
        # curly apostrophe, \u2019 and ellipsis, \u2026
        ('Could’ve Moved Mountains…', 'Could\'ve Moved Mountains...'),
        # hyphen, \u2010
        ('Half‐Light', 'Half-Light'),
        # double prime or inch symbol, \u2033
        ('12″ version', '12" version')
    ]

    def test_typography_detection(self):
        for typographic, plain_ascii in self.test_data:
            self.assertTrue(is_typographic(typographic))
            self.assertFalse(is_typographic(plain_ascii))

    def test_asciify(self):
        for typographic, asciified in self.test_data:
            test_asciified = asciify(typographic)
            self.assertEqual(asciified, test_asciified)
            self.assertFalse(is_typographic(test_asciified))


class TestRemoveFeatured(unittest.TestCase):

    def test_garbage_inputs(self):
        self.assertEqual(remove_featured('Zacier', None), 'Zacier')
        self.assertEqual(remove_featured('Zacier', ''), 'Zacier')

    def test_input_without_feat(self):
        self.assertEqual(remove_featured('Zacier', 'feat.'), 'Zacier')

    def test_inputs_with_feat(self):
        self.assertEqual(remove_featured('Clint Mansell feat. Kronos Quartet', 'feat.'),
                         'Clint Mansell')
        self.assertEqual(remove_featured('Clint Mansell feat.   Kronos Quartet', 'feat.'),
                         'Clint Mansell')
        self.assertEqual(remove_featured('Clint Mansell   feat. Kronos Quartet', 'feat.'),
                         'Clint Mansell')
        self.assertEqual(remove_featured('   Clint Mansell   feat. Kronos Quartet', 'feat.'),
                         '   Clint Mansell')
        self.assertEqual(
            remove_featured('Clint Mansell feat. Kronos Quartet feat. Zacier', 'feat.'),
            'Clint Mansell')


if __name__ == '__main__':
    unittest.main()
