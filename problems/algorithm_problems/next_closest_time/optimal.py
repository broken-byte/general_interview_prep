from datetime import datetime, timedelta


class NextClosestTime:
    def nextClosestTime(self, time_plus_one_minute: str) -> str:
        """
        Time Complexity: O(24*60 possible times) -> O(1)
        Space Complexity: O(1)
        """
        unique_digits = set(time_plus_one_minute)
        while True:
            time_plus_one_minute = (datetime.strptime(time_plus_one_minute, '%H:%M') + timedelta(minutes=1)).strftime('%H:%M')
            unique_digits_in_time_plus_one_minute = set(time_plus_one_minute)
            if self.is_subset_of_the_other(unique_digits_in_time_plus_one_minute, unique_digits):
                return time_plus_one_minute

    def is_subset_of_the_other(self, a: set, b: set) -> bool:
        return a <= b


if __name__ == '__main__':
    n_c_t = NextClosestTime()
    print(n_c_t.nextClosestTime("19:34"))
