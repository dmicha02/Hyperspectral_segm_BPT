"""
File for type of merge strategy
"""
from merge_strategy import MergeStrategy


class MeanMergeStrategy(MergeStrategy):
    """Example of merging strategy  with average distance criterion"""

    def __init__(self):
        pass

    def merge(self, r1, r2, merge_order):
        """Function to merge two nodes together

        :param r1: the first node to merge
        :type name: AbstractNode
        :param r2: the second node to merge
        :type name: AbstractNode
        :param merge_order: the merge order of new node
        :return: the new node
        :rtype: Group"""
        from region_graph import Group

        if isinstance(r1.pixel_list[0].spectrum, int):
            new_region = Group((r1.val + r2.val) / 2)
            new_region.neighbours = (r1.neighbours).union(r2.neighbours)
            new_region.neighbours.discard(r1)
            new_region.neighbours.discard(r2)
            ensemble_pixel = set(r1.pixel_list).union(set(r2.pixel_list))
            new_region.pixel_list = list(ensemble_pixel)
            new_region.childleft = r1
            new_region.childright = r2
            new_region.merge_order = merge_order
            return new_region

        elif isinstance(r1.pixel_list[0].spectrum, list):
            spectrum = []
            for i in range(0, len(r1.val)):
                spectrum = spectrum + ((r1.val[i] + r2.val[i]) / 2)
            new_region = Group(spectrum)
            new_region.neighbours = (r1.neighbours).union(r2.neighbours)
            new_region.neighbours.remove(r1)
            new_region.neighbours.remove(r2)
            ensemble_pixel = set(r1.pixel_list).union(set(r2.pixel_list))
            new_region.pixel_list = list(ensemble_pixel)
            new_region.childleft = r1
            new_region.childright = r2
            return new_region
