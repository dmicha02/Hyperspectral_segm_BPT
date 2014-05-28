"""
Main programm
"""
import sys
sys.path.append('F:\M1\Projet_Images_Hyperspectral\code')
from PIL import Image
from binary_tree_factory import BinaryTreeFactory
#import sphinx
#import sphinx.quickstart
#import sphinx.apidoc
import logging
import os
from create_log_file import createLogFile
# test modification pour git hub
#create the log file
if not os.path.isfile("binary_tree_factory.log"):
    createLogFile("binary_tree_factory.log")

#begin of program
logging.info("-------------------started program--------------------")
# load image
logging.info("load image")
img_file = "test_ndg.png"
IMG = Image.open("data/" + img_file)
logging.debug("image : " + img_file)

# partition image with Binary Partition Tree
T = BinaryTreeFactory.getFromImage(IMG, 80)

# result of partition of simple grayscale image
#BinaryTreeFactory().FinalGrayscaleImagePartition(T, IMG)
BinaryTreeFactory().DisplayResultImage(T, IMG)

# create auto-documentation using Sphinx
#logging.info("create documentation Sphinx")
#def configure_doc():
#    sphinx.quickstart.main(['sphinx-quickstart'])
#def genere_doc():
#    sphinx.apidoc.main(['sphinx-apidoc','-f','--output-dir=doc/generated','./'])
#    sphinx.main(['sphinx-build','-b','html','doc','doc/_build/html'])
#genere_doc()

logging.info("end of program")
