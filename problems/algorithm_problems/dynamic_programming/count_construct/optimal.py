

def count_construct(target: str, word_bank: list) -> int:
    """
    M = len(target)
    N = number of words in word_bank
    Time Complexity: O(M*N)
    Space Complexity: O(M^2)
    """
    memo: dict = {}

    def count_construct_recursively(deconstruction: str) -> int:
        if deconstruction in memo:
            return memo[deconstruction]
        elif len(deconstruction) == 0:
            return 1
        else:
            count_of_constructs: int = 0
            for word in word_bank:
                if deconstruction.find(word) == 0:
                    suffix: str = deconstruction[len(word):]
                    result = count_construct_recursively(suffix)
                    count_of_constructs += result
            memo[deconstruction] = count_of_constructs
            return memo[deconstruction]

    return count_construct_recursively(target)


if __name__ == '__main__':
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(count_construct("", ["cat", "dog", "mouse"]))
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
                            "e",
                            "ee",
                            "eee",
                            "eeee",
                            "eeeee",
                            "eeeeee"
    ]))