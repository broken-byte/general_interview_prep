from typing import List, Dict
from collections import defaultdict, deque


def calculate_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph: Dict[str, Dict[str, float]] = create_division_graph(equations, values)
    output: List[float] = []
    for source, target in queries:
        quotient: float = evaluate_division(graph, source, target)
        output.append(quotient)
    return output


def create_division_graph(equations: List[List[str]], values: List[float]) -> Dict[str, Dict[str, float]]:
    division_graph = defaultdict(dict)
    for (dividend, divisor), value in zip(equations, values):
        print(dividend, divisor, value)
        division_graph[dividend][divisor] = value
        division_graph[divisor][dividend] = 1/value
    return division_graph


def evaluate_division(division_graph: dict, source: str, target: str) -> int:
    if source not in division_graph or target not in division_graph:
        return -1
    elif source == target:
        return 1
    visited = set()
    product: float = 1.0

    def dfs(node, current_value):
        if node in visited:
            return 1
        if node == target:
            return current_value
        visited.add(node)
        neighbors = division_graph[node]
        for neighbor, value in neighbors.items():
            return value * dfs(neighbor, value)
    return dfs(source, 1)


if __name__ == '__main__':
    equations: List[List[str]] = [
                    ["a", "b"],
                    ["b", "c"]
                ]
    values = [
                 2.0,
                 3.0
             ]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calculate_equation(equations, values, queries))

    equations = [["a", "b"], ["c", "d"]]
    values = [1.0, 1.0]
    queries = [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]
    print(calculate_equation(equations, values, queries))
