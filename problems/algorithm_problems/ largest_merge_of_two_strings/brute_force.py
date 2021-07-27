

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        """
        N, M = len(word1), len(word2)
        Time Complexity: O(2^(max(N, M)*max(M, N))), for the
        recursive branching and the word slicing cost

        Space Complexity: max(N, M) for recursive call stack

        Algorithm: Classic Dynamic Programming minus caching
        """

        def get_largest_merge(w1: str, w2: str, merge: str) -> str:
            if len(w1) == 0 or len(w2) == 0:
                word_to_be_appended = max([w1, w2], key=len)
                merge += word_to_be_appended
                return merge
            result_from_w1_slice: str = get_largest_merge(
                w1[1:], w2, merge + w1[0]
            )
            result_from_w2_slice: str = get_largest_merge(
                w1, w2[1:], merge + w2[0]
            )
            return max(result_from_w1_slice, result_from_w2_slice)

        return get_largest_merge(word1, word2, "")


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestMerge(word1="cabaa", word2="bcaaa"))
    print(solution.largestMerge(word1="abcabc", word2="abdcaba"))
