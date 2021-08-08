

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """
        Time Complexity: O(N) or ~3N
        Space ComplexityL O(N)
        """
        split_sentence: list = sentence.split(' ')
        final_sentence: list[str] = []
        for index, word in enumerate(split_sentence):
            goat_word = goatify_word(word, index)
            final_sentence.append(goat_word)
        return " ".join(final_sentence)


def goatify_word(word: str, index: int) -> str:
    vowels: set = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    if word[0] in vowels:
        word += "ma"
    else:
        word += word[0] + "ma"
        word = word[1:]
    return word + "".join(['a' for _ in range(index + 1)])


if __name__ == '__main__':
    solution = Solution()
    print(goatify_word("I", 0))
    print(solution.toGoatLatin("I speak Goat Latin"))
    print(solution.toGoatLatin("The quick brown fox jumped over the lazy dog"))
    print("heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
    print(solution.toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
