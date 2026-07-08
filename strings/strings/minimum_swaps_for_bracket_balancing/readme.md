# Minimum Swaps for Bracket Balancing

## Problem Statement

Given a string consisting of an equal number of `'['` and `']'` brackets, find the minimum number of **adjacent swaps** required to make the string balanced.

A balanced string is one in which every opening bracket has a matching closing bracket in the correct order.

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

```text
[]][][
   ↑ swap
[][]][
     ↑ swap
[][][]
```

Total swaps = **2**

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

Already balanced.

---

## Approach

- Store the indices of every `'['` in an array.
- Traverse the string while maintaining the current balance:
  - `'['` increases the balance.
  - `']'` decreases the balance.
- Whenever the balance becomes negative:
  - Swap the current `']'` with the next available `'['`.
  - Add the distance between them to the answer.
  - Restore the balance.

This guarantees the minimum number of adjacent swaps.

---

