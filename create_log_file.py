# -*- coding: utf-8 -*-
"""
Created on Wed May 28 14:28:47 2014
"""
import logging

def createLogFile(file_name):
    """ Method to create a log file

    :param file_name: name of log file
    :type file_name: str"""

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(file_name, 'a')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
