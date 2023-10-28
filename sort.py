from typing import List, Optional

class Sorts:

    def bubble_sort(self, nums: list[int]) -> List[int]:
        passes = 0
        exchanges = 0
        while True:
            has_exchanges = False
            for index in range(len(nums) - 1):
                left_num = nums[index]
                right_num = nums[index + 1]
                if left_num > right_num:
                    nums[index], nums[index + 1] = left_num, right_num
                    exchanges += 1
                    has_exchanges = True

            passes += 1
            if not has_exchanges:
                return nums

    def insertion_sort(self, nums: List[int]) -> List[int]:
        sorted_nums = []
        while len(nums) != 0:
            sorted_nums.append(nums.pop(min(nums)))
        return nums