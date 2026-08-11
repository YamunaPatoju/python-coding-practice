# Merge Sort for Linked List

## Problem Statement

Given the head of a singly linked list, sort the linked list in non-decreasing order using the **Merge Sort** algorithm.

Return the head of the sorted linked list.

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

Merge Sort follows the **Divide and Conquer** technique.

For a linked list:

1. Find the middle node using the **slow and fast pointer** technique.
2. Split the list into two halves.
3. Recursively sort both halves.
4. Merge the two sorted halves.

Unlike arrays, linked lists can be split and merged efficiently using pointer manipulation without shifting elements.

---

## Algorithm

1. If the list contains zero or one node, return `head`.
2. Use `slow` and `fast` pointers to find the middle.
3. Split the list into two parts.
4. Recursively apply Merge Sort to both parts.
5. Merge the two sorted lists.
6. Return the merged list.

---

