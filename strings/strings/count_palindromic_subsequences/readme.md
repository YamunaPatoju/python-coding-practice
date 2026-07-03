# Count Palindromic Subsequences

## Problem Statement

Given a string `s`, count the total number of palindromic subsequences present in it. The subsequences need not be distinct.

## Example 1

**Input:**

```text
s = "abcd"
```

**Output:**

```text
4
```

## Example 2

**Input:**

```text
s = "aab"
```

**Output:**

```text
4
```

## Example 3

**Input:**

```text
s = "b"
```

**Output:**

```text
1
```

## Approach

- Use Dynamic Programming.
- Let `dp[i][j]` represent the number of palindromic subsequences in the substring `s[i...j]`.
- If the first and last characters are equal:

```text
dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
```
- Otherwise:
```text
dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
```
- The final answer is `dp[0][n-1]`.

