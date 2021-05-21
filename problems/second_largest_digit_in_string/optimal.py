from collections import deque


class Solution:
    def secondHighest(self, s: str) -> int:
        """
        Time Complexity: O(n)
        """
        largest_two = deque([-1, -1])
        for element in s:
            if element.isnumeric():
                if int(element) > largest_two[0]:
                    largest_two.pop()
                    largest_two.appendleft(int(element))
                elif int(element) > largest_two[1] and int(element) != largest_two[0]:
                    largest_two[1] = int(element)
        return largest_two.pop()
