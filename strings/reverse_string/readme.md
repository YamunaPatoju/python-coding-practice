# Reverse String

## Problem Statement

Given an array of characters, reverse the array in-place.

The solution should use O(1) extra space.

## Example 1

Input:

```text
["h","e","l","l","o"]
```

Output:

```text
["o","l","l","e","h"]
```

## Example 2

Input:

```text
["H","a","n","n","a","h"]
```

Output:

```text
["h","a","n","n","a","H"]
```

## Approach

I use two pointers:

- One pointer starts from the beginning.
- Another pointer starts from the end.

Swap both characters and move the pointers towards the center.

Continue until both pointers meet.

This reverses the string without using extra space.


```
