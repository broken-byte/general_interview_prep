from typing import Set, Tuple


def isIsomorphic(s: str, t: str) -> bool:
    unique_pairs_of_s_and_t: Set[Tuple[int, int]] = set(zip(s, t))
    unique_elements_of_s = set(s)
    unique_elements_of_t = set(t)
    return len(unique_pairs_of_s_and_t) == len(unique_elements_of_s) == len(unique_elements_of_t)


if __name__ == '__main__':
    print(isIsomorphic(s = "egg", t = "add"))
    print(isIsomorphic(s = "foo", t = "bar"))
    print(isIsomorphic(s = "paper", t = "title"))
    print(isIsomorphic("badc", "baba"))
