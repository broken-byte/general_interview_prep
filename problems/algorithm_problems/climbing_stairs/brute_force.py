

class StairClimber:
    """
    Time Complexity: O(2^N)
    Space Complexity: O(n
    """
    def __init__(self):
        self.total_steps: int = 0

    def climbStairs(self, n: int) -> int:
        self.total_steps = n
        return self.climb_recursively(0)

    def climb_recursively(self, step: int) -> int:
        if step == self.total_steps:
            return 1
        elif step > self.total_steps:
            return 0
        else:
            number_of_ways_for_one_step: int = self.climb_recursively(step + 1)
            number_of_ways_for_two_steps: int = self.climb_recursively(step + 2)
            return number_of_ways_for_one_step + number_of_ways_for_two_steps


if __name__ == '__main__':
    stair_climber = StairClimber()
    print(stair_climber.climbStairs(2))
    print(stair_climber.climbStairs(3))
