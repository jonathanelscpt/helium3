# -*- coding: utf-8 -*-
from helium3 import Config
from helium3 import click
from helium3.utils.lang import TemporaryAttrValue
from tests.api import BrowserAT


class ClickTest(BrowserAT):
    def get_page(self):
        return "test_click.html"

    def test_click(self):
        click("Click me!")
        self.assertEqual("Success!", self.read_result_from_browser())

    def test_click_non_existent_element(self):
        with TemporaryAttrValue(Config, "implicit_wait_secs", 1):
            with self.assertRaises(LookupError):
                click("Non-existent")
