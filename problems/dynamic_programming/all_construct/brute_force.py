from typing import List


def all_construct(target: str, word_bank: List[str]) -> list:
    """
    M = len(target)
    N = len(word_bank)
    Time Complexity: O(N^M*M^2)
    Space Complexity: O(M^2)
    """
    if target == '':
        return [[]]
    else:
        all_ways_to_construct: List[List[str]] = []
        for word in word_bank:
            if target.find(word) == 0:
                suffix: str = target[len(word):]
                ways_to_construct_suffix: List[List[str]] = all_construct(suffix, word_bank)
                for way in ways_to_construct_suffix:
                    way.append(word)
                all_ways_to_construct.extend(ways_to_construct_suffix)
        return all_ways_to_construct


def log_recursion(recursion_level: int, testable: bool = False, **kwargs) -> str:
    logging_message: str = (f"=============== Recursion Logger ===============\n"
                            f"Recursion level: {recursion_level}\n")
    for parameter, value in kwargs.items():
        logging_message += f"{parameter}: {value}\n"

    if testable:
        return logging_message
    else:
        print(logging_message)


if __name__ == '__main__':
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
    print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'boar']))
    print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
