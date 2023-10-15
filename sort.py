from typing import List, Optional

class Sorts:

    def bubble_sort(self, list_integers: list[int]):
        passes = 0
        exchanges = 0
        exchanges_per_pass = dict()
        while True:
            has_exchanges = False
            for index in range(len(list_integers) - 1):
                left_num = list_integers[index]
                right_num = list_integers[index + 1]
                if left_num > right_num:
                    list_integers[index], list_integers[index + 1] = left_num, right_num
                    exchanges += 1
                    has_exchanges = True

            passes += 1
            if not has_exchanges:
                break

            exchanges_per_pass[passes] = exchanges

    def insertion_sort(self, integers: List[int]) -> List[int]:
        """Removes the minimum item from a list and adds it to another until that list is empty"""
        sorted_list = []
        while len(integers) != 0:
            sorted_list.append(min(integers))
            integers.remove(min(integers))
        return sorted_list

    def index_pivot(self, integers: List[int]) -> Optional[int]:
        """Returns middle index for odd-lengthed lists"""
        length_list = len(integers)
        if length_list != 0:
            if length_list % 2 != 0:
                return length_list // 2

    def biggest_divisor_excluding_itself(self, integers: List[int]) -> Optional[int]:
        """Returns the biggest divisor of the length of the list, excluding itself"""
        length_list = len(integers)
        for integer in range(length_list - 1, 1, -1):
            if length_list % integer == 0:
                return integer

    def rearrange_integers(self, integers: List[int], pivot_index: int) -> List[int]:
        """Rearranges items to the left and right side of the pivot"""
        index_head = 0
        length_list = len(integers)
        index_tail = length_list - 1
        pivot_value = integers[pivot_index]
        while index_head <= index_tail:
            while integers[index_head] < pivot_value:
                index_head += 1
            while integers[index_tail] > pivot_value:
                index_tail -= 1
            if index_head <= index_tail:
                integers[index_head], integers[index_tail] = integers[index_tail], integers[index_head]
                index_head += 1
                index_tail -= 1
        return integers

    def create_partitions(self, integers: List[int]) -> Optional[List[List[int]]]:
        """Creates partitions of the list based on the biggest divisor"""
        partitions = []
        divisor = self.biggest_divisor_excluding_itself(integers)
        for integer in range(0, len(integers), divisor):
            partition = integers[integer:integer + divisor]
            partitions.append(partition)
        return partitions



