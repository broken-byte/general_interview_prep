from enum import Enum
from functools import lru_cache


class GameState(Enum):
    DRAW = 0
    MOUSE_WINS = 1
    CAT_WINS = 2


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        """
        Time Complexity: O(n^3)
        --------------------
        Without Memoization:
            O(N*N^(2^N)), due to recursive call tree is N^2N, for all N nodes
        With Memoization:
            Recursive call stack is: O(N^2), for all N Nodes, hence:
                - O(N^2*N) -> O(n^3)

        Space Complexity:
            O(n^2), for cache of recursive call stack
        """

        @lru_cache(None)
        def get_game_state(mouse_position: int, cat_position: int, move_count: int) -> GameState:
            # Base Cases
            if mouse_position == 0:
                return GameState.MOUSE_WINS
            elif mouse_position == cat_position:
                return GameState.CAT_WINS
            elif move_count > 2 * len(graph):
                return GameState.DRAW
            # Recursive Cases
            if move_count % 2 == 0:  # Mouse Moves
                can_draw = False
                for next_position in graph[mouse_position]:
                    next_game_state = get_game_state(next_position, cat_position, move_count + 1)
                    if next_game_state == GameState.MOUSE_WINS:
                        return GameState.MOUSE_WINS
                    elif next_game_state == GameState.DRAW:
                        can_draw = True
                if can_draw:
                    return GameState.DRAW
                return GameState.CAT_WINS
            else:  # Cat Moves
                can_draw = False
                for next_position in graph[cat_position]:
                    if next_position == 0:
                        continue
                    next_game_state = get_game_state(mouse_position, next_position, move_count + 1)
                    if next_game_state == GameState.CAT_WINS:
                        return GameState.CAT_WINS
                    elif next_game_state == GameState.DRAW:
                        can_draw = True
                if can_draw:
                    return GameState.DRAW
                return GameState.MOUSE_WINS
        return get_game_state(1, 2, 0).value
