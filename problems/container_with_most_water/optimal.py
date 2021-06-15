

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area: int = 0
        while left_pointer <= right_pointer:
            left_height: int = height[left_pointer]
            right_height: int = height[right_pointer]
            distance: int = right_pointer - left_pointer
            current_area: int = get_area(left_height, right_height, distance)
            if current_area > max_area:
                max_area = current_area
            if left_height < right_height:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area


def get_area(left: int, right:int, distance: int) -> int:
    return min(left, right) * distance
