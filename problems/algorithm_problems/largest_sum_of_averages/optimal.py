

class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        """
        N = len(nums)
        Time Complexity: O(K*N^2)
        Space Complexity: O(N*K)
        """
        cache: dict[tuple: float] = {}

        def search(n: int, number_of_partitions: int) -> float:
            if (n, number_of_partitions) in cache:
                return cache[n, number_of_partitions]
            if n < number_of_partitions:
                return 0
            if number_of_partitions == 1:
                left_hand_average: float = sum(nums[:n]) / float(n)
                cache[n, number_of_partitions] = left_hand_average
                return cache[n, number_of_partitions]
            rolling_sum = 0
            cache[n, number_of_partitions] = 0
            for index in range(n - 1, 0, -1):
                rolling_sum += nums[index]
                rolling_average: float = rolling_sum / float(n - index)
                cache[n, number_of_partitions] = max(
                    cache[n, number_of_partitions],
                    search(index, number_of_partitions - 1) + rolling_average
                )

            return cache[n, number_of_partitions]

        return search(len(nums), k)


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestSumOfAverages(nums=[9, 1, 2, 3, 9], k=3))
    print(solution.largestSumOfAverages(nums=[1, 2, 3, 4, 5, 6, 7], k=4))