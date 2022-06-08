# -*- coding: utf-8 -*-
"""
Helium's API is contained in module ``helium``. It is a simple Python API that
makes specifying web automation cases as simple as describing them to someone
looking over their shoulder at a screen.

The public functions and classes of Helium are listed below. If you wish to use
Helium functions in your Python scripts you can import them from the
``helium`` module::

    from helium import *
"""
from selenium.webdriver.common.keys import Keys

from helium3._impl import APIImpl
from helium3.api import *
from helium3.elements import *
from helium3.utils.html import get_easily_readable_snippet
from helium3.utils.inspect_ import repr_args

NULL = Keys.NULL
CANCEL = Keys.CANCEL
HELP = Keys.HELP
BACK_SPACE = Keys.BACK_SPACE
TAB = Keys.TAB
CLEAR = Keys.CLEAR
RETURN = Keys.RETURN
ENTER = Keys.ENTER
SHIFT = Keys.SHIFT
LEFT_SHIFT = Keys.LEFT_SHIFT
CONTROL = Keys.CONTROL
LEFT_CONTROL = Keys.LEFT_CONTROL
ALT = Keys.ALT
LEFT_ALT = Keys.LEFT_ALT
PAUSE = Keys.PAUSE
ESCAPE = Keys.ESCAPE
SPACE = Keys.SPACE
PAGE_UP = Keys.PAGE_UP
PAGE_DOWN = Keys.PAGE_DOWN
END = Keys.END
HOME = Keys.HOME
LEFT = Keys.LEFT
ARROW_LEFT = Keys.ARROW_LEFT
UP = Keys.UP
ARROW_UP = Keys.ARROW_UP
RIGHT = Keys.RIGHT
ARROW_RIGHT = Keys.ARROW_RIGHT
DOWN = Keys.DOWN
ARROW_DOWN = Keys.ARROW_DOWN
INSERT = Keys.INSERT
DELETE = Keys.DELETE
SEMICOLON = Keys.SEMICOLON
EQUALS = Keys.EQUALS
NUMPAD0 = Keys.NUMPAD0
NUMPAD1 = Keys.NUMPAD1
NUMPAD2 = Keys.NUMPAD2
NUMPAD3 = Keys.NUMPAD3
NUMPAD4 = Keys.NUMPAD4
NUMPAD5 = Keys.NUMPAD5
NUMPAD6 = Keys.NUMPAD6
NUMPAD7 = Keys.NUMPAD7
NUMPAD8 = Keys.NUMPAD8
NUMPAD9 = Keys.NUMPAD9
MULTIPLY = Keys.MULTIPLY
ADD = Keys.ADD
SEPARATOR = Keys.SEPARATOR
SUBTRACT = Keys.SUBTRACT
DECIMAL = Keys.DECIMAL
DIVIDE = Keys.DIVIDE
F1 = Keys.F1
F2 = Keys.F2
F3 = Keys.F3
F4 = Keys.F4
F5 = Keys.F5
F6 = Keys.F6
F7 = Keys.F7
F8 = Keys.F8
F9 = Keys.F9
F10 = Keys.F10
F11 = Keys.F11
F12 = Keys.F12
META = Keys.META
COMMAND = Keys.COMMAND


class Config:
    """
    This class contains Helium's run-time configuration. To modify Helium's
    behaviour, simply assign to the properties of this class. For instance::

            Config.implicit_wait_secs = 0

    ``implicit_wait_secs`` is Helium's analogue to Selenium's
    ``.implicitly_wait(secs)``. Suppose you have a script that executes the
    following command::

        >>> click("Download")

    If the "Download" element is not immediately available, then Helium waits up
    to ``implicit_wait_secs`` for it to appear before raising a
    ``LookupError``. This is useful in situations where the page takes slightly
    longer to load, or a GUI element only appears after a certain time.

    To disable Helium's implicit waits, simply execute::

        Config.implicit_wait_secs = 0

    Helium's implicit waits do not affect commands :py:func:`find_all` or
    :py:func:`GUIElement.exists`. Note also that setting
    ``implicit_wait_secs`` does not affect the underlying Selenium driver
    (see :py:func:`get_driver`).

    For the best results, it is recommended to not use Selenium's
    ``.implicitly_wait(...)`` in conjunction with Helium.
    """

    implicit_wait_secs = 10
