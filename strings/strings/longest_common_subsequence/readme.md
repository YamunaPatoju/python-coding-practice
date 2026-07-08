# Longest Common Subsequence (LCS)

## Problem Statement

Given two strings `s1` and `s2`, find the length of their **Longest Common Subsequence (LCS)**.

A subsequence is obtained by deleting zero or more characters without changing the order of the remaining characters.

If no common subsequence exists, return `0`.

---

## Example 1

**Input**

```text
s1 = "ABCDGH"
s2 = "AEDFHR"
```

**Output**

```text
3
```

**Explanation**

The longest common subsequence is:

```text
ADH
```

Length = **3**

---

## Example 2

**Input**

```text
s1 = "ABC"
s2 = "AC"
```

**Output**

```text
2
```

**Explanation**

```text
AC
```

---

## Example 3

**Input**

```text
s1 = "XYZW"
s2 = "XYWZ"
```

**Output**

```text
3
```

Possible LCS:

```text
XYZ
```

or

```text
XYW
```

---

## Approach

- Use Dynamic Programming.
- Create a DP table where `dp[i][j]` represents the length of the LCS between:
  - First `i` characters of `s1`
  - First `j` characters of `s2`
- If the current characters match:
  - Add `1` to the previous diagonal value.
- Otherwise:
  - Take the maximum of the top and left cells.
- The answer is stored in the bottom-right cell.

---
