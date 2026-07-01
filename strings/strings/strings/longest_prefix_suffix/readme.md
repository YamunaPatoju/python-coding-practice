# Longest Prefix Suffix

## Problem Statement

Given a string `s`, find the length of the longest proper prefix which is also a suffix.

A proper prefix or suffix cannot be equal to the entire string.

## Example 1

**Input:**

```text
s = "abab"
```

**Output:**

```text
2
```

## Example 2

**Input:**

```text
s = "aabcdaabc"
```

**Output:**

```text
4
```

## Example 3

**Input:**

```text
s = "aaaa"
```

**Output:**

```text
3
```

## Approach

- Use the KMP (Knuth-Morris-Pratt) preprocessing algorithm.
- Build the LPS (Longest Prefix Suffix) array.
- The last value of the LPS array represents the length of the longest proper prefix that is also a suffix.
