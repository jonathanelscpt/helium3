# -*- coding: utf-8 -*-
from collections import OrderedDict
from collections import namedtuple
from copy import copy

import helium3._impl
from helium3.api import _get_api_impl
from helium3.utils.html import get_easily_readable_snippet
from helium3.utils.inspect_ import repr_args


class GUIElement:
    def __init__(self):
        self._driver = _get_api_impl().require_driver()
        self._args = []
        self._kwargs = OrderedDict()
        self._impl_cached = None

    def exists(self):
        """
        Evaluates to true if this GUI element exists.
        """
        return self._impl.exists()

    def with_impl(self, impl):
        result = copy(self)
        result._impl = impl
        return result

    @property
    def _impl(self):
        if self._impl_cached is None:
            impl_class = getattr(
                helium3._impl, self.__class__.__name__ + "Impl"
            )  # ugly, requires rework. 'helium3._impl'
            self._impl_cached = impl_class(self._driver, *self._args, **self._kwargs)
        return self._impl_cached

    @_impl.setter
    def _impl(self, value):
        self._impl_cached = value

    def __repr__(self):
        return self._repr_constructor_args(self._args, self._kwargs)

    def _repr_constructor_args(self, args=None, kwargs=None):
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        return "%s(%s)" % (
            self.__class__.__name__,
            repr_args(self.__init__, args, kwargs, repr),
        )

    def _is_bound(self):
        return self._impl_cached is not None and self._impl_cached._is_bound()


class HTMLElement(GUIElement):
    def __init__(self, below=None, to_right_of=None, above=None, to_left_of=None):
        super(HTMLElement, self).__init__()
        self._kwargs["below"] = below
        self._kwargs["to_right_of"] = to_right_of
        self._kwargs["above"] = above
        self._kwargs["to_left_of"] = to_left_of

    @property
    def width(self):
        """
        The width of this HTML element, in pixels.
        """
        return self._impl.width

    @property
    def height(self):
        """
        The height of this HTML element, in pixels.
        """
        return self._impl.height

    @property
    def x(self):
        """
        The x-coordinate on the page of the top-left point of this HTML element.
        """
        return self._impl.x

    @property
    def y(self):
        """
        The y-coordinate on the page of the top-left point of this HTML element.
        """
        return self._impl.y

    @property
    def top_left(self):
        """
        The top left corner of this element, as a :py:class:`helium.Point`.
        This point has exactly the coordinates given by this element's `.x` and
        `.y` properties. `top_left` is for instance useful for clicking at an
        offset of an element::

                click(Button("OK").top_left + (30, 15))
        """
        return self._impl.top_left

    @property
    def web_element(self):
        """
        The Selenium WebElement corresponding to this element.
        """
        return self._impl.web_element

    def __repr__(self):
        if self._is_bound():
            element_html = self.web_element.get_attribute("outerHTML")
            return get_easily_readable_snippet(element_html)
        else:
            return super(HTMLElement, self).__repr__()


class S(HTMLElement):
    """
    :param selector: The selector used to identify the HTML element(s).

    A jQuery-style selector for identifying HTML elements by ID, name, CSS
    class, CSS selector or XPath. For example: Say you have an element with
    ID "myId" on a web page, such as ``<div id="myId" .../>``.
    Then you can identify this element using ``S`` as follows::

            S("#myId")

    The parameter which you pass to ``S(...)`` is interpreted by Helium
    according to these rules:

     * If it starts with an ``@``, then it identifies elements by HTML ``name``.
       Eg. ``S("@btnName")`` identifies an element with ``name="btnName"``.
     * If it starts with ``//``, then Helium interprets it as an XPath.
     * Otherwise, Helium interprets it as a CSS selector. This in particular
       lets you write ``S("#myId")`` to identify an element with ``id="myId"``,
       or ``S(".myClass")`` to identify elements with ``class="myClass"``.

    ``S`` also makes it possible to read plain text data from a web page. For
    example, suppose you have a table of people's email addresses. Then you
    can read the list of email addresses as follows::

            email_cells = find_all(S("table > tr > td", below="Email"))
            emails = [cell.web_element.text for cell in email_cells]

    Where ``email`` is the column header (``<th>Email</th>``). Similarly to
    ``below`` and ``to_right_of``, the keyword parameters ``above`` and
    ``to_left_of`` can be used to search for elements above and to the left
    of other web elements.
    """

    def __init__(
        self, selector, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(S, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(selector)


class Text(HTMLElement):
    """
    Lets you identify any text or label on a web page. This is most useful for
    checking whether a particular text exists::

            if Text("Do you want to proceed?").exists():
                click("Yes")

    ``Text`` also makes it possible to read plain text data from a web page. For
    example, suppose you have a table of people's email addresses. Then you
    can read John's email addresses as follows::

            Text(below="Email", to_right_of="John").value

    Similarly to ``below`` and ``to_right_of``, the keyword parameters ``above``
    and ``to_left_of`` can be used to search for texts above and to the left of
    other web elements.
    """

    def __init__(
        self, text=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(Text, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(text)

    @property
    def value(self):
        """
        Returns the current value of this Text object.
        """
        return self._impl.value


class Link(HTMLElement):
    """
    Lets you identify a link on a web page. A typical usage of ``Link`` is::

            click(Link("Sign in"))

    You can also read a ``Link``'s properties. This is most typically used to
    check for a link's existence before clicking on it::

            if Link("Sign in").exists():
                click(Link("Sign in"))

    When there are multiple occurrences of a link on a page, you can
    disambiguate between them using the keyword parameters ``below``,
    ``to_right_of``, ``above`` and ``to_left_of``. For instance::

            click(Link("Block User", to_right_of="John Doe"))
    """

    def __init__(
        self, text=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(Link, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(text)

    @property
    def href(self):
        """
        Returns the URL of the page the link goes to.
        """
        return self._impl.href


class ListItem(HTMLElement):
    """
    Lets you identify a list item (HTML ``<li>`` element) on a web page. This is
    often useful for interacting with elements of a navigation bar::

            click(ListItem("News Feed"))

    In other cases such as an automated test, you might want to query the
    properties of a ``ListItem``. For example, the following line checks whether
    a list item with text "List item 1" exists, and raises an error if not::

            assert ListItem("List item 1").exists()

    When there are multiple occurrences of a list item on a page, you can
    disambiguate between them using the keyword parameters ``below``,
    ``to_right_of``, ``above`` and ``to_left_of``. For instance::

            click(ListItem("List item 1", below="My first list:"))
    """

    def __init__(
        self, text=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(ListItem, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(text)


class Button(HTMLElement):
    """
    Lets you identify a button on a web page. A typical usage of ``Button`` is::

            click(Button("Log In"))

    ``Button`` also lets you read a button's properties. For example, the
    following snippet clicks button "OK" only if it exists::

            if Button("OK").exists():
                click(Button("OK"))

    When there are multiple occurrences of a button on a page, you can
    disambiguate between them using the keyword parameters ``below``,
    ``to_right_of``, ``above`` and ``to_left_of``. For instance::

            click(Button("Log In", below=TextField("Password")))
    """

    def __init__(
        self, text=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(Button, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(text)

    def is_enabled(self):
        """
        Returns true if this UI element can currently be interacted with.
        """
        return self._impl.is_enabled()


class Image(HTMLElement):
    """
    Lets you identify an image (HTML ``<img>`` element) on a web page.
    Typically, this is done via the image's alt text. For instance::

            click(Image(alt="Helium Logo"))

    You can also query an image's properties. For example, the following snippet
    clicks on the image with alt text "Helium Logo" only if it exists::

            if Image("Helium Logo").exists():
                click(Image("Helium Logo"))

    When there are multiple occurrences of an image on a page, you can
    disambiguate between them using the keyword parameters ``below``,
    ``to_right_of``, ``above`` and ``to_left_of``. For instance::

            click(Image("Helium Logo", to_left_of=ListItem("Download")))
    """

    def __init__(
        self, alt=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(Image, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(alt)


class TextField(HTMLElement):
    """
    Lets you identify a text field on a web page. This is most typically done to
    read the value of a text field. For example::

            TextField("First name").value

    This returns the value of the "First name" text field. If it is empty, the
    empty string "" is returned.

    When there are multiple occurrences of a text field on a page, you can
    disambiguate between them using the keyword parameters ``below``,
    ``to_right_of``, ``above`` and ``to_left_of``. For instance::

            TextField("Address line 1", below="Billing Address:").value
    """

    def __init__(
        self, label=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(TextField, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(label)

    @property
    def value(self):
        """
        Returns the current value of this text field. '' if there is no value.
        """
        return self._impl.value

    def is_enabled(self):
        """
        Returns true if this UI element can currently be interacted with.

        The difference between a text field being 'enabled' and 'editable' is
        mostly visual: If a text field is not enabled, it is usually greyed out,
        whereas if it is not editable it looks normal. See also ``is_editable``.
        """
        return self._impl.is_enabled()

    def is_editable(self):
        """
        Returns true if the value of this UI element can be modified.

        The difference between a text field being 'enabled' and 'editable' is
        mostly visual: If a text field is not enabled, it is usually greyed out,
        whereas if it is not editable it looks normal. See also ``is_enabled``.
        """
        return self._impl.is_editable()


class ComboBox(HTMLElement):
    """
    Lets you identify a combo box on a web page. This can for instance be used
    to determine the current value of a combo box::

            ComboBox("Language").value

    A ComboBox may be *editable*, which means that it is possible to type in
    arbitrary values in addition to selecting from a predefined drop-down list
    of values. The property :py:func:`ComboBox.is_editable` can be used to
    determine whether this is the case for a particular combo box instance.

    When there are multiple occurrences of a combo box on a page, you can
    disambiguate between them using the keyword parameters ``below``,
    ``to_right_of``, ``above`` and ``to_left_of``. For instance::

            select(ComboBox(to_right_of="John Doe", below="Status"), "Active")

    This sets the Status of John Doe to Active on the page.
    """

    def __init__(
        self, label=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(ComboBox, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(label)

    def is_editable(self):
        """
        Returns whether this combo box allows entering an arbitrary text in
        addition to selecting predefined values from a drop-down list.
        """
        return self._impl.is_editable()

    @property
    def value(self):
        """
        Returns the currently selected combo box value.
        """
        return self._impl.value

    @property
    def options(self):
        """
        Returns a list of all possible options available to choose from in the
        ComboBox.
        """
        return self._impl.options


class CheckBox(HTMLElement):
    """
    Lets you identify a check box on a web page. To tick a currently unselected
    check box, use::

            click(CheckBox("I agree"))

    ``CheckBox`` also lets you read the properties of a check box. For example,
    the method :py:func:`CheckBox.is_checked` can be used to only click a check
    box if it isn't already checked::

            if not CheckBox("I agree").is_checked():
                click(CheckBox("I agree"))

    When there are multiple occurrences of a check box on a page, you can
    disambiguate between them using the keyword parameters ``below``,
    ``to_right_of``, ``above`` and ``to_left_of``. For instance::

            click(CheckBox("Stay signed in", below=Button("Sign in")))
    """

    def __init__(
        self, label=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(CheckBox, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(label)

    def is_enabled(self):
        """
        Returns True if this GUI element can currently be interacted with.
        """
        return self._impl.is_enabled()

    def is_checked(self):
        """
        Returns True if this GUI element is checked (selected).
        """
        return self._impl.is_checked()


class RadioButton(HTMLElement):
    """
    Lets you identify a radio button on a web page. To select a currently
    unselected radio button, use::

            click(RadioButton("Windows"))

    ``RadioButton`` also lets you read the properties of a radio button. For
    example, the method :py:func:`RadioButton.is_selected` can be used to only
    click a radio button if it isn't already selected::

            if not RadioButton("Windows").is_selected():
                click(RadioButton("Windows"))

    When there are multiple occurrences of a radio button on a page, you can
    disambiguate between them using the keyword parameters ``below``,
    ``to_right_of``, ``above`` and ``to_left_of``. For instance::

            click(RadioButton("I accept", below="License Agreement"))
    """

    def __init__(
        self, label=None, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(RadioButton, self).__init__(
            below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of
        )
        self._args.append(label)

    def is_selected(self):
        """
        Returns true if this radio button is selected.
        """
        return self._impl.is_selected()


class Window(GUIElement):
    """
    Lets you identify individual windows of the currently open browser session.
    """

    def __init__(self, title=None):
        super(Window, self).__init__()
        self._args.append(title)

    @property
    def title(self):
        """
        Returns the title of this Window.
        """
        return self._impl.title

    @property
    def handle(self):
        """
        Returns the Selenium driver window handle assigned to this window. Note
        that this window handle is simply an abstract identifier and bears no
        relationship to the corresponding operating system handle (HWND on
        Windows).
        """
        return self._impl.handle

    def __repr__(self):
        if self._is_bound():
            return self._repr_constructor_args([self.title])
        else:
            return super(Window, self).__repr__()


class Alert(GUIElement):
    """
    Lets you identify and interact with JavaScript alert boxes.
    """

    def __init__(self, search_text=None):
        super(Alert, self).__init__()
        self._args.append(search_text)

    @property
    def text(self):
        """
        The text displayed in the alert box.
        """
        return self._impl.text

    def accept(self):
        """
        Accepts this alert. This typically corresponds to clicking the "OK"
        button inside the alert. The typical way to use this method is::

                >>> Alert().accept()

        This accepts the currently open alert.
        """
        self._impl.accept()

    def dismiss(self):
        """
        Dismisses this alert. This typically corresponds to clicking the
        "Cancel" or "Close" button of the alert. The typical way to use this
        method is::

                >>> Alert().dismiss()

        This dismisses the currently open alert.
        """
        self._impl.dismiss()

    def __repr__(self):
        if self._is_bound():
            return self._repr_constructor_args([self.text])
        else:
            return super(Alert, self).__repr__()


# todo - convert to dataclass
class Point(namedtuple("Point", ["x", "y"])):
    """
    A clickable point. To create a ``Point`` at an offset of an existing point,
    use ``+`` and ``-``::

            >>> point = Point(x=10, y=25)
            >>> point + (10, 0)
            Point(x=20, y=25)
            >>> point - (0, 10)
            Point(x=10, y=15)
    """

    def __new__(cls, x=0, y=0):
        return cls.__bases__[0].__new__(cls, x, y)

    def __init__(self, x=0, y=0):
        # tuple is immutable so we can't do anything here. The initialization
        # happens in __new__(...) above.
        pass

    @property
    def x(self):
        """
        The x coordinate of the point.
        """
        return self[0]

    @property
    def y(self):
        """
        The y coordinate of the point.
        """
        return self[1]

    def __eq__(self, other):
        return (self.x, self.y) == other

    def __ne__(self, other):
        return self != other

    def __hash__(self):
        return self.x + 7 * self.y

    def __add__(self, delta):
        dx, dy = delta
        return Point(self.x + dx, self.y + dy)

    def __radd__(self, delta):
        return self.__add__(delta)

    def __sub__(self, delta):
        dx, dy = delta
        return Point(self.x - dx, self.y - dy)

    def __rsub__(self, delta):
        x, y = delta
        return Point(x - self.x, y - self.y)
