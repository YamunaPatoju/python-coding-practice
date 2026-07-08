# Minimum Swaps for Bracket Balancing

## Problem Statement

Given a string consisting of an equal number of `'['` and `']'` brackets, determine the minimum number of adjacent swaps required to make the string balanced.

A balanced string satisfies proper opening and closing bracket order.

---

## Example 1

**Input**

```text
[]][][
```

**Output**

```text
2
```

**Explanation**

Two adjacent swaps are sufficient to balance the brackets.

---

## Example 2

**Input**

```text
[][]
```

**Output**

```text
0
```

The string is already balanced.

---

## Example 3

**Input**

```text
[[[][][]]]
```

**Output**

```text
0
```

---

## Approach

- Traverse the string from left to right.
- Maintain:
  - `open_brackets` = number of unmatched `'['`
  - `imbalance` = number of unmatched `']'`
- When `'['` is encountered:
  - Increase `open_brackets`.
  - If there is an imbalance, swap it with a previous unmatched `']'`.
- When `']'` is encountered:
  - Match it with an available `'['` if possible.
  - Otherwise, increase the imbalance.
- The accumulated swaps give the minimum adjacent swaps required.

---

