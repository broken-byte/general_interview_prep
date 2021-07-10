import heapq

"""
This Implementation does not work! I kept it because of the custom heap wrapper and TimeBucket class.
P.S. It ALMOST works lol
"""


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        time_buckets = TimeBuckets(tasks)
        time_buckets.print()
        order_of_processing: list[int] = []
        task_heap = TaskHeap()
        time_until_idle: int = 0
        for time in range(time_buckets.get_min_time(), time_buckets.get_max_time() + 1):
            if not time_buckets.time_bucket_exists_at_time(time):
                continue
            for task in time_buckets.get_tasks_at_time(time):
                task_heap.push(task)
            if time_until_idle == 0:
                shortest_task = task_heap.pop()
                processing_time: int = shortest_task[0]
                task_id: int = shortest_task[1]
                order_of_processing.append(task_id)
                time_until_idle = processing_time
            if time_until_idle != 0:
                time_until_idle -= 1
        while not task_heap.empty():
            shortest_task = task_heap.pop()
            task_id: int = shortest_task[1]
            order_of_processing.append(task_id)
        return order_of_processing


class TimeBuckets:
    def __init__(self, tasks: list[list[int]]):
        self._tasks: list[list[int]] = tasks
        self._time_buckets: dict[int: list[tuple]] = {}
        self._max_enqueue_time = tasks[0][0]
        self._min_enqueue_time = tasks[0][0]
        self._bucket_sort_tasks_by_enqueue_time()

    def _bucket_sort_tasks_by_enqueue_time(self):
        for index, task in enumerate(self._tasks):
            task_id: int = index
            enqueue_time, processing_time = task
            if enqueue_time not in self._time_buckets:
                self._time_buckets[enqueue_time] = []
            self._time_buckets[enqueue_time].append((processing_time, task_id))
            if enqueue_time > self._max_enqueue_time:
                self._max_enqueue_time = enqueue_time
            if enqueue_time < self._min_enqueue_time:
                self._min_enqueue_time = enqueue_time

    def get_tasks_at_time(self, t: int) -> list[tuple]:
        return self._time_buckets[t]

    def get_min_time(self) -> int:
        return self._min_enqueue_time

    def get_max_time(self) -> int:
        return self._max_enqueue_time

    def time_bucket_exists_at_time(self, t: int) -> bool:
        return t in self._time_buckets

    def print(self):
        for time in sorted(self._time_buckets.keys()):
            print(f'Time: {time}, Tasks Available: {self._time_buckets.get(time)}')


class TaskHeap(object):
    def __init__(self):
        self._data = []

    def push(self, task):
        heapq.heappush(self._data, task)

    def pop(self):
        return heapq.heappop(self._data)

    def empty(self) -> bool:
        return len(self._data) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]))
    print(solution.getOrder(tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))
    # Failed
    print(solution.getOrder(tasks=[[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]]))
