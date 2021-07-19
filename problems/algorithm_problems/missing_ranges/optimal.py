from typing import List

# TODO: Fix the single element edge case
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        self.nums = nums
        self.lower = lower
        self.upper = upper
        self.result: List[str] = []
        if len(self.nums) == 0:
            self.handle_empty_case()
            return self.result
        elif self.lower == self.upper:
            self.handle_same_range_case()
            return self.result
        self.handle_initial_range()
        for index in range(len(self.nums) - 1):  # O(n)
            lower_bound = self.nums[index] + 1
            upper_bound = self.nums[index + 1] - 1
            if lower_bound > upper_bound:
                continue
            else:
                missing_val_range = self.transform_ranges(lower_bound, upper_bound)
                self.result.append(missing_val_range)
        self.handle_final_range()
        return self.result

    def handle_empty_case(self):
        if self.lower < self.upper:
            self.result.append(f'{self.lower}->{self.upper}')
        else:
            self.result.append(f'{self.lower}')

    def handle_same_range_case(self):
        if self.lower in self.nums:  # O(n)
            return
        else:
            self.result.append(f'{self.lower}')

    def handle_initial_range(self):
        initial_lower = self.lower
        initial_upper = self.nums[0] - 1
        if initial_lower == initial_upper:
            return
        else:
            initial_range = f'{initial_lower}->{initial_upper}'
            self.result.append(initial_range)

    def transform_ranges(self, lower: int, upper: int):
        if lower == upper:
            return f'{lower}'
        else:
            return f'{lower}->{upper}'

    def handle_final_range(self):
        final_lower = self.nums[len(self.nums) - 1] + 1
        final_upper = self.upper
        if final_lower == final_upper:
            return
        else:
            final_range = f'{final_lower}->{final_upper}'
            self.result.append(final_range)



