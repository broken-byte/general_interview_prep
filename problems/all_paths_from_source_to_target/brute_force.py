from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    n= len(graph)
    source = 0
    target = n - 1
    all_paths = []

    def backtracking_traversal(current_node: int, path: list):
        if current_node == target:
            all_paths.append(path.copy())
            return
        else:
            if current_node == source:
                path.append(current_node)
            for neighbor in graph[current_node]:
                path.append(neighbor)
                backtracking_traversal(neighbor, path)
                path.pop()

    path_to_record = []
    backtracking_traversal(source, path_to_record)
    return all_paths


if __name__ == '__main__':
    print(allPathsSourceTarget([[1,2],[3],[3],[]]))


