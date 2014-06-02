"""
Main programm to partition image using binary partition tree
"""
import logging
import os
import time
import sys
sys.path.append('F:\M1\Projet_Images_Hyperspectral\code')
from PIL import Image
from binary_tree_factory import BinaryTreeFactory
from create_log_file import createLogFile
from sphinx_doc import genere_doc

#create the log file
LOG_FILE = "binary_tree_factory.log"
if not os.path.isfile(LOG_FILE):
    createLogFile(LOG_FILE)

#begin of program
logging.info("-------------------started program--------------------")
begin = time.clock()

# load image
logging.info("load image")
img_file = "test_ndg.png"
IMG = Image.open("data/" + img_file)
logging.debug("image : " + img_file)

# partition image with Binary Partition Tree
T = BinaryTreeFactory.getFromImage(IMG, 80)

# result of partition of simple grayscale image
BinaryTreeFactory().FinalGrayscaleImagePartition(T, IMG)
BinaryTreeFactory().DisplayResultImage(T, IMG)

# create auto-documentation using Sphinx
logging.info("create documentation Sphinx")
genere_doc()

<<<<<<< HEAD
end = time.clock()
time = end - begin
logging.info("end of program (execution time: " + str(time) + " s)")
>>>>>>> c4292f3213f84baa5b009358e82143530d1a2e69
