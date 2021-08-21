

class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        """
        Algorithm Explaination: https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/196304/Verbosely-commented-Python-binary-search-approach-%2B-example-walkthrough
        N = len(nums)
        M = Maximum distance possible in nums
        Time Complexity: O(Nlog(N) + Nlog(M))
        Space Complexity: O(1)
        """
        def k_or_more_pairs_less_than_guess_distance(guess_distance: int) -> bool:
            """
            Time Complexity: O(2N) -> O(N)
            Space Complexity: O(1)
            """
            count = 0
            i, j = 0, 1
            while i < len(nums):
                # If the distance calculated from j-i is less than the guess,
                # increase the window on `j` side.
                while (j < len(nums)) and ((nums[j] - nums[i]) <= guess_distance):
                    j += 1
                number_of_distances_between_j_and_i = j - i - 1
                count += number_of_distances_between_j_and_i
                i += 1
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]

        while lo < hi:
            mid = (lo + hi) // 2
            if k_or_more_pairs_less_than_guess_distance(mid):
                # We don't set to `mid - 1` because we found a number of distances
                # bigger than *or equal* to `k`. If this `mid` ends up being
                # actually equal to `k` then it's a correct guess, so let's leave it within
                # the guess space.
                hi = mid
            else:
                lo = mid + 1
        # `lo` ends up being an actual distance in the input, because
        # the binary search mechanism waits until the exact lo/hi combo where
        # 2nd to last `mid` did not produce enough results (k or more), but
        # the last `mid` did.
        return lo
