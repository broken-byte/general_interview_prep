from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    rooms_needed = 0
    start_times: List[int] = sorted(interval[0] for interval in intervals)
    end_times: List[int] = sorted(interval[1] for interval in intervals)
    start_pointer = end_pointer = 0
    while start_pointer < len(start_times):
        start_time: int = start_times[start_pointer]
        end_time: int = end_times[end_pointer]
        if room_is_free_for_use(start_time, end_time):
            rooms_needed -= 1
            end_pointer += 1  # Finish current meeting
        rooms_needed += 1
        start_pointer += 1  # Compare next meetings start time to see if we can reuse a meeting room
    return rooms_needed


def room_is_free_for_use(start_time: int, end_time: int) -> bool:
    return start_time >= end_time


if __name__ == '__main__':
    print(minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))
    print(minMeetingRooms(intervals = [[7,10],[2,4]]))
    print(minMeetingRooms(intervals = [[9,10],[4,9],[4,17]]))
    print(minMeetingRooms(intervals = [[2,11],[6,16],[11,16]]))
