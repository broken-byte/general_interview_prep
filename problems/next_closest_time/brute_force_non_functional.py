from itertools import permutations
from datetime import datetime


class NextClosestTime:
    """
    Non functional brute force approach, since
    grabbing all the permutations is not enough to
    meet the requirements of the problem. Specifically,
    you can reuse a digit any number of times, which is not
    a permutation but rather a decision tree outcome given
    all digits available as possible paths.

    HOWEVER, I leave it here because this contains the logic
    for comparisons between times using Python's datetime
    module. The actual brute force approach will likely
    use a recursive decision tree structure, using that same
    logic for comparisons.
    """

    def __init__(self):
        self.time: str = ""
        self.next_closest_time: str = ""

    def nextClosestTime(self, time: str) -> str:
        self.time = time
        all_perms_of_given_time: list = self.get_all_permutations_of_given_time()
        self.next_closest_time: str = all_perms_of_given_time[0]
        for new_time in all_perms_of_given_time:
            if self.new_time_is_valid(new_time) and \
               self.new_time_is_between_given_time_and_next_closest_time(new_time):
                self.next_closest_time = new_time
        return self.next_closest_time

    def get_all_permutations_of_given_time(self) -> list:
        """
        Time Complexity: O(n!)
        """
        colon_index = 2
        time_digits = self.time[:colon_index] + self.time[colon_index + 1:]
        permutation_iterator = permutations(time_digits)
        perms = [''.join(p) for p in permutation_iterator]
        perms_formatted = [f'{p[:colon_index]}:{p[colon_index:]}' for p in perms]
        return perms_formatted

    def new_time_is_between_given_time_and_next_closest_time(self, new_time: str) -> bool:
        print(new_time)
        new_time = datetime.strptime(new_time, '%H:%M')
        given_time = datetime.strptime(self.time, '%H:%M')
        next_closest_time = datetime.strptime(self.next_closest_time, '%H:%M')
        return given_time < new_time < next_closest_time

    def new_time_is_valid(self, new_time: str) -> bool:
        colon_index = 2
        hours: int = int(new_time[:colon_index])
        minutes: int = int(new_time[colon_index + 1:])
        return hours < 24 and minutes < 60


if __name__ == '__main__':
    n_c_t = NextClosestTime()
    print(n_c_t.nextClosestTime("19:34"))
