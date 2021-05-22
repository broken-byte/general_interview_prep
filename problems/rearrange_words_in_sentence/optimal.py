

class Solution:
    def arrangeWords(self, text: str) -> str:
        """
        n = number of words
        Time Complexity: O(log(n!))
        Space Complexity: O(n)

        Python uses a sorting algorithm called TimSort, which utilizes
        already sorted original orderings, thus fulfilling the
        criteria of original ordering for equal length strings
        """
        sorted_indexed_text = sorted(text.split(" "), key=len)
        return " ".join(sorted_indexed_text).lower().capitalize()
