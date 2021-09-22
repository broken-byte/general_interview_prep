

class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def findPoisonedDuration(self, time_series: list[int], duration: int) -> int:
        clock = time_series[0] + duration - 1
        poison_duration = duration
        for attack_time in time_series[1:]:
            if clock >= attack_time:
                overlap: int = clock - attack_time
                poison_duration += duration - (overlap + 1)
            else:
                poison_duration += duration
            clock = attack_time + duration - 1
        return poison_duration


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPoisonedDuration(time_series=[1, 4], duration=2))
    print(solution.findPoisonedDuration(time_series=[1, 2], duration=2))
    print(solution.findPoisonedDuration(time_series=[1, 3], duration=4))

