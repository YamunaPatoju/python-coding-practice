# Longest Palindrome in a String

## Problem Statement

Given a string s, find the longest palindromic substring.

If multiple palindromes have the same maximum length, return the first one.

## Example 1

Input:

```text
forgeeksskeegfor
```

Output:

```text
geeksskeeg
```

## Example 2

Input:

```text
Geeks
```

Output:

```text
ee
```

## Example 3

Input:

```text
abc
```

Output:

```text
a
```

## Approach

- Treat every character as the center of a palindrome.
- Expand in both directions while characters match.
- Check for:
  - Odd length palindromes
  - Even length palindromes
- Keep track of the longest palindrome found.
