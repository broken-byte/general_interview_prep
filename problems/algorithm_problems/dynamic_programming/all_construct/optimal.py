from typing import List


def all_construct(target: str, word_bank: List[str]) -> list:
    """
    M = len(target)
    N = len(word_bank)
    Time Complexity: O(N*M^3) for specific cases,
        (many repeated sub problems)
        However, most of the time,
        we must traverse all the way down most paths,
        as they represent a unique way to construct.
        Therefore, our Time Complexity here should be:
        O(N^M)
    Space Complexity: O(M^2)
    """
    memo: dict = {}

    def all_construct_recursively(target_word: str) -> list:
        if target_word in memo:
            return memo[target_word]
        elif target_word == '':
            return [[]]
        all_ways_to_construct: List[List[str]] = []
        for word in word_bank:
            if word_at_beginning_of_target_word(word, target_word):
                suffix: str = target_word[len(word):]
                ways_to_construct_suffix: List[List[str]] = all_construct_recursively(suffix)
                ways_to_construct_target_word: List[List[str]] = add_word_to_every_way_of_constructing(word, ways_to_construct_suffix)
                all_ways_to_construct.extend(ways_to_construct_target_word)
        memo[target_word] = all_ways_to_construct
        return all_ways_to_construct

    return all_construct_recursively(target)


def word_at_beginning_of_target_word(word: str, target: str) -> bool:
    return target.find(word) == 0


def add_word_to_every_way_of_constructing(word: str, ways_of_constructing: List[List[str]]) -> List[List[str]]:
    ways_to_construct_plus_word: List[List[str]] = list(map(
        lambda way: way + [word],
        ways_of_constructing
    ))
    return ways_to_construct_plus_word


if __name__ == '__main__':
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
    print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'boar']))
    print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
