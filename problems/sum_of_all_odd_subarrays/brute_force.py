

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        """
        Time Complexity: O(n^3)
        Space Complexity: O(1)
        """
        final_sum: int = 0
        n: int = len(arr)
        for i in range(n):
            for j in range(i, n):
                sub_array: list = arr[i: j + 1]
                if len(sub_array) % 2 != 0:
                    final_sum += sum(sub_array)
        return final_sum
