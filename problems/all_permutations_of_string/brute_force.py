from typing import List


def permutations(s: str) -> List[str]:
    """
    base case -> permutations('') -> []
    base case -> permutations('a') -> ['s']
    base case -> permutations('ab' -> ['ab', reversed('ab')]

    recursive case -> permutations('abc') -> permutations('ab').map(lambda permutation: permutation +'c' in every crevice)

    Time Complexity: O(n^2*n!) -> O(call_stack*permutation_iterations*interleaving_time_complexity)
    Space Complexity: O(n*n!)
    """
    if s == '':
        return []
    elif len(s) == 1:
        return [s]
    elif len(s) == 2:
        return [s, s[::-1]]
    character_to_interleave: str = s[-1]
    permutations_for_sliced: List[str] = permutations(s[:-1])
    all_interleaved_permutations: List[str] = []
    for perm in permutations_for_sliced:  # (n)
        interleaved_permutations: List[str] = interleave(character_to_interleave, perm)  # O(n!)
        all_interleaved_permutations.extend(interleaved_permutations)
    return all_interleaved_permutations


def interleave(character_to_interleave: str, word: str) -> List[str]:
    interleaved_permutations: List[str] = []
    for i in range(len(word)):
        interleaving: str = word[:i] + character_to_interleave + word[i:]
        interleaved_permutations.append(interleaving)
    return interleaved_permutations


if __name__ == '__main__':
    print(permutations('abcd'))
    print(permutations('abc'))
    print(permutations('ab'))
    print(permutations('a'))
