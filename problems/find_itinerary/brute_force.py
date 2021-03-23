from typing import List
from collections import defaultdict


def brute_force(tickets: List[List[str]]) -> list:
    itinerary_finder = ItineraryFinder(tickets)
    return itinerary_finder.find_itinerary()


class ItineraryFinder:

    def __init__(self, tickets: List[List[str]]):
        self.tickets: List[List[str]] = tickets
        self.graph: dict = defaultdict(list)
        self.itinerary: list = []
        self.num_flights = len(tickets)
        self.visit_bit_map: dict = {}

    def find_itinerary(self) -> List[str]:
        """
        Time Complexity: O(Total Flights^(max number of flights from a given airport))
        Space Complexity: O(number of flights + number of airports)
        """
        self.graph = self.create_itinerary_graph()
        self.backtrack_traversal('JFK', ['JFK'])
        return self.itinerary

    def create_itinerary_graph(self) -> dict:
        itinerary_graph: dict = defaultdict(list)
        for airport, destination in self.tickets:
            itinerary_graph[airport].append(destination)
        for airport, destinations in itinerary_graph.items():
            destinations.sort()
            self.visit_bit_map[airport] = [False] * len(destinations)

        return itinerary_graph

    def backtrack_traversal(self, airport: str, route: list) -> bool:
        if len(route) == self.num_flights + 1:
            self.itinerary = route
            return True
        for i, next_destination in enumerate(self.graph[airport]):
            if not self.visit_bit_map[airport][i]:
                self.visit_bit_map[airport][i] = True
                was_a_valid_path: bool = self.backtrack_traversal(next_destination, route + [next_destination])
                self.visit_bit_map[airport][i] = False
                if was_a_valid_path:
                    return True
        return False


if __name__ == '__main__':
    tickets = [
        ["MUC", "LHR"],
        ["JFK", "MUC"],
        ["SFO", "SJC"],
        ["LHR", "SFO"]
    ]
    print(brute_force(tickets))


