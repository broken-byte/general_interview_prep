
class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)

        Algorithm:
        -----------
        I struggled with this one!
        Essentially, the eureka is that
        we only need the max and min values.
        Once we know those, we check
        if the possible range of change using
        K overlaps (minimum + k >= maximum - k).

        if it does, we know that every other number
        falls WITHIN that range, and therefore we
        could eventually use the X operation to
        equalize every number. return 0!

        if not, then the best we can do is move
        the max and min as close as possible,
        so the optimal score possible is the
        adjusted difference. return (minimum + k) - (maximum - k)
        """
        adjusted_minimum: int = min(nums) + k
        adjusted_maximum: int = max(nums) - k
        if adjusted_minimum >= adjusted_maximum:
            return 0
        return adjusted_maximum - adjusted_minimum
