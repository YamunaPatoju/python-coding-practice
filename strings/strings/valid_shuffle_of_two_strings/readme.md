# Check if a String is a Valid Shuffle of Two Distinct Strings

## Problem Statement

Given two strings and a third string, check whether the third string is a valid shuffle of the first two strings.

A valid shuffle contains all characters of both strings while maintaining the relative order of characters from each string.

## Example 1

Input:

```text
first = "XY"
second = "12"
result = "X1Y2"
```

Output:

```text
True
```

## Example 2

Input:

```text
first = "XY"
second = "12"
result = "Y1X2"
```

Output:

```text
False
```

Explanation:

```text
The order of characters in the first string is not maintained.
```

## Approach

- Check if the length of the result string equals the sum of lengths of the first two strings.
- Use three pointers to traverse all strings.
- Compare characters from the first and second strings with the result string.
- If any character does not match, return False.

