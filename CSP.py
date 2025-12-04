import numpy as np

def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.
    
    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.
            
    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    
    # Convert to Python list of lists for faster indexing during recursion
    grid = sudoku.tolist()
    
    if not is_initial_state_valid(grid):
         return np.full((9, 9), -1)
    
    if solve_csp(grid):
        return np.array(grid)
    else:
        return np.full((9, 9), -1)

def is_initial_state_valid(grid):
    """Checks if the starting grid violates any rules immediately."""
    for r in range(9):
        for c in range(9):
            val = grid[r][c]
            if val != 0:
                grid[r][c] = 0 # Temp remove to check validity
                if not is_safe(grid, r, c, val):
                    return False
                grid[r][c] = val # Restore
    return True

def find_best_empty_cell(grid):
    """
    MRV Heuristic: Follows fail-first principle by selecting the empty cell
    with the fewest valid choices.
    Returns: (row, col, valid_choices_set) or (None, None, None) if full.
    """
    best_cell = None
    min_options = 10  # Max possible is 9
    best_candidates = None
    
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                candidates = get_candidates(grid, r, c)
                count = len(candidates)
                
                if count == 0:
                    # Unsolvable
                    return -1, -1, None
                
                if count < min_options:
                    min_options = count
                    best_cell = (r, c)
                    best_candidates = candidates
                    
                    # One option left, return immediately
                    if count == 1:
                        return r, c, candidates
                        
    if best_cell is None:
        return None, None, None # Solved
        
    return best_cell[0], best_cell[1], best_candidates

def get_candidates(grid, r, c):
    """Returns a set of valid numbers for cell (r, c)."""
    candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    # Remove values in ...
    # Row
    for val in grid[r]:
        candidates.discard(val)
        
    # Col
    for i in range(9):
        candidates.discard(grid[i][c])
        
    # Box
    start_r, start_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(start_r, start_r + 3):
        for j in range(start_c, start_c + 3):
            candidates.discard(grid[i][j])
            
    return candidates

def is_safe(grid, row, col, num):
    """Checks if placing num at grid[row][col] is valid."""
    # Check ...
    # Row
    if num in grid[row]: return False

    # Col
    for r in range(9):
        if grid[r][col] == num: return False

    # Box
    start_r, start_c = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_r, start_r + 3):
        for j in range(start_c, start_c + 3):
            if grid[i][j] == num: return False

    return True

def solve_csp(grid):
    """Recursive CSP solver with MRV."""
    # Select unassigned variable using MRV
    row, col, candidates = find_best_empty_cell(grid)
    
    # Solved
    if row is None:
        return True
        
    # Unsolvable
    if row == -1:
        return False
    
    # Try each candidate
    for val in candidates:
        grid[row][col] = val
        
        if solve_csp(grid):
            return True
            
        # Backtrack
        grid[row][col] = 0
        
    return False