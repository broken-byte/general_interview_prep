from functools import lru_cache


class Solution:
    """
    Still have not solved this problem. I will go back to it one day!
    It is an NP-Hard problem, and is listed as Hard on LeetCode. So,
    on to the next one lol.
    """
    def maxHappyGroups(self, batch_size, groups):
        max_happy_groups = get_guaranteed_happy_groups(groups, batch_size)
        filter_out_guaranteed_happy_groups(groups, batch_size)
        remainder_frequency_counter = get_counts_of_how_many_remainders_there_are_in_groups(groups, batch_size)
        max_happy_groups += get_number_of_happy_groups_obtained_from_complimentary_pairs(groups, batch_size)
        if sum(remainder_frequency_counter) == 0:
            # No need to brute force
            return max_happy_groups
        brute_force_result = brute_force_find_optimal_ordering_of_groups(remainder_frequency_counter, batch_size)
        return max_happy_groups + brute_force_result


def get_guaranteed_happy_groups(groups: list[int], batch_size: int) -> int:
    return sum(group % batch_size == 0 for group in groups)


def filter_out_guaranteed_happy_groups(groups: list[int], batch_size: int):
    groups = [g for g in groups if g % batch_size != 0]


def get_counts_of_how_many_remainders_there_are_in_groups(groups: list[int], batch_size: int) -> list[int]:
    remainder_frequency_counter = [0] * batch_size
    for group in groups:
        remainder_frequency_counter[group % batch_size] += 1
    return remainder_frequency_counter


def get_number_of_happy_groups_obtained_from_complimentary_pairs(remainder_frequency_counter: list[int], batch_size: int) -> int:
    complimentary_pair_happy_groups = 0
    for remainder in range(1, batch_size):
        compliment_frequency = 0
        if 2 * remainder != batch_size:
            compliment_frequency = min(
                remainder_frequency_counter[remainder],
                remainder_frequency_counter[batch_size - remainder]
            )
        else:
            compliment_frequency = remainder_frequency_counter[remainder] // 2
        complimentary_pair_happy_groups += compliment_frequency
        remainder_frequency_counter[remainder] -= compliment_frequency
        remainder_frequency_counter[batch_size - remainder] -= compliment_frequency
    return complimentary_pair_happy_groups


def brute_force_find_optimal_ordering_of_groups(remainder_frequency_counter: list[int], batch_size: int):
    @lru_cache(None)
    def dfs(position, last):
        if sum(position) == 0:
            return 0
        ans = float("-inf")
        for i in range(batch_size):
            if position[i] > 0:
                t = [j for j in position]
                t[i] -= 1
                U = (last - i) % batch_size
                ans = max(ans, dfs(tuple(t), U) + (U == 0))
        return ans

    depth_first_search_ordering = [dfs(tuple(remainder_frequency_counter), i) for i in range(1, batch_size)]
    return max(depth_first_search_ordering)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxHappyGroups(batch_size=3, groups=[1, 2, 3, 4, 5, 6]))
