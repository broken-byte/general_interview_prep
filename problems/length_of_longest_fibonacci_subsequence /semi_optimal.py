

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        """
        n = len(arr)
        m = max(arr)
        Time Complexity: O(n^2*log(m))
        Space Complexity: O(n)

        n^2 - nested for loop
        log(m) - number of iterations before fibonacci number exceeds m, the maximum number in arr
        """
        hashed_values = set(arr)
        n: int = len(arr)
        max_fib_length: int = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                previous_value: int = arr[i]
                current_value: int = arr[j]
                extrapolated_length: int = get_extrapolated_fib_length_for_current_fib_values(previous_value, current_value, hashed_values)
                max_fib_length = max(max_fib_length, extrapolated_length)
        return max_fib_length if max_fib_length >= 3 else 0


def get_extrapolated_fib_length_for_current_fib_values(previous_value: int, current_value: int, hashed_values: set) -> int:
    possible_next_value: int = previous_value + current_value
    length = 2
    while possible_next_value in hashed_values:
        current_value, possible_next_value = possible_next_value, current_value + possible_next_value
        length += 1
    return length


if __name__ == '__main__':
    solution = Solution()
    print(solution.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
    print(solution.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
