# Stream First Non-Repeating Character

## Problem Statement

Given a string `s` consisting of lowercase English letters, find the first non-repeating character for every prefix of the string.

If no non-repeating character exists for a prefix, append `#`.

## Example

### Input

```text
s = "aabc"
```

### Output

```text
a#bb
```

### Explanation

| Prefix | First Non-Repeating |
|--------|----------------------|
| a | a |
| aa | # |
| aab | b |
| aabc | b |

## Approach

- Use a **queue** to maintain the order of characters.
- Use a **frequency array** to count occurrences of each character.
- For every character in the stream:
  - Increase its frequency.
  - Push it into the queue.
  - Remove characters from the front while their frequency is greater than `1`.
  - The front of the queue is the first non-repeating character.
  - If the queue becomes empty, append `#`.

## Algorithm

1. Create a frequency array of size `26`.
2. Create an empty queue.
3. Traverse the string character by character.
4. Increase the frequency of the current character.
5. Push the current character into the queue.
6. Remove repeating characters from the front of the queue.
7. Append the front character to the answer if the queue is not empty.
8. Otherwise, append `#`.
9. Return the final string.

