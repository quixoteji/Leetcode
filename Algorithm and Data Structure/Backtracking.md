# Backtracking

## Defination

Backtracking is an approach to solving constraint-satisfaction problems without trying all possiblilities.

## Typical Problems

1. Eight-Queens
2. Map Coloring
3. No Equal Adjacent Substrings
4. Solve Sudoku
5. Maze Solving
6. Kirkman Problem

## Python Codes

```python
def solver(values, safe_up_to, size) :
    """ Finds a solution to a backtracking problem.
    values  -- a sequence of values to try, in order. For a map coloring problem, this may be a list of colors, such as ['red', 'green', 'yellow']
    safe_up_to  -- a function with two arguments, solution and position, that returns whether the values assigned to slots 0 .. pos in the solution list, satisfy the problem constraints.
    size    -- the total number of "slots" you are trying to fill

    Return the solutions as a list of values.
    """
    solutions = [None] * size
    def extend_solution(position) :
        for value in values :
            solutions[position] = value
            if safe_up_to(solution, position) :
                if position >= size - 1 or extend_solution(position + 1) :
                    return solution
        return None
    return extend_solution(0)
```