

def can_construct(target_word: str, word_bank: list[str]) -> bool:
    """
    N = len(word_bank)
    M = len(target_word)
    Time Complexity: O(N*M^2)
    Space Complexity: O(M)
    """
    table: list[bool] = [False for _ in range(len(target_word) + 1)]
    table[0] = True
    for index in range(len(target_word) + 1):  # O(m)
        if not table[index] or index == len(target_word):
            continue
        tabulate(index, table, target_word, word_bank)
    return table[len(target_word)]


def tabulate(index: int, table: list[bool], target_word: str,  word_bank: list[str]):  # O(n*m)
    for word in word_bank:  # O(n)
        if characters_match_up_at_index(word, target_word, index):  # O(m)
            movement_forward: int = len(word)
            if index + movement_forward < len(table):
                table[index + movement_forward] = True


def characters_match_up_at_index(word: str, target_word: str, index: int) -> bool:  # O(m)
    return target_word[index: index + len(word)] == word


if __name__ == '__main__':
    """
    ab -> abab -> ababab
    ab -> abcd -> abcda
    """
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(can_construct("", ["cat", "dog", "mouse"]))
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        [
            "e",
            "ee",
            "eee",
            "eeee",
            "eeeee",
            "eeeeee"
        ]
    ))
