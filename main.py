"""
Main program : partition images using binary partition tree
"""
import logging
import time
from PIL import Image
from binary_tree_factory import BinaryTreeFactory
from plot_img import plotImage, showFinalsRegions
from create_log_file import createLogFile
from enable_debug import enableDebug
from sphinx_doc import genere_doc

# Create the log file, if you don't want log file, comment the 2 lines under
LOG_FILE = "binary_tree_factory.log"
enableDebug(0)
createLogFile(LOG_FILE, logging.debug)

# Begin of program
begin = time.clock()
logging.info("--------Beginning of program--------")

# Load image
FILE = "lena64.png"
IM = Image.open("data/" + FILE)
logging.info("Load Image")
TYPE_IM = 'L'   # type of image
SIZE = IM.size   # image size
CRITERION = 50   # stop criterion
logging.info("Stop Criterion: " + str(CRITERION))
# Partition image using binary partition tree
TREE = BinaryTreeFactory.getFromImage(IM, CRITERION, TYPE_IM)

# Results
plotImage(TREE, SIZE, TYPE_IM)
#showFinalsRegions(TREE, SIZE, TYPE_IM, "standard")

# Create auto-documentation using Sphinx
#genere_doc()

# End of program
end = time.clock()
time = end - begin
logging.info("End of program (execution time: " + str(time) + "s )")
