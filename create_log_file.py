"""
This file contain the method to create log file of a programm
"""
import logging
import os


def createLogFile(file_name, level):
    """ Method to create a log file

    :param file_name: name of log file
    :type file_name: str
    :param level: level of logger
    :type level: logging.(debug, info, warning, error or critical)"""
    if not os.path.isfile(file_name):
        logger = logging.getLogger()
        logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh = logging.FileHandler(file_name, 'a')
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
