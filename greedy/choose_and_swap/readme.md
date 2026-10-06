# Choose and Swap

## Problem

Given a string `s` containing lowercase English letters, we can swap all occurrences of any two distinct characters at most once.

Find the lexicographically smallest string possible after the operation.

## Approach

Use a **Greedy** approach.

1. Store the first occurrence of every character.
2. Scan the string from left to right.
3. For the current character, check whether a smaller character occurs later.
4. If such a character exists, swap all occurrences of the two characters.
5. Return the result immediately.
6. If no beneficial swap exists, return the original string.

The first beneficial swap is enough because lexicographical order depends on the earliest position where the strings differ.

## Algorithm

```text
Store the first occurrence of every character.

For each character from left to right:
    Check all smaller characters.

    If a smaller character occurs later:
        Swap all occurrences of the two characters.
        Return the resulting string.

If no swap is possible:
    Return the original string.
```

## Example 1

### Input

```text
s = "ccad"
```

The character `a` occurs after `c`.

Swap all `c` and `a`:

```text
ccad → aacd
```

### Output

```text
aacd
```


