

def single_number(nums: list) -> int:
    xor_buffer: int = 0
    for num in nums:
        xor_buffer ^= num
    return xor_buffer


if __name__ == '__main__':
    print(single_number([2, 2, 1]))
    print(single_number([4, 1, 2, 1, 2]))
    # ^= -> a = a ^ num
    print(4 ^ 1 ^ 2 ^ 1 ^ 2)
