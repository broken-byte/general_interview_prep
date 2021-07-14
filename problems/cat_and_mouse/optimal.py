from enum import Enum
from functools import lru_cache
from collections import namedtuple


class WinnerIs(Enum):
    DRAW = 0
    MOUSE = 1
    CAT = 2


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:

        @lru_cache(None)
        def dp(mouse_position: int, cat_position: int, move_count: int) -> WinnerIs:
            # Base Cases
            if mouse_position == 0:
                return WinnerIs.MOUSE
            elif mouse_position == cat_position:
                return WinnerIs.CAT
            elif move_count > 2 * len(graph):
                return WinnerIs.DRAW
            # Recursive Cases
            if move_count % 2 == 0:  # Mouse Moves
                can_draw = False
                for next_position in graph[mouse_position]:
                    result = dp(next_position, cat_position, move_count + 1)
                    if result == WinnerIs.MOUSE:
                        return WinnerIs.MOUSE
                    elif result == WinnerIs.DRAW:
                        can_draw = True
                if can_draw:
                    return WinnerIs.DRAW
                return WinnerIs.CAT
            else:  # Cat Moves
                can_draw = False
                for next_position in graph[cat_position]:
                    if next_position == 0:
                        continue
                    result = dp(mouse_position, next_position, move_count + 1)
                    if result == WinnerIs.CAT:
                        return WinnerIs.CAT
                    elif result == WinnerIs.DRAW:
                        can_draw = True
                if can_draw:
                    return WinnerIs.DRAW
                return WinnerIs.MOUSE
        return dp(1, 2, 0).value
