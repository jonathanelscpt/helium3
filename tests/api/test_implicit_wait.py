# -*- coding: utf-8 -*-
from time import time

from helium3 import Config
from helium3 import click
from helium3.utils.lang import TemporaryAttrValue
from tests.api import BrowserAT


class ImplicitWaitTest(BrowserAT):
    def get_page(self):
        return "test_implicit_wait.html"

    def test_click_text_implicit_wait(self):
        click("Click me!")
        start_time = time()
        click("Now click me!")
        end_time = time()
        self.assertEqual("Success!", self.read_result_from_browser())
        self.assertGreaterEqual(end_time - start_time, 3.0)

    def test_click_text_no_implicit_wait(self):
        with TemporaryAttrValue(Config, "implicit_wait_secs", 0):
            with self.assertRaises(LookupError):
                click("Non-existent")

    def test_click_text_too_small_implicit_wait_secs(self):
        with TemporaryAttrValue(Config, "implicit_wait_secs", 1):
            click("Click me!")
            with self.assertRaises(LookupError):
                click("Now click me!")
