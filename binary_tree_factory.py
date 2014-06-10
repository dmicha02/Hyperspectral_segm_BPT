from region_graph import initRegionGraphe
import logging
import numpy as np


class BinaryTreeFactory:
    @staticmethod
    def getFromImage(image, criterion, type_img):
        """Method to partition image using binary partition tree

        :param image: image to partition
        :type image: image
        :param criterion: stop criterion
        :type criterion: int
        :param type_img: type of image 'L' for Grayscale 'RGB' for color
        :type type_img: str
        :return: the binary tree
        :rtype: list"""
        try:
			logging.info("** in getFromGrayscaleImage():")
			g = initRegionGraphe(image, type_img)
			#logging.debug("Nodes: " + str([n.mean_reg(type_img) for n in g.node_list]))
			(node1, node2) = g.initDictRegions()
			g.merge(node1, node2)
			temp = 0
			while(len(g.node_list) > 1):
				temp = temp + 1
				#logging.debug("Iteration " + str(temp))
				node1, node2 = g.regionToMerge()
				if abs(np.mean(node1.mean_reg(type_img)) - np.mean(node2.mean_reg(type_img))) < criterion:
					#logging.debug("test pass: dmin=" + str(abs(node1.mean_reg(type_img) - node2.mean_reg(type_img))) + " < stop criterion")
					g.merge(node1, node2)
					#logging.debug("Nodes: " + str([n.mean_reg(type_img) for n in g.node_list]))
				else:
					#logging.debug("test fail: dmin=" + str(abs(node1.mean_reg(type_img) - node2.mean_reg(type_img))) + " > stop criterion")
					break
			tree = g.node_list
			logging.info(" \t \tSuccess")
			return tree
        except:
            logging.error(" \t \tError in getFromGrayscaleImage()")
            print "Error in getFromGrayscaleImage()"
