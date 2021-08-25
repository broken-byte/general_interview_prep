

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)

        Algorithm: Sliding Window:
        ----------------------------
        We compare sub-array products,
        increment the total count every time we have a
        valid product, and reduce the sub_array window
        if we go beyond k, thus counting only valid sub
        -arrays! Beautiful approach, especially since
        I had to look up the answer after taking too
        long XD

        BTW, this solution only works assuming the
        numbers are ALL positive :)
        """

        def product_too_large() -> bool:
            return product_for_current_window >= k

        def window_doesnt_overlap() -> bool:
            return left_cursor <= right_cursor

        n: int = len(nums)
        left_cursor = 0
        product_for_current_window = 1
        count_of_sub_arrays = 0
        for right_cursor in range(n):
            product_for_current_window *= nums[right_cursor]
            while product_too_large() and window_doesnt_overlap():
                product_for_current_window /= nums[left_cursor]
                left_cursor += 1
            count_of_sub_arrays += (right_cursor - left_cursor) + 1
        return count_of_sub_arrays


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
