# Longest Common Prefix

## Problem Statement

Given an array of strings, find the longest common prefix shared by all the strings.

If there is no common prefix, return an empty string.

---

## Example 1

**Input**

```text
["flower","flow","flight"]
```

**Output**

```text
"fl"
```

---

## Example 2

**Input**

```text
["dog","racecar","car"]
```

**Output**

```text
""
```

---

## Approach

- Assume the first string is the common prefix.
- Compare it with every other string.
- While the current string does not start with the prefix, remove the last character from the prefix.
- If the prefix becomes empty, return an empty string.
- After processing all strings, the remaining prefix is the answer.

---
