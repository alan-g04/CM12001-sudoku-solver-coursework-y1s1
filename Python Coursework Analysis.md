## Preamble

The pass mark for this assignment is 40%. It is due on the 5th January.

### Success Criteria

For this part of the assignment, you will need to submit the implementation for an agent which can solve sudoku puzzles:

- You can use any algorithm
- Your code will be subject to automated testing
- Speed of code $\propto$ Higher grade
- Must be compatible with sample tests
- An array of -1 should be returned for invalid puzzles

### Warnings

#### Technical

Failure in following technical instructions can result in a grade of zero.

- Code at the bottom of .ipynb page must run correctly before submission
- Do not modify or delete any of the cells that are marked as test cells, even if they appear to be empty.
- Do not duplicate any cells in the notebook. Insert a new cell and copy over contents.

#### Moral

- Do not copy or work with other students.
- Do not copy online answers.
- Submitting plagiarised work risks your entire place on your degree.

## Choice of algorithm

Evaluate and balance the trade-off between how well suited you think the algorithm is and how difficult it is to write.

Constraint Satisfaction is suggested - a good implementation of a backtracking DFS with CP should achieve around 60-70%.

A successful agent using basic, heuristic, or local search may be easier to implement but will not perform as well.

A high grade requires a particularly efficient implementation of constraint satisfaction, or something beyond the specification.

More than one algorithm can be implemented and included **(where??)** and written about in the **report**, but only code in the notebook will be tested.

### Ideas:

- Backtracking
- Dancing Links (Hulusi?)
- Stochastic Search
- SAT Solver

#### Backtracking

Basic Backtracker:

1. Pick first empty cell
2. Try values in the domain
3. Check whether the choice is valid (numpy slicing?)

#### Dancing Links (Algorithm X)

#### Stochastic Search

#### SAT Solver

#### CSP:

##### Parameters

Variables ($X$): 81 cells
Domain ($D$): The set of values $\{ 1, \dots, 9 \}$ for each variable
Constraints ($C$): All values must be different across rows, columns and $3\times3$ grids.

##### Implementation

Keep track of “legal” domain for each empty cell after each choice.

#### Heuristic:

##### Fail First

Always choose the variable with the smallest remaining domain. (Tiebreaker: Choose variable involved in the largest number of constraints on other unassigned variables.)

##### Fail last

When choosing a value for a cell, pick the one that rules out the fewest choices for the neighbouring cells. This maximises the flexibility for future assignments.

#### Arc Consistency (AC-3)

After every assignment enforce AC.

For every pair of variables $X_{i}, X_{j}$, that share a constraint, you ensure that for every value of the domain of $X_{i}$, there satisfies at least one value in the domain of $X_{j}$.

Solves naked and hidden singles purely through logic sometimes solving easier before.
