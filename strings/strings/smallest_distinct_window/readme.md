# Smallest Distinct Window

## Problem Statement

Given a string `s`, find the length of the smallest substring that contains every distinct character present in the original string at least once.

---

## Example 1

**Input**

```text
aabcbcdbca
```

**Output**

```text
4
```

**Explanation**

The smallest valid window is:

```text
dbca
```

---

## Example 2

**Input**

```text
aaab
```

**Output**

```text
2
```

**Explanation**

```text
ab
```

contains both distinct characters.

---

## Example 3

**Input**

```text
geeksforgeeks
```

**Output**

```text
7
```

One valid smallest window is:

```text
eksforg
```

---

## Approach

- Count the total number of distinct characters in the string.
- Use the **Sliding Window** technique with two pointers.
- Expand the right pointer until all distinct characters are included.
- Then shrink the left pointer while maintaining all distinct characters.
- Keep updating the minimum window length.

---

