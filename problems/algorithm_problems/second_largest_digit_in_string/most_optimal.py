

class Solution:
    def secondHighest(self, s: str) -> int:
        digits: list[int] = get_unique_digits(s)
        digits.sort()
        if len(digits) > 2:
            return digits[-2]
        elif len(digits) == 2:
            return digits[0]
        return -1


def get_unique_digits(s: str) -> list[int]:
    digits_only: list[int] = [int(char) for char in s if char.isnumeric()]
    unique_digits_only: list[int] = list(set(digits_only))
    return unique_digits_only
