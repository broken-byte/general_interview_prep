from enum import Enum
from functools import lru_cache
from collections import namedtuple


class WinnerIs(Enum):
    DRAW = 0
    MOUSE = 1
    CAT = 2


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        GameState = namedtuple('GameState', ['mouse_position', 'cat_position', 'move_count'])

        @lru_cache(None)
        def dp(current_game_state: GameState) -> WinnerIs:
            # Base Cases
            if current_game_state.mouse_position == 0:
                return WinnerIs.MOUSE
            elif current_game_state.mouse_position == current_game_state.cat_position:
                return WinnerIs.CAT
            elif current_game_state.move_count > 2 * len(graph):
                return WinnerIs.DRAW

            # Recursive Cases
            if current_game_state.move_count % 2 == 0:  # Mouse Moves
                can_draw = False
                for next_position in graph[current_game_state.mouse_position]:
                    next_game_state = GameState(
                        mouse_position=next_position,
                        cat_position=current_game_state.cat_position,
                        move_count=current_game_state.move_count + 1
                    )
                    result = dp(next_game_state)
                    if result == WinnerIs.MOUSE:
                        return WinnerIs.MOUSE
                    elif result == WinnerIs.DRAW:
                        can_draw = True
                if can_draw:
                    return WinnerIs.DRAW
                return WinnerIs.CAT
            else:  # Cat Moves
                can_draw = False
                for next_position in graph[current_game_state.cat_position]:
                    if next_position == 0:
                        continue
                    next_game_state = GameState(
                        mouse_position=current_game_state.mouse_position,
                        cat_position=next_position,
                        move_count=current_game_state.move_count + 1
                    )
                    result = dp(next_game_state)
                    if result == WinnerIs.CAT:
                        return WinnerIs.CAT
                    elif result == WinnerIs.DRAW:
                        can_draw = True
                if can_draw:
                    return WinnerIs.DRAW
                return WinnerIs.MOUSE
        starting_game_state = GameState(1, 2, 0)
        return dp(starting_game_state).value
