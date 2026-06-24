# Print All Duplicate Characters in a String

## Problem Statement

Given a string, find all characters that appear more than once and return each character along with its count.

## Example 1

Input:

```text
geeksforgeeks
```

Output:

```text
['e', 4]
['g', 2]
['k', 2]
['s', 2]
```

## Example 2

Input:

```text
programming
```

Output:

```text
['r', 2]
['g', 2]
['m', 2]
```

## Approach

- Create a dictionary to store the frequency of each character.
- Traverse the string and count occurrences.
- Traverse the dictionary and collect characters whose count is greater than 1.
