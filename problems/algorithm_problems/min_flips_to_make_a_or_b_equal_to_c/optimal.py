

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        N = maximum significant bits of a, b, c
        Time Complexity: O(N)
        Space Complexity: O(1)

        Algorithm: LSB Window Linear Search
        ------------------------------------
        1. get the least significant bits (LSB) for  a, b, and c
        2. Compare:
            - If c's LSB is 1 and both a and b's LSB's are 0,
            we just have to switch one bit!

            - If c's LSB is 0, and at least one of a or b's LSB is 1 (XOR),
            we still just have to switch one bit.

            - If c's LSB is 0 and BOTH LSB's of a and b are 1 (AND),
            we have to switch both of them!

        3. After every iteration we right shift a, b, and c to move the LSB's to
        the next set of values.

        4. At the end, we will have gone through every significant bit in constant
        space and linear time! :)

        I recommend this guide if you need a refresher on bits for Python :)
        https://realpython.com/python-bitwise-operators/
        """
        if a | b == c:
            return 0
        min_flips = 0
        while a != 0 or b != 0 or c != 0:
            a_lsb, b_lsb, c_lsb = get_least_significant_bits_of(a, b, c)
            if c_lsb == 1 and a_lsb == 0 and b_lsb == 0:
                min_flips += 1
            elif c_lsb == 0 and a_lsb ^ b_lsb:
                min_flips += 1
            elif c_lsb == 0 and a_lsb & b_lsb:
                min_flips += 2
            a, b, c = get_right_shifted_by_1_values_of(a, b, c)
        return min_flips


def get_least_significant_bits_of(a: int, b: int, c: int) -> tuple:
    return a & 1, b & 1, c & 1


def get_right_shifted_by_1_values_of(a: int, b: int, c: int) -> tuple:
    return a >> 1, b >> 1, c >> 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minFlips(a=2, b=6, c=5))
    print(solution.minFlips(a=4, b=2, c=7))
    print(solution.minFlips(a=1, b=2, c=3))
