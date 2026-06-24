# Palindrome String

## Problem Statement

Given a string `s`, check whether it is a palindrome.

A string is called a palindrome if it reads the same from left to right and right to left.

Return `true` if the string is a palindrome, otherwise return `false`.

## Example 1

Input:

```text
s = "abba"
```

Output:

```text
true
```

Explanation:

```text
"abba" is the same when read from both directions.
```

## Example 2

Input:

```text
s = "abc"
```

Output:

```text
false
```

Explanation:

```text
"abc" and "cba" are different.
```

## Approach

I use two pointers:

- One starts from the beginning of the string.
- Another starts from the end.

If characters at both positions are different, the string is not a palindrome.

If all matching characters are equal, the string is a palindrome.
