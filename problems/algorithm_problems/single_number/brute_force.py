from collections import Counter


def single_number(nums: list) -> int:  # O(n)
    number_count = Counter(nums)
    for num in nums:
        if number_count[num] == 1:
            return num


if __name__ == '__main__':
    single_number([2, 2, 1])
    single_number([4, 1, 2, 1, 2])
