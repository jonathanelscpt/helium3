# -*- coding: utf-8 -*-
from unittest import TestCase

from helium3.utils.dictionary import inverse


class InverseTest(TestCase):
    def test_inverse_empty(self):
        self.assertEqual({}, inverse({}))

    def test_inverse(self):
        names_for_ints = {0: {"zero", "naught"}, 1: {"one"}}
        ints_for_names = {"zero": {0}, "naught": {0}, "one": {1}}
        self.assertEqual(ints_for_names, inverse(names_for_ints))
