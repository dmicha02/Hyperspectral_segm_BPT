from region_graph import initRegionGraphe
import logging


class BinaryTreeFactory:
    @staticmethod
    def getFromGrayscaleImage(image, criterion):
        try:
            logging.info("** in getFromGrayscaleImage():")
            g = initRegionGraphe(image)
            #logging.debug("Nodes: " + str([n.val for n in g.node_list]))
            (node1, node2) = g.initDictRegions()
            g.merge(node1, node2)
            temp = 0
            while(len(g.node_list) > 1):
                temp = temp + 1
                #logging.debug("Iteration " + str(temp))
                node1, node2 = g.regionToMerge()
                if abs(node1.val - node2.val) < criterion:
                    #logging.debug("test pass: dmin=" + str(abs(node1.val - node2.val)) + " < stop criterion")
                    g.merge(node1, node2)
                    #logging.debug("Nodes: " + str([n.val for n in g.node_list]))
                else:
                    #logging.debug("test fail: dmin=" + str(abs(node1.val - node2.val)) + " > stop criterion")
                    break
            tree = g.node_list
            logging.info(" \t \tSuccess")
            return tree
        except:
            logging.error(" \t \tError in getFromGrayscaleImage()")
            print "Error in getFromGrayscaleImage()"
