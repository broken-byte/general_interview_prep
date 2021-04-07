from typing import List


def can_construct(target_word: str, word_bank: List[str]) -> bool:
    memo: dict = {}

    def can_construct_recursively(target: str) -> bool:
        """
        N = len(word_bank)
        M = len(target)
        Time Complexity: O(N*M^2)  # branchFactor^worstCaseDepth*findCost
        Space Complexity: O(M^2)  # recursionDepth*findCost
        """
        if target in memo:
            return memo[target]
        elif target == "":
            return True
        else:
            for word in word_bank:
                if target.find(word) == 0:
                    suffix: str = target[len(word):]
                    if can_construct_recursively(suffix):
                        memo[target] = True
                        return True
            memo[target] = False
            return False

    return can_construct_recursively(target_word)


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
