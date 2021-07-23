

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """
        N = len(arr)
        Time Complexity: O(NLog(N)) or ~(Nlog(N) + 2N)
        Space Complexity: O(N) or ~(2N) for ranks dict and results list

        This is more optimal, however, given that our dict is not
        storing an array in every hash like in the previous solution
        """
        result = sorted(arr)
        ranks: {str: int} = {}
        rank = 1
        for element in result:
            if element in ranks:
                continue
            ranks[element] = rank
            rank += 1
        for index in range(len(arr)):
            result[index] = ranks[arr[index]]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrayRankTransform([100, 100, 100]))
