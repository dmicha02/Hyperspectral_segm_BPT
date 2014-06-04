# -*- coding: utf-8 -*-
"""
Function to enable or disable logging for debug
"""


def enableDebug(param):
    """Function to enable or disable logging for debug

    :param param: 1 to enable the debug logging
    :type param: int"""
    if param == 1:
        f = file("binary_tree_factory.py", "r+")
        chaine = "logging.debug"
        for line in file("binary_tree_factory.py", "r"):
            if chaine in line:
                f.write(line.replace("#", ""))
            else:
                f.write(line)
        f.close()

    else:
        f = file("binary_tree_factory.py", "r+")
        chaine = "logging.debug"
        chaine2 = "#logging.debug"
        for line in file("binary_tree_factory.py", "r"):
            if (chaine in line) and (chaine2 not in line):
                f.write(line.replace("logging.debug", "#logging.debug"))
            else:
                f.write(line)
        f.close()
