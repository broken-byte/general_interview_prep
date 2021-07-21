

class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    """
    N = Number of Integers in list
    L = Number of Lists in List
    D = Maximum Depth of nested structure
    Time Complexity: O(N + L)

    Space Complexity: O(N + D)
    """
    def __init__(self, nested_list: [NestedInteger]):
        self.flattened_list = self.flatten_list(nested_list)
        self.iterator_cursor = 0

    def flatten_list(self, current_struct: any) -> list[int]:
        # Base
        if type(current_struct) == NestedInteger and current_struct.isInteger():
            return [current_struct.getInteger()]
        # Recursive Case
        results: list[int] = []
        iterable_current_struct = current_struct if type(current_struct) == list else current_struct.getList()
        for list_item in iterable_current_struct:
            result = self.flatten_list(list_item)
            results.extend(result)
        return results

    def next(self) -> int:
        next_item = self.flattened_list[self.iterator_cursor]
        self.iterator_cursor += 1
        return next_item

    def hasNext(self) -> bool:
        return self.iterator_cursor < len(self.flattened_list)


if __name__ == '__main__':
    """
    test = [
        NestedInteger{
            _integer: None, _list: [
                NestedInteger{_integer: 1, _list: []}, 
                NestedInteger{_integer: 1, _list: []}
            ]
        }, 
        NestedInteger{_integer: 2, _list: []}, 
        NestedInteger{
            _integer: None, _list: [
                NestedInteger{_integer: 1, _list: []}, 
                NestedInteger{_integer: 1, _list: []}
            ]
        }
    ]
    """
