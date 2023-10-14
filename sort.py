class Sort:

    def bubble_sort(self, lst_nums: list) -> dict:
        passes = 0
        exchanges = 0
        exchanges_per_pass = dict()
        while True:
            has_exchanges = False
            for index in range(len(lst_nums) - 1):
                left_num = lst_nums[index]
                right_num = lst_nums[index + 1]
                if left_num > right_num:
                    lst_nums[index], lst_nums[index + 1] = left_num, right_num
                    exchanges += 1
                    has_exchanges = True
                print(lst_nums)

            passes += 1
            if not has_exchanges:
                break

            exchanges_per_pass[passes] = exchanges

        return exchanges_per_pass
