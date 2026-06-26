# Longest Repeating Subsequence

## Problem Statement

Given a string `s`, find the length of the longest subsequence that appears at least twice in the string.

The same character can be used in both subsequences only if it comes from different indices.

## Example 1

**Input:**

```text
s = "axxzxy"
```

**Output:**

```text
2
```

**Explanation:**

The longest repeating subsequence is `"xx"`.

## Example 2

**Input:**

```text
s = "axxxy"
```

**Output:**

```text
2
```

## Approach

- Use Dynamic Programming.
- Compare the string with itself.
- If characters match and their indices are different, increase the subsequence length.
- Otherwise, take the maximum value from the previous computations.
- The final answer is stored in the last cell of the DP table.

