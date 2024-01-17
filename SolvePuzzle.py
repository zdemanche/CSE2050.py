def solve_puzzle(board):
    """
    Solves a puzzle given a board with specific rules.

    Args:
        board (list): A list representing the puzzle board.

    Returns:
        tuple: A tuple containing the optimal path (list of indices) and the minimum number of moves (int).
    """
    def solve_recursive(current_tile, moves, visited):
        """
        Recursively solves the puzzle by exploring possible moves.

        Args:
            current_tile (int): The current position on the board.
            moves (int): The number of moves taken so far.
            visited (list): A list indicating visited positions on the board.

        Returns:
            tuple: A tuple containing the optimal path (list of indices) and the minimum number of moves (int).
        """
        if current_tile < 0 or current_tile >= len(board) or visited[current_tile]:
            return None, float('inf')
        
        if current_tile == len(board) - 1:
            return [current_tile], moves

        visited[current_tile] = True

        forward_move = solve_recursive(current_tile + board[current_tile], moves + 1, visited[:])
        backward_move = solve_recursive(current_tile - board[current_tile], moves + 1, visited[:])

        visited[current_tile] = False

        if forward_move[1] < backward_move[1]:
            return [current_tile] + (forward_move[0] if forward_move[0] is not None else []), forward_move[1]
        else:
            return [current_tile] + (backward_move[0] if backward_move[0] is not None else []), backward_move[1]  

    visited = [False] * len(board)
    optimal_path, min_moves = solve_recursive(0, 0, visited)

    if min_moves == float('inf'):
        return None, None

    return optimal_path, min_moves

# Example usage:
L = [1, 3, 10, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1]
optimal_path, min_moves = solve_puzzle(L)
print("Optimal Path:", optimal_path)
print("Minimum Moves:", min_moves)
