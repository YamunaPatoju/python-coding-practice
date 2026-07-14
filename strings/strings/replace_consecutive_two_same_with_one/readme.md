# Replace Consecutive Two Same with One

## Problem Statement

Given a string `s` consisting of lowercase English letters, remove all consecutive duplicate characters.

Return the modified string after removing adjacent duplicate characters.

---

## Example 1

**Input**

```text
aabb
```

**Output**

```text
ab
```

**Explanation**

The consecutive duplicate characters are removed.

---

## Example 2

**Input**

```text
aabaa
```

**Output**

```text
aba
```

**Explanation**

Only adjacent duplicate characters are removed.

---

## Example 3

**Input**

```text
aaaa
```

**Output**

```text
a
```

**Explanation**

All consecutive `'a'` characters are reduced to a single `'a'`.

---

## Approach

- Start by adding the first character to the result.
- Traverse the string from left to right.
- If the current character is different from the previous character, append it to the result.
- Ignore consecutive duplicate characters.
- Join the characters to form the final string.

---
