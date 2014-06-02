"""File with class RegionGraph, Region, Group, Pixel, ... """
import numpy as np
from mean_merge_strategy import MeanMergeStrategy
import logging


class RegionGraph(object):
    """Class that implements the neighbouring graph of regions

    :param merge_strategy: the merge strategy choose by user
    :type merge_strategy: MergeStrategy"""

    def __init__(self, merge_strategy):
        self.merge_strategy = merge_strategy
        self.region_list = []

    def addRegion(self, r):
        """Method for add a region in the list

        :param r: region to add to region_list
        :type r: Region"""
        self.region_list.append(r)

    def mergeRegions(self, r1, r2, temp):
        """Method for merge two regions

        :param r1: first node to merge
        :type r1: AbstractNode
        :param r2: second node to merge
        :type r2: AbstractNode
        :param temp: it serves to define the merge order of new node
        :type temp: int
        :return: the new node after merge
        :rtype: Group"""
        logging.info("merge two regions")
        r3 = self.merge_strategy.merge(r1, r2, temp)
        return r3

    def initDistance(self):
        """Method to initialize a list of distance between two pixels
        in neighborhood and save result in tuple

        :return: list of tuple where the two first arguments are two AbstractNode and the third is distance
        :rtype: list"""
        logging.info("init / update distance list")
        l = []
        for region in self.region_list:
            for neighbour in region.neighbours:
                l.append(tuple([region, neighbour, abs(region.val - neighbour.val)]))
        return l

    def findDistanceMin(self, distance_list):
        """Method to find the couple of pixels which have the minimal distance and this distance

        :param distance_list: list tuple provide by initDistance() method
        :type distance_list: list
        :return: the minimal tuple
        :rtype: tuple"""

        logging.info("find the minimal criterion")
        dmin = float("inf")
        for element in distance_list:
            if element[2] < dmin:
                dmin = element[2]
                tuple_min = element
            else:
                dmin = dmin
                tuple_min = tuple_min
        return tuple_min

#    def InitDistanceDict(self):
#        """Method to initialize the list of dictionnary
#        including the two neighbours with the minimal distance
#
#        :return: list of dict
#        :rtype: list"""
#        list_dict = []
#        dico_2 = {"r1": None, "neighbours": []}
#        dico = {"r2": None, "val": None}
#        for node in self.region_list:
#            dico_2 = {"r1": None, "neighbours": []}
#
#            dico_2["r1"] = node
#            for neighbour in node.neighbours:
#                dico = {"r2": None, "val": None}
#                dico["r2"] = neighbour
#                dico["val"] = abs(neighbour.val - node.val)
#                dico_2["neighbours"].append(dico)
#            list_dict.append(dico_2)
#        return list_dict

#    def FindDistanceMin(self, dict_list):
#        """Method to find the two region with the smaller distance
#
#        :param dict_list: the list of dict
#        :type dict_list: list
#        :return: dict with the two regions and the distance
#        :rtype: dict"""
#        dmin = float("inf")
#        dico_min = None
#        for r1 in dict_list:
#            for r2 in r1["neighbours"]:
#                if abs(r1["r1"].val - r2["r2"].val) < dmin:
#                    dmin = abs(r1["r1"].val - r2["r2"].val)
#                    dico_min = {"r1": r1["r1"], "r2": r2["r2"], "val": dmin}
#                else:
#                    dmin = dmin
#                    dico_min = dico_min
#        return dico_min

#    def UpdateDistanceDict(self, dico_list, dict_min, new_region):
#        """Method to update the list of dictionnary
#        including the two neighbours with the minimal distance
#
#        :return: list of dict
#        :rtype: list"""
#        for dico in dico_list:
#            if dico["r1"] != dict_min["r1"] and dico["r1"] != dict_min["r2"]:
#                for neighbour in dico["neighbours"]:
#                    if neighbour["r2"] == dict_min["r1"] or neighbour["r2"] == dict_min["r2"]:
#                        neighbour["r2"] = new_region
#                        neighbour["val"] = abs(new_region.val - dico["r1"].val)
#                    else:
#                        neighbour = neighbour
#        for dico in dico_list:
#            if dico["r1"] == dict_min["r1"] or dico["r1"] == dict_min["r2"]:
#                dico_list.remove(dico)
#        temp = []
#        for n in new_region.neighbours:
#            temp.append({"val": abs(new_region.val - n.val), "r2": n})
#        dico_list.append({"r1": new_region, "neighbours": temp})

    def initRegionList(self, pixel, line, column):
        """Method to initialize the region list

        :param pixel: list of pixels
        :type pixel: Pixel
        :param line: number of ligne on image
        :type line: int
        :param column: number of column on image
        :type column: int"""
        for i in range(0, line):
            for j in range(0, column):
                self.addRegion(Region([pixel[i][j]], pixel[i][j].spectrum))

    def initNeighboursRegionList(self, line, column):
        """Method to initialize the neighbours

        :param line: number of ligne on image
        :type line: int
        :param column: number of column on image
        :type column: int"""
        for i in range(0, line):
            for j in range(0, column):

                if i == 0 and j == 0:
                    self.region_list[i][j].addNeighbours(self.region_list[i][j+1])
                    self.region_list[i][j].addNeighbours(self.region_list[i+1][j])

                elif i == 0 and j == column-1:
                    self.region_list[i][j].addNeighbours(self.region_list[i][j-1])
                    self.region_list[i][j].addNeighbours(self.region_list[i+1][j])

                elif i == line-1 and j == 0:
                    self.region_list[i][j].addNeighbours(self.region_list[i][j+1])
                    self.region_list[i][j].addNeighbours(self.region_list[i-1][j])

                elif i == line-1 and j == column-1:
                    self.region_list[i][j].addNeighbours(self.region_list[i][j-1])
                    self.region_list[i][j].addNeighbours(self.region_list[i-1][j])

                elif i == 0 and (j != 0 and j != column-1):
                    self.region_list[i][j].addNeighbours(self.region_list[i+1][j])
                    self.region_list[i][j].addNeighbours(self.region_list[i][j-1])
                    self.region_list[i][j].addNeighbours(self.region_list[i][j+1])

                elif i == line-1 and (j != 0 and j != column-1):
                    self.region_list[i][j].addNeighbours(self.region_list[i-1][j])
                    self.region_list[i][j].addNeighbours(self.region_list[i][j-1])
                    self.region_list[i][j].addNeighbours(self.region_list[i][j+1])

                elif j == 0 and (i != 0 and i != line-1):
                    self.region_list[i][j].addNeighbours(self.region_list[i-1][j])
                    self.region_list[i][j].addNeighbours(self.region_list[i+1][j])
                    self.region_list[i][j].addNeighbours(self.region_list[i][j+1])

                elif j == column-1 and (i != 0 and i != line-1):
                    self.region_list[i][j].addNeighbours(self.region_list[i-1][j])
                    self.region_list[i][j].addNeighbours(self.region_list[i+1][j])
                    self.region_list[i][j].addNeighbours(self.region_list[i][j-1])

                else:
                    self.region_list[i][j].addNeighbours(self.region_list[i-1][j])
                    self.region_list[i][j].addNeighbours(self.region_list[i+1][j])
                    self.region_list[i][j].addNeighbours(self.region_list[i][j+1])
                    self.region_list[i][j].addNeighbours(self.region_list[i][j-1])

    def updateGraph(self, region_to_del1, region_to_del2, region_to_add):
        """method to update Graph after merging

        :param region_to_del1: first region to del in list of regions
        :type region_to_del1: AbstractNode
        :param region_to_del2: second region to del in list of regions
        :type region_to_del2: AbstractNode
        :param region_to_add: region to add in list of regions
        :type region_to_add: AbstractNode"""
        logging.info("update Graph")
        self.addRegion(region_to_add)
        self.region_list.remove(region_to_del1)
        self.region_list.remove(region_to_del2)

    def updateNeighbours(self, region_to_del1, region_to_del2, region_to_add):
        """method to update region's neighbours after merging

        :param region_to_del1: first region to del in list of neighbours
        :type region_to_del1: AbstractNode
        :param region_to_del2: second region to del in list of neighbours
        :type region_to_del2: AbstractNode
        :param region_to_add: region to add in list of neighbours
        :type region_to_add: AbstractNode"""
        logging.info("update neighbours")
        for node in self.region_list:
            if region_to_del1 in node.neighbours or region_to_del2 in node.neighbours:
                node.neighbours.discard(region_to_del1)
                node.neighbours.discard(region_to_del2)
                node.neighbours.add(region_to_add)


class AbstractNode(object):
    """Parent class of Region and Group"""
    def __init__(self):
        pass


class Region(AbstractNode):
    """Class that represents a region of the image

    :param pixel_list: list of pixel(s)
    :type pixel_list: list
    :param value: region value
    :type value: int or tuple"""

    def __init__(self, pixel_list, value):
        self.pixel_list = pixel_list
        self.neighbours = set()
        self.val = value

    def addNeighbours(self, r):
        """Method to add a neighbour

        :param r: neighbour to add
        :type r: AbstractNode"""
        self.neighbours.add(r)


class Group(AbstractNode):
    """Class that implements the binary tree structure

    :param value: node value
    :type value: int or tuple"""

    def __init__(self, value):
        self.pixel_list = None
        self.childright = None
        self.childleft = None
        self.merge_order = None
        self.val = value
        self.neighbours = set()


class PixelList(list):
    """Represents a pixel list """

    def __init__(self):
        pass

    def initList(self, data, line, column):
        """Method to initialize the pixel list

        :return: pixel array of image for initialization
        :rtype: array"""
        px = []
        if isinstance(data[0][0], int):
            for i in range(0, line):
                for j in range(0, column):
                    px.append(Pixel(i, j, data[i][j]))
        else:
            for i in range(0, line):
                for j in range(0, column):
                    px.append(Pixel(i, j, tuple(data[i][j])))
        return np.reshape(px, (line, column))


class Pixel(object):
    """Represents a pixel with 2 space coordinates and the spectrum

    :param x: line coordinate
    :type x: int
    :param y: column coordinate
    :type y: int
    :param spectrum: pixel spectrum
    :type spectrum: int or tuple"""

    def __init__(self, x, y, spectrum):
        self.x = x
        self.y = y
        self.spectrum = spectrum


def initRegionGraphe(img):
    """ Function to assign each pixel to a region
    it returns a list of all regions (pixels)

    :param img: image to merge
    :type img: image
    :return: the initialization graphe
    :rtype: RegionGraph"""
    logging.info("initialization")
    lig, col = img.size   # lig: number of lines col: number of columns
    data = list(img.getdata())
    if isinstance(data[0], int) == 1:
        data = np.reshape(data, (lig, col))
    elif isinstance(data[0], tuple) == 1:
        data = np.reshape(data, (lig, col, len(data[0])))

    graphe = RegionGraph(MeanMergeStrategy())

    px = PixelList().initList(data, lig, col)   # pixels of image

    graphe.initRegionList(px, lig, col)
    graphe.region_list = np.reshape(graphe.region_list, (lig, col))   # regions list

    #neighbours assignement
    graphe.initNeighboursRegionList(lig, col)

    #reshaping
    graphe.region_list = np.reshape(graphe.region_list, (1, lig * col))
    graphe.region_list = list(graphe.region_list[0])

    return graphe
