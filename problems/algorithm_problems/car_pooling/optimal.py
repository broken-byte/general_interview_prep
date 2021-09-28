

class Solution:
    """
    N = len(trips)
    Time Complexity: O(Nlog(N))
    Space Complexity: O(N)
    """
    def carpooling(self, trips: list[list[int]], capacity: int) -> bool:
        trip_nodes: dict[int: int] = create_trip_node_map(trips)
        car_load = 0
        for _, net_passenger_load in sorted(trip_nodes.items()):
            car_load += net_passenger_load
            if car_load > capacity:
                return False
        return True if car_load == 0 else False


def create_trip_node_map(trips: list[list[int]]) -> dict[int: int]:
    nodes: dict[int: int] = {}
    for num_passengers, first_node, second_node in trips:
        if first_node in nodes:
            nodes[first_node] += num_passengers
        else:
            nodes[first_node] = num_passengers

        if second_node in nodes:
            nodes[second_node] -= num_passengers
        else:
            nodes[second_node] = (-1) * num_passengers
    return nodes

