# Quick Sort on Linked List

## Problem Statement

Given the head of a singly linked list, sort the linked list in non-decreasing order using the **Quick Sort** algorithm and return the head of the sorted list.

---

## Example 1

### Input

```text
8 → 2 → 9 → 5
```

### Output

```text
2 → 5 → 8 → 9
```

---

## Example 2

### Input

```text
30 → 10 → 60 → 40 → 20 → 50
```

### Output

```text
10 → 20 → 30 → 40 → 50 → 60
```

---

## Approach

Quick Sort works by selecting a **pivot** and partitioning the linked list into three parts:

```text
Less    → values smaller than pivot
Equal   → values equal to pivot
Greater → values greater than pivot
```

Then recursively sort the `less` and `greater` lists and combine them:

```text
Less → Equal → Greater
```

---

## Algorithm

1. If the list is empty or contains one node, return it.
2. Select the first node's value as the pivot.
3. Traverse the linked list.
4. Divide nodes into:
   - `less`
   - `equal`
   - `greater`
5. Recursively sort `less`.
6. Recursively sort `greater`.
7. Join the three lists.
8. Return the resulting head.

---

