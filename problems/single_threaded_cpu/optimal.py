from collections import namedtuple
from heapq import heappush, heappop


Task = namedtuple('Task', ['enqueue_time', 'processing_time', 'original_index'])

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks: list[Task] = sort_converted_tasks_by_enqueue_time(tasks)
        current_cpu_clock = 0
        current_task_index = 0
        heap, processing_order = [], []
        while len(processing_order) < len(tasks):
            # Push all the tasks available at current CPU clock
            while current_task_index < len(tasks) and tasks[current_task_index].enqueue_time <= current_cpu_clock:
                task = tasks[current_task_index]
                prioritized_task = (task.processing_time, task.original_index)
                heappush(heap, prioritized_task)
                current_task_index += 1
            if heap:
                processing_time, original_index = heappop(heap)
                processing_order.append(original_index)
                current_cpu_clock += processing_time
            else:
                # Jump to the next available task
                current_cpu_clock = tasks[current_task_index].enqueue_time
        return processing_order


def sort_converted_tasks_by_enqueue_time(tasks: list[list[int]]) -> list[Task]:
    converted_tasks: list[Task] = []
    for original_index, task in enumerate(tasks):
        enqueue_time: int = task[0]
        processing_time: int = task[1]
        task = Task(enqueue_time, processing_time, original_index)
        converted_tasks.append(task)
    return sorted(converted_tasks)


if __name__ == '__main__':
    solution = Solution()
    print(solution.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]))
    print(solution.getOrder(tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))
    print(solution.getOrder(tasks=[[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]]))
