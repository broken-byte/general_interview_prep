

class StairClimber:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def __init__(self):
        self.total_steps: int = 0
        self.memo: dict = {}

    def climbStairs(self, n: int) -> int:
        self.total_steps = n
        self.memo = {}
        return self.climb_recursively(0)

    def climb_recursively(self, step: int) -> int:
        if step in self.memo:
            return self.memo[step]
        elif step == self.total_steps:
            return 1
        elif step > self.total_steps:
            return 0
        else:
            number_of_ways_for_one_step: int = self.climb_recursively(step + 1)
            number_of_ways_for_two_steps: int = self.climb_recursively(step + 2)
            summation_of_ways = number_of_ways_for_one_step + number_of_ways_for_two_steps
            self.memo[step] = summation_of_ways
            return summation_of_ways


if __name__ == '__main__':
    stair_climber = StairClimber()
    print(stair_climber.climbStairs(2))
    print(stair_climber.climbStairs(3))
    print(stair_climber.climbStairs(36))
