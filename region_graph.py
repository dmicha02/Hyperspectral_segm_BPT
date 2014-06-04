"""
File with class to represent pixels, nodes, graph and associated methods
"""
import numpy as np
import logging
from mean_merge_strategy import MeanMergeStrategy


class RegionGraph(object):
    """Class that implements the graph of nodes

    :param merge_strategy: the merge strategy choose by user
    :type merge_strategy: MergeStrategy"""
    def __init__(self, merge_strategy):
        self.merge_strategy = merge_strategy
        self.node_list = []
        self.edge = dict()

    def initDictRegions(self):
        """Initialization of a dictionnary which contains the nodes couple
        and the distance between the two nodes

        :return: the two regions with minimal distance
        :rtype: AbstractNodes"""
        try:
            for i in self.node_list:
                for j in i.neighbours:
                    if (j, i) not in self.edge:
                        self.edge[i, j] = self.merge_strategy.score(i, j)
            return self.regionToMerge()
        except:
            logging.error(" \t \tError in RegionGraph.initDictRegions()")
            print "Error in RegionGraph.initDictRegions()"

    def update(self, node1, node2, node3):
        """Method to delete the edges between node1 and node2
        and replace by the new edges with node3

        :param node1: First node to merge
        :type node1: AbstractNode
        :param node2: Second node to merge
        :type node2: AbstractNode
        :param node3: New node after merging
        :type node3: AbstractNode
        :return: dictionnary of nodes couple
        :rtype: dict"""
        try:
            for i in node2.neighbours:
                if (node2, i) in self.edge:
                    del self.edge[node2, i]
                elif(i, node2) in self.edge:
                    del self.edge[i, node2]
            for i in node1.neighbours:
                if (node1, i) in self.edge:
                    del self.edge[node1, i]
                elif(i, node1) in self.edge:
                    del self.edge[i, node1]
            for i in node3.neighbours:
                self.edge[node3, i] = self.merge_strategy.score(node3, i)
            return self.edge
        except:
            logging.error(" \t \tError in RegionGraph.update()")
            print "Error in RegionGraph.update()"

    def regionToMerge(self):
        """Method to find the two nodes to merge

        :return: the two regions to merge
        :rtype: AbstractNodes"""
        try:
            (r1, r2) = self.merge_strategy.mini(self.edge)
            return r1, r2
        except:
            logging.error(" \t \tError in RegionGraph.regionToMerge()")
            print "Error in RegionGraph.regionToMerge()"

    def merge(self, node1, node2):
        """This function merges two nodes together.

        :param node1: The first node to merge
        :type node1: AbstractNode
        :param node2: The second node to merge
        :type node2: AbstractNode"""
        try:
            node3 = Group()
            node3.child1 = node1
            node3.child2 = node2
            node3.neighbours = node1.neighbours.union(node2.neighbours)
            node3.neighbours.discard(node1)
            node3.neighbours.discard(node2)
            node3.pixel_list = node1.pixel_list.union(node2.pixel_list)
            node3.val = self.merge_strategy.newValue(node1, node2)
            node3.order = max(node2.order, node1.order) + 1

            # Update neighbours in other groups
            self.update(node1, node2, node3)
            self.node_list.remove(node1)
            self.node_list.remove(node2)

            for node in self.node_list:
                if node1 in node.neighbours or node2 in node.neighbours:
                    node.neighbours.discard(node1)
                    node.neighbours.discard(node2)
                    node.neighbours.add(node3)

            # Add new node to list of nodes
            self.node_list.append(node3)
        except:
            logging.error(" \t \tError in RegionGraph.merge()")
            print "Error in RegionGraph.merge()"

    def initRegionList(self, line, column, data):
        """Method to initialize the graph

        :param line: number of lines in image
        :type line: int
        :param column: number of columns in image
        :type column: int
        :param data: array represent pixels in image
        :type data: array
        :return: list of regions
        :rtype: list"""
        try:
            reg = []
            for i in range(0, line):
                for j in range(0, column):
                    reg.append(Region(Pixel(i, j, data[i][j])))
            return reg
        except:
            logging.error(" \t \tError in RegionGraph.initRegionList()")
            print "Error in RegionGraph.initRegionList()"

    def initNeighboursRegionList(self, reg, line, column):
        """Method to initialize the neighbours

        :param reg: array of regions
        :type reg: array
        :param line: number of ligne on image
        :type line: int
        :param column: number of column on image
        :type column: int"""
        try:
            for i in range(0, line):
                for j in range(0, column):

                    if (i == 0 and j == 0):
                        reg[i][j].addNeighbour(reg[i][j+1])
                        reg[i][j].addNeighbour(reg[i+1][j])

                    elif (i == 0 and j == column - 1):
                        reg[i][j].addNeighbour(reg[i][j-1])
                        reg[i][j].addNeighbour(reg[i+1][j])

                    elif (i == line - 1 and j == 0):
                        reg[i][j].addNeighbour(reg[i][j+1])
                        reg[i][j].addNeighbour(reg[i-1][j])

                    elif (i == line - 1 and j == column - 1):
                        reg[i][j].addNeighbour(reg[i][j-1])
                        reg[i][j].addNeighbour(reg[i-1][j])

                    elif (i == 0 and (j != 0 and j != column - 1)):
                        reg[i][j].addNeighbour(reg[i+1][j])
                        reg[i][j].addNeighbour(reg[i][j-1])
                        reg[i][j].addNeighbour(reg[i][j+1])

                    elif (i == line - 1 and (j != 0 and j != column - 1)):
                        reg[i][j].addNeighbour(reg[i-1][j])
                        reg[i][j].addNeighbour(reg[i][j-1])
                        reg[i][j].addNeighbour(reg[i][j+1])

                    elif (j == 0 and (i != 0 and i != line - 1)):
                        reg[i][j].addNeighbour(reg[i-1][j])
                        reg[i][j].addNeighbour(reg[i+1][j])
                        reg[i][j].addNeighbour(reg[i][j+1])

                    elif (j == column - 1 and i != 0 and i != line - 1):
                        reg[i][j].addNeighbour(reg[i-1][j])
                        reg[i][j].addNeighbour(reg[i+1][j])
                        reg[i][j].addNeighbour(reg[i][j-1])

                    else:
                        reg[i][j].addNeighbour(reg[i-1][j])
                        reg[i][j].addNeighbour(reg[i+1][j])
                        reg[i][j].addNeighbour(reg[i][j+1])
                        reg[i][j].addNeighbour(reg[i][j-1])
        except:
            logging.error(" \t \tError in RegionGraph.initNeighboursRegionList()")
            print "Error in RegionGraph.initNeighboursRegionList()"


class AbstractNode(object):
    """Parent class of Region and Group"""
    order = 0


class Region(AbstractNode):
    """Class that represents a region of the image

    :param pixel: a pixel
    :type pixel: Pixel"""
    def __init__(self, pixel):
        self.pixel = pixel
        self.neighbours = set()
        self.pixel_list = set()
        self.pixel_list.add(pixel)
        self.val = pixel.spectrum

    def addNeighbour(self, r):
            self.neighbours.add(r)


class Group(AbstractNode):
    """Class that implements the binary tree structure"""
    def __init__(self):
        self.pixel_list = set()
        self.child1 = None
        self.child2 = None
        self.merge_order = None
        self.neighbours = set()
        self.val = None


class Pixel:
    """Represents a pixel with 2 space coordinates and the spectrum

    :param x: x coordinate of pixel
    :type x: int
    :param y: y coordinate of pixel
    :type y: int
    :param spectrum: spectrum of pixel
    :type spectrum: int or tuple"""
    def __init__(self, x, y, spectrum):
        self.x = x
        self.y = y
        self.spectrum = spectrum


def initRegionGraphe(img):
    """ Function to initialize a list of regions and all arguments of Regions

    :param img: image to partition
    :type img: image
    :return: list of all regions in image
    :rtype: list"""
    try:
        line, column = img.size
        data = list(img.getdata())
        data = np.reshape(data, (line, column))
        Graphe = RegionGraph(MeanMergeStrategy())
        region_list = Graphe.initRegionList(line, column, data)
        Graphe.node_list = region_list
        region_list = np.reshape(region_list, (line, column))
        Graphe.initNeighboursRegionList(region_list, line, column)
        return Graphe
    except:
            logging.error(" \t \tError in initRegionGraphe()")
            print "Error in initRegionGraphe()"
