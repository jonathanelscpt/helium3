# -*- coding: utf-8 -*-
from unittest import TestCase

from helium3.utils.xpath import predicate_or


class PredicateOrTest(TestCase):
    def test_no_args(self):
        self.assertEqual("", predicate_or())

    def test_one_arg(self):
        self.assertEqual("[a=b]", predicate_or("a=b"))

    def test_two_args(self):
        self.assertEqual("[a=b or c=d]", predicate_or("a=b", "c=d"))

    def test_one_empty_arg(self):
        self.assertEqual("", predicate_or(""))

    def test_empty_arg_among_normal_args(self):
        self.assertEqual("[a=b or c=d]", predicate_or("a=b", "", "c=d"))
