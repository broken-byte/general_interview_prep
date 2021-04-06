from typing import List


def can_construct(target: str, word_bank: List[str]) -> bool:
    """
    N = len(word_bank)
    M = len(target)
    Time Complexity: O(N^(M)*M)  # branchFactor^worstCaseDepth*stringCopy
    Space Complexity: O(M^2)  # recursionDepth*stringCopy
    """
    return can_construct_recursively("", target, word_bank)


def can_construct_recursively(construct: str, target: str, word_bank: List[str]) -> bool:
    if construct == target:
        return True
    elif len(construct) >= len(target):
        return False
    else:
        for word in word_bank:
            if can_construct_recursively(construct + word, target, word_bank):
                return True
        return False


if __name__ == '__main__':
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(can_construct("", ["cat", "dog", "mouse"]))
