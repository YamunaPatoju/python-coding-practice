# Word Search - Count Occurrences with 4 Directions

## Problem Statement

Given a 2D grid of characters and a string `word`, count the total number of occurrences of the word in the grid.

Rules:
- Movement is allowed only in four directions: Up, Down, Left, and Right.
- The path may bend at 90° turns.
- A cell can be used only once in a single occurrence.

## Example 1

**Input:**

```text
mat = [
['S','N','B','S','N'],
['B','A','K','E','A'],
['B','K','B','B','K'],
['S','E','B','S','E']
]

word = "SNAKES"
```

**Output:**

```text
3
```

## Example 2

**Input:**

```text
mat = [
['c','a','t'],
['a','p','c'],
['t','t','a']
]

word = "cat"
```

**Output:**

```text
3
```

## Approach

- Traverse every cell in the matrix.
- Start a Depth First Search (DFS) whenever the first character of the word matches.
- If the current character does not match or the cell is out of bounds, return `0`.
- If the last character of the word is matched, return `1`.
- Mark the current cell as visited to avoid revisiting it in the same path.
- Explore all four directions recursively.
- Restore the cell while backtracking.
- Sum all valid occurrences.
