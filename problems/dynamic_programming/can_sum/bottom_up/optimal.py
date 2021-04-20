

def can_sum_forward_facing(target: int, nums: list) -> bool:
    table = [False for _ in range(target + 1)]
    table[0] = True  # dp[0] = can_sum(0, nums) -> True
    for i in range(len(table)):
        if table[i] is True:
            tabulate(i, table, nums)
    return table[target]


def tabulate(i, table, nums):
    for num in nums:
        if i + num < len(table):
            table[i + num] = True


if __name__ == '__main__':
    print(can_sum_forward_facing(7, [5, 3, 4, 7]))
    print(can_sum_forward_facing(7, [2, 4]))
    print(can_sum_forward_facing(300, [7, 14]))