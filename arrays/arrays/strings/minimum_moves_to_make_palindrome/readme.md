# Minimum Number of Moves to Make Palindrome

## Problem Statement

Given a string `s` consisting of lowercase English letters, find the minimum number of adjacent swaps required to convert the string into a palindrome.

It is guaranteed that the string can always be converted into a palindrome.

## Example 1

Input:

```text
s = "aabb"
```

Output:

```text
2
```

Explanation:

```text
aabb
→ abab  (1 move)
→ abba  (1 move)
```

Total moves = 2

## Example 2

Input:

```text
s = "letelt"
```

Output:

```text
2
```

Explanation:

```text
letelt
→ letetl  (1 move)
→ lettel  (1 move)
```

Total moves = 2

## Approach

I used a Greedy approach.

- Start from the first character.
- Find its matching character from the right side.
- Move the matching character to the end using adjacent swaps.
- Count all swaps performed.
- Remove both matched characters and continue with the remaining string.
- If a character does not have a matching pair, it must be the middle character of the palindrome, so move it one step towards the center.

This guarantees the minimum number of adjacent swaps.

