# Intersection Sorted Linked Lists

## Problem Statement

Given two linked lists sorted in increasing order, create a new linked list containing the intersection of both lists.

The original linked lists must not be modified.

Duplicate elements are allowed.

---

## Example 1

### Input

```text
LinkedList1 = 1 → 2 → 3 → 4 → 6
LinkedList2 = 2 → 4 → 6 → 8
```

### Output

```text
2 → 4 → 6
```

---

## Example 2

### Input

```text
LinkedList1 = 10 → 20 → 40 → 50
LinkedList2 = 15 → 40
```

### Output

```text
40
```

---

## Approach

Both linked lists are sorted, so we can use two pointers.

- If both values are equal, add the value to the new list and move both pointers.
- If the value in the first list is smaller, move the first pointer.
- Otherwise, move the second pointer.

A new node is created for every intersection value, so the original lists remain unchanged.

---

## Algorithm

1. Create a dummy node for the result list.
2. Set pointers to the heads of both lists.
3. While both pointers are not `None`:
   - If both values are equal:
     - Create a new node.
     - Add it to the result.
     - Move both pointers.
   - If the first value is smaller:
     - Move the first pointer.
   - Otherwise:
     - Move the second pointer.
4. Return `dummy.next`.

---

