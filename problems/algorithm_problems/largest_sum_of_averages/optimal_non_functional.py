
class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        """
        Time Complexity: O(Nlog(N))
        Space Complexity: O(1)

        This algorithm does not work because
        the problem states that the sub arrays
        must be adjacent! This algo assumes
        that sub arrays can be non adjacent :(
        """
        nums.sort()
        n: int = len(nums)
        partition_index: int = n - (k - 1)
        count_of_first_partition_size = 0
        summation_of_first_partition = 0
        for index in range(partition_index):
            count_of_first_partition_size += 1
            summation_of_first_partition += nums[index]
        summation_of_single_partitions = 0
        for index in range(partition_index, n):
            summation_of_single_partitions += nums[index]
        return (summation_of_first_partition / count_of_first_partition_size) + summation_of_single_partitions


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestSumOfAverages(nums=[9, 1, 2, 3, 9], k=3))
    print(solution.largestSumOfAverages(nums=[1, 2, 3, 4, 5, 6, 7], k=4))