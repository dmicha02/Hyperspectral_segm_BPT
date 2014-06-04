"""
File contain the different strategies to merge nodes
"""
from merge_strategy import MergeStrategy
import logging


class MeanMergeStrategy(MergeStrategy):
    """Example of merging strategy : average distance between two nodes"""

    def __init__(self):
        pass

    def score(self, r1, r2):
        """Method to calcul the distance between two nodes

        :param r1: First node
        :type r1: AbstractNode
        :param r2: Second node
        :type r2: AbstractNode
        :return: Distance between r1 and r2
        :rtype: int"""
        try:
            return abs(r1.val - r2.val)
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
            dmin = float('inf')
            for cle, valeur in edge.items():
                if valeur < dmin:
                    dmin = valeur
                    (r1, r2) = cle
            return r1, r2
        except:
            logging.error(" \t \tError in MeanMergeStrategy().mini()")
            print "Error in MeanMergeStrategy().mini()"

    def newValue(self, node1, node2):
        """Method to calcul the new value of new node after merging

        :param node1: The first node to merge
        :type node1: AbstractNode
        :param node2: The second node to merge
        :type node2: AbstractNode
        :return: New value for new node
        :rtype: int"""
        try:
            return (node1.val + node2.val) / 2
        except:
            logging.error(" \t \tError in MeanMergeStrategy().newValue()")
            print "Error in MeanMergeStrategy().newValue()"
