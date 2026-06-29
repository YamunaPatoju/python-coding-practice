# Edit Distance

## Problem Statement

Given two strings `s1` and `s2`, find the minimum number of operations required to convert `s1` into `s2`.

Allowed operations:
- Insert a character
- Delete a character
- Replace a character

## Example 1

**Input:**

```text
s1 = "geek"
s2 = "gesek"
```

**Output:**

```text
1
```

**Explanation:**

Insert `'s'` between the two `'e'` characters.

## Example 2

**Input:**

```text
s1 = "gfg"
s2 = "gfg"
```

**Output:**

```text
0
```

## Example 3

**Input:**

```text
s1 = "abcd"
s2 = "bcfe"
```

**Output:**

```text
3
```

## Approach

- Use Dynamic Programming.
- Let `dp[i][j]` represent the minimum operations needed to convert the first `i` characters of `s1` into the first `j` characters of `s2`.
- If characters match, no new operation is needed.
- Otherwise, take the minimum among:
  - Insert
  - Delete
  - Replace
