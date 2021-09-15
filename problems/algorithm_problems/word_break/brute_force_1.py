from functools import lru_cache


class Solution:
    """
    N = len(s)
    M = len(wordDict)
    Time Complexity: O(M^N)
    Space Complexity: O(N)

    LRU Cache does not significantly
    speed up execution time due to
    there not being many repeated
    sub problems with this implementation :/
    """
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        @lru_cache(None)
        def can_word_build_to_original_string(built_string: str) -> bool:
            if len(built_string) > len(s):
                return False
            elif s == built_string:
                return True
            for word in wordDict:
                concatenated_string: str = built_string + word
                if can_word_build_to_original_string(concatenated_string):
                    return True
            return False

        return can_word_build_to_original_string("")


def get_string_after_slicing(string_to_slice: str, start_slice: int, end_slice) -> str:
    left: str = string_to_slice[:start_slice]
    right: str = string_to_slice[end_slice:]
    return left + right


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(solution.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
    print(solution.wordBreak(
        "bccdbacdbdacddabbaaaadababadad",
        [
            "cbc", "bcda", "adb", "ddca", "bad", "bbb", "dad", "dac", "ba", "aa", "bd", "abab", "bb", "dbda", "cb", "caccc", "d", "dd", "aadb", "cc", "b", "bcc", "bcd", "cd",
            "cbca", "bbd", "ddd", "dabb", "ab", "acd", "a", "bbcc", "cdcbd", "cada", "dbca", "ac", "abacd", "cba", "cdb", "dbac", "aada", "cdcda", "cdc", "dbc", "dbcb", "bdb",
            "ddbdd", "cadaa", "ddbc", "babb"
        ]
    ))
