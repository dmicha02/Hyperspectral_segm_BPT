"""
File contain the different strategies to merge nodes
"""
from merge_strategy import MergeStrategy
import logging


class MeanMergeStrategy(MergeStrategy):
    """Example of merging strategy : average distance between two nodes"""

    def __init__(self, type_img):
        self.type_img = type_img

    def score(self, r1, r2):
        """Method to calculate the distance between two nodes

        :param r1: First node
        :type r1: AbstractNode
        :param r2: Second node
        :type r2: AbstractNode
        :return: Distance between r1 and r2
        :rtype: int"""
        try:
            v1 = r1.mean_reg(self.type_img)
            v2 = r2.mean_reg(self.type_img)
            if self.type_img == 'L':
                val = abs(v1-v2)
            else:
                val=[]
                for i in range(len(v1)):
                    val.append(v1[i]-v2[i])
            return val
        except:
            logging.error(" \t \tError in MeanMergeStrategy().score()")
            print "Error in MeanMergeStrategy().score()"

    def mini(self, edge):
        """Method to return the two nodes which have the smallest distance

        :param edge: Dictionnary which contains the couples node of the image
        :type edge: dict
        :return: the two nodes with minimal distance
        :rtype: AbstractNodes"""
        try:
            if self.type_img == 'L':
                dmin = float("inf")
                for cle, valeur in edge.items():
                    if (valeur < dmin):
                        dmin = valeur
                        (r1, r2) = cle
            else:
                dmin = float("inf")
                for cle, valeur in edge.items():
                    if sum(valeur) < dmin:
                        dmin = sum(valeur)
                        (r1, r2) = cle
            return r1, r2
        except:
            logging.error(" \t \tError in MeanMergeStrategy().mini()")
            print "Error in MeanMergeStrategy().mini()"
