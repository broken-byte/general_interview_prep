

def count_construct(target: str, word_bank: list) -> int:
    """
    M = len(target)
    N = number of words in word_bank
    Time Complexity: O(N^M*M)
    Space Complexity: O(M^2)
    """
    if len(target) == 0:
        return 1
    else:
        count_of_constructs: int = 0
        for word in word_bank:  # O(N)
            if target.find(word) == 0:  # O(M)
                suffix: str = target[len(word):]  # O(n-len(word) -> O(M) memory = O(M)
                result = count_construct(suffix, word_bank)
                count_of_constructs += result
        return count_of_constructs


if __name__ == '__main__':
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
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
