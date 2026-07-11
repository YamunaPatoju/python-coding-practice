# Smallest Window Containing All Characters

## Problem Statement

Given two strings `s` and `p`, find the smallest substring in `s` that contains all the characters of `p`, including duplicate characters.

If multiple windows of the same minimum length exist, return the one with the smallest starting index.

If no such window exists, return an empty string.

---

## Example 1

**Input**

```text
s = "timetopractice"
p = "toc"
```

**Output**

```text
toprac
```

**Explanation**

The substring `"toprac"` is the smallest window containing the characters `t`, `o`, and `c`.

---

## Example 2

**Input**

```text
s = "zoomlazapzo"
p = "oza"
```

**Output**

```text
apzo
```

---

## Example 3

**Input**

```text
s = "zoom"
p = "zooe"
```

**Output**

```text
""
```

**Explanation**

The character `'e'` is not present in `s`, so no valid window exists.

---

## Approach

- Count the frequency of each character in `p`.
- Use the **Sliding Window** technique with two pointers.
- Expand the right pointer until all required characters are included.
- Shrink the left pointer while the window remains valid to obtain the minimum-length window.
- Keep track of the smallest valid window found.

---
