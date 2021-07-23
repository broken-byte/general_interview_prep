

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """
        N = len(arr)
        Time Complexity: O(Nlog(N)) or ~(Nlog(N) + 2N)
        Space Complexity: O(N) or ~ 2N
        """
        index_counter: {str: list[int]} = create_counter_dict_with_original_indices(arr)
        sorted_arr = sorted(arr)
        rank = 1
        previously_encountered = set()
        for element in sorted_arr:
            if element in previously_encountered:
                continue
            original_indices = index_counter[element]
            for original_index in original_indices:
                arr[original_index] = rank
            rank += 1
            previously_encountered.add(element)
        return arr


def create_counter_dict_with_original_indices(arr: list[int]) -> dict:
    counter_with_original_indices: {str: list[int]} = {}
    for index, element in enumerate(arr):
        if element in counter_with_original_indices:
            counter_with_original_indices[element].append(index)
        else:
            counter_with_original_indices[element] = [index]
    return counter_with_original_indices


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrayRankTransform([100, 100, 100]))
