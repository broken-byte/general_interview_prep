
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        a, b = halve(s)
        return are_alike(a, b)


def halve(s: str) -> tuple:
    """
    TC, SC = O(n), O(1)
    """
    middle_index = len(s) // 2
    a = s[:middle_index]
    b = s[middle_index:]
    return a, b


def are_alike(a: str, b: str) -> bool:
    """
    TC, SC = O(n), O(1)
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    a_count, b_count = 0, 0
    for a_char, b_char in zip(a, b):
        if a_char in vowels:
            a_count += 1
        if b_char in vowels:
            b_count += 1
    return a_count == b_count


if __name__ == '__main__':
    print(halve("book"))
    solution = Solution()
    print(solution.halvesAreAlike("book"))
