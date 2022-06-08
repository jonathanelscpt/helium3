# -*- coding: utf-8 -*-
from helium3 import click
from helium3 import right_click
from tests.api import BrowserAT


class RightclickTest(BrowserAT):
    def get_page(self):
        return "test_rightclick.html"

    def test_simple_rightclick(self):
        right_click("Perform a normal rightclick here.")
        self.assertEqual(
            "Normal rightclick performed.", self.read_result_from_browser()
        )

    def test_rightclick_select_normal_item(self):
        right_click("Rightclick here for context menu.")
        click("Normal item")
        self.assertEqual("Normal item selected.", self.read_result_from_browser())
