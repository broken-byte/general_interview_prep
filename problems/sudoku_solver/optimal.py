from math import floor


def sudoku_can_be_solved(board: list) -> bool:
    # For each empty cell, consider 'newCandidates', the
    # set of possible candidate values that can
    # be placed into that cell.

    row = -1
    col = -1
    candidates = None

    for r in range(0, 8):
        for c in range(0, 8):
            if board[r][c] == '.':
                new_candidates = get_candidates(board, r, c)
                # Then, we want to keep the smallest
                # sized 'newCandidates', plus remember the
                # position where it was found
                if candidates is None or len(new_candidates) < len(candidates):
                    candidates = new_candidates
                    row = r
                    col = c

    # If we have not found any empty cell, then
    # the whole board is filled already
    if candidates is None:
        return True

    # For each possible value that can be placed
    # in position (row, col), let's
    # place that value and then recursively query
    # whether the board can be solved.  If it can,
    # we are done.
    for val in candidates:
        board[row][col] = val
        if sudoku_can_be_solved(board):
            return True
        # The tried value val didn't work so restore
        # the (row, col) cell back to '.'
        board[row][col] = '.'

    # Otherwise, there is no value that can be placed
    # into position (row, col) to make the
    # board solved
    return False


# A helper function that returns a set of all valid
# candidates for a given cell in the board
def get_candidates(board: list, row: int, col: int):
    # For some empty cell board[row][col], what possible
    # characters can be placed into this cell
    # that aren't already placed in the same row,
    # column, and sub-board?

    # At the beginning, we don't have any candidates
    candidates = []

    # For each character add it to the candidate list
    # only if there's no collision, i.e. that character
    # doesn't already exist in the same row, column
    # and sub-board. Notice the top-left corner of (row, col)'s
    # sub-board is (row - row%3, col - col%3).
    for char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        collision = False
        for i in range(0, 8):
            if (board[row][i] == char or
                    board[i][col] == char or
                    board[(row - row % 3) + floor(i / 3)][(col - col % 3) + i % 3] == char):
                collision = True
                break

        if not collision:
            candidates.append(char)

    return candidates
