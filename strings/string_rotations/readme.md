# Strings Rotations of Each Other

## Problem Statement

Given two strings s1 and s2 of equal length, check whether s2 is a rotation of s1.

A string is a rotation of another string if characters can be shifted from the beginning to the end (or vice versa) without changing their order.

## Example 1

Input:

```text
s1 = "abcd"
s2 = "cdab"
```

Output:

```text
true
```

Explanation:

```text
After rotation, "abcd" becomes "cdab".
```

## Example 2

Input:

```text
s1 = "aab"
s2 = "aba"
```

Output:

```text
true
```

## Example 3

Input:

```text
s1 = "abcd"
s2 = "acbd"
```

Output:

```text
false
```

## Approach

- If lengths are different, return False.
- Concatenate s1 with itself.
- If s2 exists inside (s1 + s1), then s2 is a rotation of s1.

