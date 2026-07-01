# Search Pattern

## Problem Statement

Given a text string `txt` and a pattern string `pat`, return the starting indices (0-based) of all occurrences of `pat` in `txt`.

If the pattern does not occur, return an empty list.

## Example 1

**Input:**

```text
txt = "geeksforgeeks"
pat = "geek"
```

**Output:**

```text
[0, 8]
```

## Example 2

**Input:**

```text
txt = "abesdu"
pat = "edu"
```

**Output:**

```text
[]
```

## Example 3

**Input:**

```text
txt = "aabaacaadaabaaba"
pat = "aaba"
```

**Output:**

```text
[0, 9, 12]
```

## Approach

- Use the Knuth-Morris-Pratt (KMP) algorithm.
- First, build the LPS (Longest Prefix Suffix) array for the pattern.
- Traverse the text using the LPS array to efficiently skip unnecessary comparisons.
- Record every occurrence of the pattern.

