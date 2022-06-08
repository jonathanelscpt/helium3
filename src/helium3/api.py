# -*- coding: utf-8 -*-
from helium3._impl import APIImpl

_API_IMPL = None


def _get_api_impl():
    global _API_IMPL
    if _API_IMPL is None:
        _API_IMPL = APIImpl()
    return _API_IMPL


def start_chrome(
    url=None, headless=False, maximize=False, options=None, capabilities=None
):
    """
    :param url: URL to open.
    :type url: str
    :param headless: Whether to start Chrome in headless mode.
    :type headless: bool
    :param maximize: Whether to maximize the Chrome window. Ignored when `headless` is set to `True`.
    :type maximize: bool
    :param options: ChromeOptions to use for starting the browser
    :type options: :py:class:`selenium.webdriver.ChromeOptions`
    :param capabilities: DesiredCapabilities to use for starting the browser
    :type capabilities: :py:class:`selenium.webdriver.DesiredCapabilities`

    Starts an instance of Google Chrome::

            start_chrome()

    If this doesn't work for you, then it may be that Helium's copy of
    ChromeDriver is not compatible with your version of Chrome. To fix this,
    place a copy of ChromeDriver on your `PATH`.

    You can optionally open a URL::

            start_chrome("google.com")

    The `headless` switch lets you prevent the browser window from appearing on
    your screen::

            start_chrome(headless=True)
            start_chrome("google.com", headless=True)

    For more advanced configuration, use the `options` or `capabilities`
    parameters::

            from selenium.webdriver import ChromeOptions
            options = ChromeOptions()
            options.add_argument('--proxy-server=1.2.3.4:5678')
            start_chrome(options=options)

            from selenium.webdriver import DesiredCapabilities
            capabilities = DesiredCapabilities.CHROME
            capabilities["pageLoadStrategy"] = "none"
            capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
            start_chrome(capabilities=capabilities)

    On shutdown of the Python interpreter, Helium cleans up all resources used
    for controlling the browser (such as the ChromeDriver process), but does
    not close the browser itself. If you want to terminate the browser at the
    end of your script, use the following command::

            kill_browser()
    """
    return _get_api_impl().start_chrome_impl(
        url, headless, maximize, options, capabilities
    )


def start_firefox(url=None, headless=False, options=None):
    """
    :param url: URL to open.
    :type url: str
    :param headless: Whether to start Firefox in headless mode.
    :type headless: bool
    :param options: FirefoxOptions to use for starting the browser.
    :type options: :py:class:`selenium.webdriver.FirefoxOptions`

    Starts an instance of Firefox::

            start_firefox()

    If this doesn't work for you, then it may be that Helium's copy of
    geckodriver is not compatible with your version of Firefox. To fix this,
    place a copy of geckodriver on your `PATH`.

    You can optionally open a URL::

            start_firefox("google.com")

    The `headless` switch lets you prevent the browser window from appearing on
    your screen::

            start_firefox(headless=True)
            start_firefox("google.com", headless=True)

    For more advanced configuration, use the `options` parameter::

            from selenium.webdriver import FirefoxOptions
            options = FirefoxOptions()
            options.add_argument("--width=2560")
            options.add_argument("--height=1440")
            start_firefox(options=options)

    On shutdown of the Python interpreter, Helium cleans up all resources used
    for controlling the browser (such as the geckodriver process), but does
    not close the browser itself. If you want to terminate the browser at the
    end of your script, use the following command::

            kill_browser()
    """
    return _get_api_impl().start_firefox_impl(url, headless, options)


def go_to(url):
    """
    :param url: URL to open.
    :type url: str

    Opens the specified URL in the current web browser window. For instance::

            go_to("google.com")
    """
    _get_api_impl().go_to_impl(url)


def set_driver(driver):
    """
    Sets the Selenium WebDriver used to execute Helium commands. See also
    :py:func:`get_driver`.
    """
    _get_api_impl().set_driver_impl(driver)


def get_driver():
    """
    Returns the Selenium WebDriver currently used by Helium to execute all
    commands. Each Helium command such as ``click("Login")`` is translated to a
    sequence of Selenium commands that are issued to this driver.
    """
    return _get_api_impl().get_driver_impl()


def write(text, into=None):
    """
    :param text: The text to be written.
    :type text: one of str, unicode
    :param into: The element to write into.
    :type into: one of str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement`, :py:class:`Alert`

    Types the given text into the active window. If parameter 'into' is given,
    writes the text into the text field or element identified by that parameter.
    Common examples of 'write' are::

        write("Hello World!")
        write("user12345", into="Username:")
        write("Michael", into=Alert("Please enter your name"))
    """
    _get_api_impl().write_impl(text, into)


def press(key):
    """
    :param key: Key or combination of keys to be pressed.

    Presses the given key or key combination. To press a normal letter key such
    as 'a' simply call `press` for it::

            press('a')

    You can also simulate the pressing of upper case characters that way::

            press('A')

    The special keys you can press are those given by Selenium's class
    :py:class:`selenium.webdriver.common.keys.Keys`. Helium makes all those keys
    available through its namespace, so you can just use them without having to
    refer to :py:class:`selenium.webdriver.common.keys.Keys`. For instance, to
    press the Enter key::

            press(ENTER)

    To press multiple keys at the same time, concatenate them with `+`. For
    example, to press Control + a, call::

            press(CONTROL + 'a')
    """
    _get_api_impl().press_impl(key)


def click(element):
    """
    :param element: The element or point to click.
    :type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

    Clicks on the given element or point. Common examples are::

        click("Sign in")
        click(Button("OK"))
        click(Point(200, 300))
        click(ComboBox("File type").top_left + (50, 0))
    """
    _get_api_impl().click_impl(element)


def doubleclick(element):
    """
    :param element: The element or point to click.
    :type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

    Performs a double-click on the given element or point. For example::

        doubleclick("Double click here")
        doubleclick(Image("Directories"))
        doubleclick(Point(200, 300))
        doubleclick(TextField("Username").top_left - (0, 20))
    """
    _get_api_impl().doubleclick_impl(element)


def drag(element, to):
    """
    :param element: The element or point to drag.
    :type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`
    :param to: The element or point to drag to.
    :type to: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

    Drags the given element or point to the given location. For example::

        drag("Drag me!", to="Drop here.")

    The dragging is performed by hovering the mouse cursor over ``element``,
    pressing and holding the left mouse button, moving the mouse cursor over
    ``to``, and then releasing the left mouse button again.

    This function is exclusively used for dragging elements inside one web page.
    If you wish to drag a file from the hard disk onto the browser window (eg.
    to initiate a file upload), use function :py:func:`drag_file`.
    """
    _get_api_impl().drag_impl(element, to)


def press_mouse_on(element):
    _get_api_impl().press_mouse_on_impl(element)


def release_mouse_over(element):
    _get_api_impl().release_mouse_over_impl(element)


def find_all(predicate):
    """
    Lets you find all occurrences of the given GUI element predicate. For
    instance, the following statement returns a list of all buttons with label
    "Open"::

            find_all(Button("Open"))

    Other examples are::

            find_all(Window())
            find_all(TextField("Address line 1"))

    The function returns a list of elements of the same type as the passed-in
    parameter. For instance, ``find_all(Button(...))`` yields a list whose
    elements are of type :py:class:`Button`.

    In a typical usage scenario, you want to pick out one of the occurrences
    returned by :py:func:`find_all`. In such cases, :py:func:`list.sort` can
    be very useful. For example, to find the leftmost "Open" button, you can
    write::

            buttons = find_all(Button("Open"))
            leftmost_button = sorted(buttons, key=lambda button: button.x)[0]
    """
    return _get_api_impl().find_all_impl(predicate)


def scroll_down(num_pixels=100):
    """
    Scrolls down the page the given number of pixels.
    """
    _get_api_impl().scroll_down_impl(num_pixels)


def scroll_up(num_pixels=100):
    """
    Scrolls the the page up the given number of pixels.
    """
    _get_api_impl().scroll_up_impl(num_pixels)


def scroll_right(num_pixels=100):
    """
    Scrolls the page to the right the given number of pixels.
    """
    _get_api_impl().scroll_right_impl(num_pixels)


def scroll_left(num_pixels=100):
    """
    Scrolls the page to the left the given number of pixels.
    """
    _get_api_impl().scroll_left_impl(num_pixels)


def hover(element):
    """
    :param element: The element or point to hover.
    :type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

    Hovers the mouse cursor over the given element or point. For example::

        hover("File size")
        hover(Button("OK"))
        hover(Link("Download"))
        hover(Point(200, 300))
        hover(ComboBox("File type").top_left + (50, 0))
    """
    _get_api_impl().hover_impl(element)


def right_click(element):
    """
    :param element: The element or point to click.
    :type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

    Performs a right click on the given element or point. For example::

        rightclick("Something")
        rightclick(Point(200, 300))
        rightclick(Image("captcha"))
    """
    _get_api_impl().rightclick_impl(element)


def select(combo_box, value):
    """
    :param combo_box: The combo box whose value should be changed.
    :type combo_box: str, unicode or :py:class:`ComboBox`
    :param value: The visible value of the combo box to be selected.

    Selects a value from a combo box. For example::

            select("Language", "English")
            select(ComboBox("Language"), "English")
    """
    _get_api_impl().select_impl(combo_box, value)


def drag_file(file_path, to):
    """
    Simulates the dragging of a file from the computer over the browser window
    and dropping it over the given element. This allows, for example, to attach
    files to emails in Gmail::

            click("COMPOSE")
            write("example@gmail.com", into="To")
            write("Email subject", into="Subject")
            drag_file(r"C:\\Documents\\notes.txt", to="Drop files here")
    """
    _get_api_impl().drag_file_impl(file_path, to)


def attach_file(file_path, to=None):
    """
    :param file_path: The path of the file to be attached.
    :param to: The file input element to which the file should be attached.

    Allows attaching a file to a file input element. For instance::

            attach_file("c:/test.txt", to="Please select a file:")

    The file input element is identified by its label. If you omit the ``to=``
    parameter, then Helium attaches the file to the first file input element it
    finds on the page.
    """
    _get_api_impl().attach_file_impl(file_path, to=to)


def refresh():
    """
    Refreshes the current page. If an alert dialog is open, then Helium first
    closes it.
    """
    _get_api_impl().refresh_impl()


def wait_until(condition_fn, timeout_secs=10, interval_secs=0.5):
    """
    :param condition_fn: A function taking no arguments that represents the \
    condition to be waited for.
    :param timeout_secs: The timeout, in seconds, after which the condition is \
    deemed to have failed.
    :param interval_secs: The interval, in seconds, at which the condition \
    function is polled to determine whether the wait has succeeded.

    Waits until the given condition function evaluates to true. This is most
    commonly used to wait for an element to exist::

        wait_until(Text("Finished!").exists)

    More elaborate conditions are also possible using Python lambda
    expressions. For instance, to wait until a text no longer exists::

        wait_until(lambda: not Text("Uploading...").exists())

    ``wait_until`` raises
    :py:class:`selenium.common.exceptions.TimeoutException` if the condition is
    not satisfied within the given number of seconds. The parameter
    ``interval_secs`` specifies the number of seconds Helium waits between
    evaluating the condition function.
    """
    _get_api_impl().wait_until_impl(condition_fn, timeout_secs, interval_secs)


def switch_to(window):
    """
    :param window: The title (string) of a browser window or a \
:py:class:`Window` object

    Switches to the given browser window. For example::

        switch_to("Google")

    This searches for a browser window whose title contains "Google", and
    activates it.

    If there are multiple windows with the same title, then you can use
    :py:func:`find_all` to find all open windows, pick out the one you want and
    pass that to ``switch_to``. For example, the following snippet switches to
    the first window in the list of open windows::

        switch_to(find_all(Window())[0])
    """
    _get_api_impl().switch_to_impl(window)


def kill_browser():
    """
    Closes the current browser with all associated windows and potentially open
    dialogs. Dialogs opened as a response to the browser closing (eg. "Are you
    sure you want to leave this page?") are also ignored and closed.

    This function is most commonly used to close the browser at the end of an
    automation run::

            start_chrome()
            ...
            # Close Chrome:
            kill_browser()
    """
    _get_api_impl().kill_browser_impl()


def highlight(element):
    """
    :param element: The element to highlight.

    Highlights the given element on the webpage by drawing a red rectangle
    around it. This is useful for debugging purposes. For example::

            highlight("Helium")
            highlight(Button("Sign in"))
    """
    _get_api_impl().highlight_impl(element)
