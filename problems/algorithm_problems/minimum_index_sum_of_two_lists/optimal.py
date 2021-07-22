import heapq


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        """
        N, M = Len(list1), Len(list2)
        Time Complexity: O(N) or ~(2N) due to heap search
        Space Complexity: O(N) or ~(2N) due to dict and min_heap
        """
        results = []
        min_heap = []
        heapq.heapify(min_heap)
        hashed_list_1 = {restaurant: index for index, restaurant in enumerate(list1)}  # O(n)
        for index, restaurant in enumerate(list2):  # O(n)
            if restaurant in hashed_list_1:
                index_sum = index + hashed_list_1[restaurant]
                heapq.heappush(min_heap, (index_sum, restaurant))
        min_sum, restaurant = 0, ""
        if min_heap:
            min_sum, restaurant = heapq.heappop(min_heap)
            results.append(restaurant)
        while min_heap:
            next_min_sum, next_restaurant = heapq.heappop(min_heap)
            if next_min_sum != min_sum:
                break
            results.append(next_restaurant)
        return results


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