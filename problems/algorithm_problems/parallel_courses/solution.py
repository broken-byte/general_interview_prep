from typing import List
from collections import defaultdict


class Solution:

    def __init__(self):
        self.n = 0
        self.relations: List[List[int]] = []
        self.class_graph: dict = defaultdict()
        self.schedule: list = []
        self.next_semester_schedule: list = []
        self.semesters_taken: int = 0
        self.completed_class_count: int = 0

    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        self.n = n
        self.relations = relations
        self.create_class_graph()
        self.fill_schedule_with_available_classes()
        self.take_courses_for_the_semester()
        return self.semesters_taken if self.all_courses_taken() else -1

    def create_class_graph(self):
        for node in range(1, self.n + 1):
            self.class_graph[node] = {
                "prerequisite_count": 0,
                "dependent_classes": []
            }
        for prerequisite, cls in self.relations:
            self.class_graph[prerequisite]["dependent_classes"].append(cls)
            self.class_graph[cls]["prerequisite_count"] += 1

    def fill_schedule_with_available_classes(self):
        for node in self.class_graph.keys():
            if self.class_graph[node]["prerequisite_count"] == 0:
                self.schedule.append(node)

    def take_courses_for_the_semester(self):
        while not self.schedule_empty():
            self.start_new_semester()
            self.next_semester_schedule: list = []
            for current_class in self.schedule:
                self.completed_class_count += 1
                dependent_classes: list = self.class_graph[current_class]["dependent_classes"]
                self.remove_current_class_as_dependency_of(dependent_classes)
            self.schedule = self.next_semester_schedule

    def schedule_empty(self) -> bool:
        return len(self.schedule) == 0

    def start_new_semester(self):
        self.semesters_taken += 1

    def remove_current_class_as_dependency_of(self, dependent_classes: list):
        for cls in dependent_classes:
            self.class_graph[cls]["prerequisite_count"] -= 1
            if self.all_prerequisites_met(cls):
                self.next_semester_schedule.append(cls)

    def all_prerequisites_met(self, cls: int) -> bool:
        return self.class_graph[cls]["prerequisite_count"] == 0

    def all_courses_taken(self) -> bool:
        return self.completed_class_count == self.n

    def clear_memory(self):
        self.n = 0
        self.relations = []
        self.class_graph = {}
        self.next_semester_schedule = []
        self.semesters_taken = 0
        self.schedule = []
        self.completed_class_count = 0


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.minimumSemesters(3, [[1, 3], [2, 3]]))
    solution.clear_memory()
    print(solution.minimumSemesters(3, [[1,2],[2,3],[3,1]]))
