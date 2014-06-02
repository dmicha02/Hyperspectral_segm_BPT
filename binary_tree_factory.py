"""File of partition process"""
from region_graph import initRegionGraphe
from PIL import Image, ImageDraw
import numpy as np
import logging


class BinaryTreeFactory(object):
    """Class to partition images with binary partition tree"""

    def __init__(self):
        pass

    @staticmethod
    def getFromImage(image, criterion):
        """Method to partition a grayscale image

        :param image: image
        :type image: image
        :param criterion: criterion of merging
        :type criterion: int
        :return: the tree after merging
        :rtype: list"""
        logging.info("partition image with Binary Partition Tree, criterion: " + str(criterion))
        #initialization
        g = initRegionGraphe(image)
        temp = 0
        #dico_lst = g.InitDistanceDict()
        while len(g.region_list) > 1:
            temp = temp + 1
            logging.debug("iteration number " + str(temp))
            #dico_lst = g.InitDistanceDict()
            #dicomin = g.FindDistanceMin(dico_lst)
            l = g.initDistance()
            dicomin = g.findDistanceMin(l)
            #d = dicomin["val"]
            d = dicomin[2]
            # merge criterion : minimal distance
            logging.info("test criterion")
            if d < criterion:
                logging.debug("test pass (" + str(d) + "<" + str(criterion) + ")")
                # the two nodes to merge
                #region1 = dicomin["r1"]
                #region2 = dicomin["r2"]
                region1 = dicomin[0]
                region2 = dicomin[1]
                # merge
                new_region = g.mergeRegions(region1, region2, temp)
                # update
                g.updateNeighbours(region1, region2, new_region)
                g.updateGraph(region1, region2, new_region)
                logging.debug("node value in graph : " + str([node.val for node in g.region_list]))
                #g.UpdateDistanceDict(dico_lst, dicomin, new_region)
            else:
                logging.debug("test fail(" + str(d) + ">" + str(criterion) + ")")
                break
        logging.info("return tree")
        tree = g.region_list
        return tree

    def DisplayForGrayscaleImage(self, tree, line, column, merge_order, M):
        """Display of a merge order for grayscale image

        :param tree: final tree (after partition)
        :type tree: RegionGraph
        :param line: number of line on the image
        :type line: int
        :param column: number of column on the image
        :type column: int
        :param merge_order: merge order choosen by user
        :type merge_order: int
        :param M: array of the image
        :type M: array"""

        from region_graph import Group
        node_order = tree.merge_order
        child = [tree.childright, tree.childleft]
        zone = []
        if node_order == merge_order:
            val_region = tree.val
            for px in tree.pixel_list:
                M[px.x][px.y] = val_region
                zone = zone + [(px.y, px.x)]
            M = np.reshape(M, (1, line * column))
            IMG = Image.new('L', (line, column))
            IMG.putdata(M[0])
            IMG_demo = IMG.convert('RGB')
            draw = ImageDraw.Draw(IMG_demo)
            for z in zone:
                draw.point(z, "red")
            IMG_demo.show()
        else:
            for c in child:
                if isinstance(c, Group):
                    self.DisplayForGrayscaleImage(c, line, column, merge_order, M)

    def FinalGrayscaleImagePartition(self, tree, img):
        """Method to show final regions after partition

        :param img: base image
        :type img: image
        :param tree: tree of partition
        :type tree: RegionGraph"""
        logging.info("show final partition")
        from region_graph import Group
        lig, col = np.size(img)
        M = list(img.getdata())
        M = np.reshape(M, (lig, col))
        for r in tree:
            if isinstance(r, Group):
                BinaryTreeFactory().DisplayForGrayscaleImage(r, lig, col, r.merge_order, M)

    def DisplayResultImage(self, tree, img):
        """Method to show the result image

        :param tree: tree of partition
        :type tree: RegionGraph
        :param img: base image
        :type image: image"""
        logging.info("show result")
        line, column = img.size
        M = [0 for i in range(0, line * column)]
        M = np.reshape(M, (line, column))
        #M = np.reshape(M, (line, column, len(M[0])))
        for t in tree:
            for px in t.pixel_list:
                M[px.x][px.y] = t.val
        if isinstance(M[0][0], int):
            M = np.reshape(M, (1, line * column))
            IMG = Image.new('L', (line, column))
            IMG.putdata(M[0])
        else:
            M1 = np.reshape(M, (1, line * column * len(M[0][0])))
            M = []
            for i in range(0, line * column * 3, 3):
                M = M + [tuple(M1[0][i:i+3])]
            IMG = Image.new('RGB', (line, column))
            IMG.putdata(M)
        IMG.show()
