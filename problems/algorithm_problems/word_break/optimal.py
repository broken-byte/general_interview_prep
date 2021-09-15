from functools import lru_cache


class Solution:
    """
    Time Complexity: O(N^2*N)  # For every index, we can at worst check to the end, times substring cost
    Space Complexity: O(N)
    """
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        word_dict = set(wordDict)

        @lru_cache(None)
        def can_split_at(start_index: int) -> bool:
            if start_index == len(s):
                return True
            possible_ending_indices = range(start_index + 1, len(s) + 1)
            for end_index in possible_ending_indices:
                prefix: str = s[start_index:end_index]
                if prefix in word_dict and can_split_at(start_index=end_index):
                    return True
            return False

        return can_split_at(0)


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
