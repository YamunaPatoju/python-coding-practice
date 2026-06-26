# All Subsequences of a String

## Problem Statement

Given a string `s`, generate all possible subsequences of the string (including the empty subsequence) and return them in lexicographical order.

A subsequence is formed by deleting zero or more characters without changing the order of the remaining characters.

## Example 1

**Input:**

```text
s = "abc"
```

**Output:**

```text
["", "a", "ab", "abc", "ac", "b", "bc", "c"]
```

## Example 2

**Input:**

```text
s = "aa"
```

**Output:**

```text
["", "a", "a", "aa"]
```

## Approach

- Use recursion (backtracking).
- For each character, we have two choices:
  - Include it in the current subsequence.
  - Exclude it from the current subsequence.
- When we reach the end of the string, store the generated subsequence.
- Finally, sort all subsequences in lexicographical order.
