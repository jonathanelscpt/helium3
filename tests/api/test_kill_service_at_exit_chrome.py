# -*- coding: utf-8 -*-
from unittest import TestCase, skipIf

from helium3 import start_chrome
from helium3._impl import is_windows
from tests.api import test_browser_name
from tests.api.test_kill_service_at_exit import KillServiceAtExitAT
from tests.api.util import InSubProcess


@skipIf(test_browser_name() != "chrome", "Only run this test for Chrome")
class KillServiceAtExitChromeTest(KillServiceAtExitAT, TestCase):
    def get_service_process_names(self):
        if is_windows():
            return ["chromedriver.exe"]
        return ["chromedriver"]

    def get_browser_process_name(self):
        return "chrome" + (".exe" if is_windows() else "")

    def start_browser_in_sub_process(self):
        with ChromeInSubProcess():
            pass


class ChromeInSubProcess(InSubProcess):
    @classmethod
    def main(cls):
        start_chrome(headless=True)
        cls.synchronize_with_parent_process()


if __name__ == "__main__":
    ChromeInSubProcess.main()
