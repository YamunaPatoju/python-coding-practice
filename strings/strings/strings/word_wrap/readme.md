# Word Wrap

## Problem Statement

Given an array `arr[]` where `arr[i]` represents the length of the ith word and an integer `k` representing the maximum line width, arrange the words into lines such that the total cost is minimized.

The cost of a line is the square of the extra spaces left at the end of the line. The last line has zero cost.

## Example 1

**Input:**

```text
arr = [3,2,2,5]
k = 6
```

**Output:**

```text
10
```

## Example 2

**Input:**

```text
arr = [3,2,2]
k = 4
```

**Output:**

```text
5
```

## Approach

- Use Dynamic Programming.
- Let `dp[i]` represent the minimum cost to arrange words from index `i` to the end.
- Try placing words `i...j` on the same line until the line width exceeds `k`.
- Compute the extra spaces and update the minimum cost.
- The last line contributes zero cost.

