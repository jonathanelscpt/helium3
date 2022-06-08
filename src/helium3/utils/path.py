# -*- coding: utf-8 -*-
import pathlib
from os.path import split


def get_components(path):
    folders = []
    while True:
        path, folder = split(path)
        if folder != "":
            folders.append(folder)
        else:
            if path != "":
                folders.append(path)
            break
    return list(reversed(folders))


def ensure_exists(path):
    """
    https://stackoverflow.com/a/600612/190597 (tzot)
    """
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
