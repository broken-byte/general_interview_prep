

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        """
        N, M = Len(list1), Len(list2)
        Time Complexity: O(N) or ~(N)
        Space Complexity: O(N) or ~(N) due to dict
        """
        hashed_list_1 = {restaurant: index for index, restaurant in enumerate(list1)}
        min_sum, result = float('inf'), []
        for j, restaurant in enumerate(list2):
            i = hashed_list_1.get(restaurant, float('inf'))
            if i + j < min_sum:
                min_sum = i + j
                # reset result state to new minimum
                result = [restaurant]
            elif i + j == min_sum:
                result.append(restaurant)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRestaurant(
        list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
        list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    ))
    print(solution.findRestaurant(
        list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
        list2=["KFC", "Shogun", "Burger King"]
    ))
    print(solution.findRestaurant(
        list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
        list2=["KFC", "Burger King", "Tapioca Express", "Shogun"]
    ))
