

class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return False

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return 0

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return []


class NestedIterator:
    """
    N = Number of Integers in list
    L = Number of Lists in list

    Time Complexity:
    -------------------------------------------------------------------
        self.__init__(): O(N + L)
        self._make_top_element_an_integer(): O(L/N) or O(1)

            - To analyze the TC here, we need to amortize the cost
              across all calls to this function. Once the stack is
              exhausted, the function in question must have processed
              every integer, and every list, so the total cost is
              O(N + L).

              The total number of calls to the function in question is
              the total number of integers in the list, O(N).

              So, the amortized cost is:
              (N + l) / N -> N/N + N/L -> 1 + N + L -> O(N/L)
        self.next(): same as ^^^
        self.hasNext(): same as ^^^

    Space Complexity:
    -------------------------------------------------------------------
        O(N + L)
    """
    def __init__(self, nested_list: [NestedInteger]):
        self.stack: list[NestedInteger] = []
        self.stack.extend(reversed(nested_list))

    def next(self) -> int:
        self._make_top_element_an_integer()
        top_integer: NestedInteger = self.stack.pop()
        return top_integer.getInteger()

    def hasNext(self) -> bool:
        self._make_top_element_an_integer()
        return len(self.stack) > 0

    def _make_top_element_an_integer(self) -> None:
        while not self.empty() and not self._top_element_is_integer():
            nested_list: NestedInteger = self.stack.pop()
            self.stack.extend(reversed(nested_list.getList()))

    def empty(self) -> bool:
        return len(self.stack) == 0

    def _top_element_is_integer(self) -> bool:
        return self.stack[-1].isInteger()
