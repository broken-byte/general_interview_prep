from typing import List


def can_construct(target: str, word_bank: List[str]) -> bool:
    """
    N = len(word_bank)
    M = len(target)
    Time Complexity: O(N^(M)*M)  # branchFactor^worstCaseDepth*stringCopy
    Space Complexity: O(M^2)  # recursionDepth*stringCopy
    """
    if target == "":
        return True
    else:
        for word in word_bank:
            if target.find(word) == 0:
                suffix: str = target[len(word):]
                if can_construct(suffix, word_bank):
                    return True
        return False


if __name__ == '__main__':
    """
    ab -> abab -> ababab
    ab -> abcd -> abcda
    """
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(can_construct("", ["cat", "dog", "mouse"]))
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
                            "e",
                            "ee",
                            "eee",
                            "eeee",
                            "eeeee",
                            "eeeeee"
    ]))
