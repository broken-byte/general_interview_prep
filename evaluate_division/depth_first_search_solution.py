from typing import List, Dict
from collections import defaultdict, deque


def create_division_graph(equations: List[List[str]], values: List[float]) -> Dict[str, Dict[str, float]]:
    division_graph = defaultdict(dict)
    for (dividend, divisor), value in zip(equations, values):
        print(dividend, divisor, value)
        division_graph[dividend][divisor] = value
        division_graph[divisor][dividend] = 1/value
    return division_graph


def evaluate_division(division_graph: dict, source: str, target: str) -> int:
    pass