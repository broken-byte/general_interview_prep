

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        N = len(weights)
        Time Complexity: Nlog(sum(weights))
        Space Complexity: O(1)

        Algorithm: Binary Search
        """

        def can_ship_items_in_time_with(ship_capacity: int) -> bool:
            """
            Time Complexity: O(N)
            Space Complexity: O(1)
            """
            day_count = 1
            rolling_weight_sum = 0
            for item_weight in weights:
                rolling_weight_sum += item_weight
                if rolling_weight_sum > ship_capacity:
                    rolling_weight_sum = item_weight
                    day_count += 1
                if day_count > days:
                    return False
            return True

        left: int = max(weights)
        right: int = sum(weights)
        while left < right:
            middle_ship_capacity_guess = left + (right - left) // 2
            if can_ship_items_in_time_with(middle_ship_capacity_guess):
                right = middle_ship_capacity_guess
            else:
                left = middle_ship_capacity_guess + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
    print(solution.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
    print(solution.shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))
