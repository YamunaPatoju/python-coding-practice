# Isomorphic Strings

## Problem Statement

Given two strings `s1` and `s2` consisting of lowercase English letters and having the same length, determine whether they are **isomorphic**.

Two strings are isomorphic if:

- Every character in `s1` maps to exactly one character in `s2`.
- No two different characters in `s1` map to the same character in `s2`.
- A character may map to itself.

Return `true` if the strings are isomorphic; otherwise, return `false`.

---

## Example 1

**Input**

```text
s1 = "aab"
s2 = "xxy"
```

**Output**

```text
true
```

**Explanation**

```text
a → x
b → y
```

The mapping is consistent.

---

## Example 2

**Input**

```text
s1 = "aab"
s2 = "xyz"
```

**Output**

```text
false
```

**Explanation**

The character `a` maps to both `x` and `y`, which is not allowed.

---

## Example 3

**Input**

```text
s1 = "abc"
s2 = "xxz"
```

**Output**

```text
false
```

**Explanation**

Characters `a` and `b` both map to `x`.

---

## Approach

- Use two hash maps:
  - One maps characters from `s1` to `s2`.
  - The other maps characters from `s2` to `s1`.
- Traverse both strings together.
- If an existing mapping conflicts, return `false`.
- Otherwise, store the new mapping.
- If the traversal completes successfully, return `true`.

---


```text
O(n)
```

where `n` is the length of the strings.

---

## Space Complexity

```text
O(1)
```

At most 26 lowercase English letters are stored in the hash maps.

---

## Python Code

```python
class Solution:
    def areIsomorphic(self, s1, s2):

        map1 = {}
        map2 = {}

        for c1, c2 in zip(s1, s2):

            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                map1[c1] = c2

            if c2 in map2:
                if map2[c2] != c1:
                    return False
            else:
                map2[c2] = c1

        return True
```
