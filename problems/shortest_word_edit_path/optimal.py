from collections import defaultdict
from collections import deque


def shortestWordEditPath(source: str, target: str, words: list) -> int:
    """
    n = len(words)
    m = len(word)
    Time Complexity: O(n^2*m)
    Space Complexity: O(n)
    """
    if len(source) != len(target):
        return -1
    graph: dict = create_word_graph(source, words)
    length_of_shortest_path_from_source_to_target: int = breadth_first_search(graph, source, target)
    return length_of_shortest_path_from_source_to_target


def create_word_graph(source, words) -> dict:  # O(n^2*m)
    adjacency_list: dict = defaultdict(list)
    words.append(source)
    for word in words:  # O(n)
        adjacency_list[word] = []
        for other_word in words:  # O(n)
            if has_difference_of_only_one_letter(word, other_word):
                adjacency_list[word].append(other_word)
    return adjacency_list


def has_difference_of_only_one_letter(word, other_word) -> bool:  # O(m)
    index = 0
    number_of_differences = 0
    while index < len(word):  # O(m)
        character: str = word[index]
        other_character: str = other_word[index]
        if character != other_character:
            number_of_differences += 1
        index += 1
    return number_of_differences == 1


def breadth_first_search(graph, source, target):  # O(N + Edges)
    visited = set()
    queue = deque()
    visited.add(source)
    queue.append((source, 0))
    while len(queue) != 0:
        word_node, depth = queue.popleft()
        if word_node == target:
            return depth
        for neighbor in graph[word_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    return -1


