import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)

        Algorithm
        ------------------------------
        Essentially, this problem
        devolves to finding the pattern
        of bulbs on as n gets large.


        Essentially, the number of
        on bulbs increases on every
        perfect square root, so just
        round down for any value that
        doesn't fall on a perfect square root.

        sqrt(3) -> 1.7 -> 1
        sqrt(4) -> 2
        etc...

        I had to look up the
        answer but dang was I close! I
        haven't decided if I like these types
        of questions, but either way the outcome
        was pleasantly simple :)
        """
        return int(math.sqrt(n))


if __name__ == '__main__':
    solution = Solution()
    for n in range(27):
        print(f"N = {n}, number of bulbs left on: {solution.bulbSwitch(n)}")
