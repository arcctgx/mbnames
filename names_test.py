#!/usr/bin/env python3

"""Tests of names module."""

import unittest
from names import asciify


class TestAsciify(unittest.TestCase):

    def test_typographic_hyphen(self):
        self.assertEqual(asciify('Half‐Light'), 'Half-Light')

    def test_double_prime(self):
        self.assertEqual(asciify('12″ version'), '12" version')


if __name__ == '__main__':
    unittest.main()
