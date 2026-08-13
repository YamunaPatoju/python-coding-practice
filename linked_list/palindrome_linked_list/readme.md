# Palindrome Linked List

**Difficulty:** Medium

## Problem Statement

Given the `head` of a singly linked list, determine whether the linked list is a **palindrome**.

A linked list is a palindrome if its elements read the same from left to right and right to left.

## Examples

### Example 1

**Input:**

```text
1 → 2 → 1 → 1 → 2 → 1
```

**Output:**

```text
true
```

The linked list reads the same in both directions.

### Example 2

**Input:**

```text
10 → 20 → 30 → 40 → 50
```

**Output:**

```text
false
```

The linked list is not the same when read backwards.

## Approach

Use the **Slow and Fast Pointer** technique.

1. Find the middle of the linked list using two pointers.
2. Reverse the second half of the linked list.
3. Compare the first half with the reversed second half.
4. If all corresponding values are equal, the linked list is a palindrome.
5. Otherwise, return `False`.

### Why Slow and Fast Pointers?

- `slow` moves one step at a time.
- `fast` moves two steps at a time.
- When `fast` reaches the end, `slow` reaches the middle.

## Algorithm

```text
Find middle
     ↓
Reverse second half
     ↓
Compare both halves
     ↓
Same values?
   /      \
 Yes       No
 ↓          ↓
True      False
```

