# Balanced Splits of a Binary String

## Problem Statement

Given a binary string `s`, split it into the maximum number of substrings such that each substring contains an equal number of `0`s and `1`s.

If it is not possible, return `-1`.

## Example 1

**Input:**

```text
s = "0100110101"
```

**Output:**

```text
4
```

**Explanation:**

Possible splits:

```text
01 | 0011 | 01 | 01
```

## Example 2

**Input:**

```text
s = "0111100010"
```

**Output:**

```text
3
```

## Example 3

**Input:**

```text
s = "0010"
```

**Output:**

```text
-1
```

## Approach

- Traverse the string once.
- Count the number of `0`s and `1`s.
- Whenever both counts become equal, one balanced substring is found.
- If the total number of `0`s and `1`s are unequal after traversal, return `-1`.

