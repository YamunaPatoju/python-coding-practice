# Add Number Linked Lists

## Problem Statement

Given two singly linked lists representing two non-negative integers, find their sum and return the result as a linked list.

The input lists may contain leading zeros, but the output must not contain leading zeros.

---

## Example 1

### Input

```text
1 → 2 → 3
9 → 9 → 9
```

The numbers are:

```text
123 + 999 = 1122
```

### Output

```text
1 → 1 → 2 → 2
```

---

## Example 2

### Input

```text
6 → 3
7
```

The numbers are:

```text
63 + 7 = 70
```

### Output

```text
7 → 0
```

---

## Approach

Addition starts from the last digit, but a singly linked list starts from the first digit.

Therefore:

1. Reverse both linked lists.
2. Add corresponding digits from right to left.
3. Maintain a `carry`.
4. Create nodes for the result.
5. Reverse the result list.
6. Remove leading zeros from the result.

---

## Algorithm

1. Reverse `head1`.
2. Reverse `head2`.
3. Initialize:
   ```text
   carry = 0
   ```
4. Traverse both lists.
5. Calculate:
   ```text
   total = digit1 + digit2 + carry
   ```
6. Store:
   ```text
   total % 10
   ```
7. Update:
   ```text
   carry = total // 10
   ```
8. Continue until both lists and carry are exhausted.
9. Reverse the result.
10. Remove leading zeros.
11. Return the result.

---

