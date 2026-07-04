# Word in Grid - All Occurrences

## Problem Statement

Given a 2D grid of characters and a word, find all starting positions where the word occurs.

Rules:
- The word can be searched in any of the 8 directions:
  - Up
  - Down
  - Left
  - Right
  - Top-Left
  - Top-Right
  - Bottom-Left
  - Bottom-Right
- Once a direction is chosen, it cannot change.
- Return all unique starting coordinates in lexicographical order.

## Example 1

**Input:**

```text
mat =
a b a b
a b e b
e b e b

word = "abe"
```

**Output:**

```text
[[0,0], [0,2], [1,0]]
```

## Example 2

**Input:**

```text
mat =
G E E K S F O R G E E K S
G E E K S Q U I Z G E E K
I D E Q A P R A C T I C E

word = "GEEKS"
```

**Output:**

```text
[[0,0], [0,8], [1,0]]
```

## Approach

- Traverse every cell in the grid.
- If the first character matches the word's first character:
  - Check all 8 possible directions.
  - Move in the selected direction while characters continue matching.
- If the complete word is matched, add the starting position.
- Stop checking other directions for that starting cell after the first successful match.

