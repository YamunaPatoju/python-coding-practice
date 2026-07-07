# Min Number of Flips

## Problem Statement

Given a binary string `s`, determine the minimum number of bit flips required to make the string alternate between `0` and `1`.

Two possible alternating patterns are:
- `010101...`
- `101010...`

Return the minimum number of flips required.

---

## Example 1

**Input**

```text
s = "001"
```

**Output**

```text
1
```

**Explanation**

Flip the first bit to get:

```text
101
```

---

## Example 2

**Input**

```text
s = "0001010111"
```

**Output**

```text
2
```

---

## Approach

- There are only two valid alternating patterns:
  - Start with `0`
  - Start with `1`
- Traverse the string once.
- Count mismatches with both patterns.
- Return the smaller mismatch count.

---
