# -*- coding: utf-8 -*-
from os import chmod
from os import stat
from stat import S_IEXEC


def make_executable(file_path):
    chmod(file_path, stat(file_path).st_mode | S_IEXEC)
