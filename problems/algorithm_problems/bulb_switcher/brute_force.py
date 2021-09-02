

class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Time Complexity: O(N^2)
        Space Complexity: O(N)

        This algorithm is correct functionally,
        but it results in a Time Limit Exceeded
        on LeetCode, so on to the optimal solution!
        """
        if n == 0 or n == 1:
            return n
        bulb_is_on: list[bool] = [True] * n

        def toggle_bulbs_given_round_number(current_round: int) -> None:
            """
            Time Complexity: O(n)
            Space Complexity: O(1)
            """
            if current_round == n - 1:
                bulb_is_on[-1] = not bulb_is_on[-1]
                return
            step_size: int = current_round + 1
            start: int = current_round
            stop: int = n
            for index in range(start, stop, step_size):
                bulb_is_on[index] = not bulb_is_on[index]

        for round_number in range(1, n):
            toggle_bulbs_given_round_number(round_number)

        return get_lit_bulb_count(bulb_is_on)


def get_lit_bulb_count(bulbs: list[bool]) -> int:
    number_of_lit_bulbs: int = 0
    for bulb_is_on in bulbs:
        if bulb_is_on:
            number_of_lit_bulbs += 1
    return number_of_lit_bulbs


if __name__ == '__main__':
    solution = Solution()
    print(solution.bulbSwitch(n=3))
    print(solution.bulbSwitch(n=0))
    print(solution.bulbSwitch(n=1))
    print(solution.bulbSwitch(n=4))


