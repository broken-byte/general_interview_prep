

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        frequency = 0
        n = len(arr)
        for index in range(n):
            frequency = odd_sub_frequency_of_current_element_with_previous_element(index, frequency) + \
                        odd_sub_frequency_of_current_element(index, n)
            result += frequency * arr[index]
        return result


def odd_sub_frequency_of_current_element_with_previous_element(index: int, previous_frequency: int) -> int:
    return previous_frequency - (index + 1) // 2


def odd_sub_frequency_of_current_element(index: int, n: int) -> int:
    return (n - index + 1) // 2
