# Add 1 to a Linked List Number

## Problem Statement

Given a linked list where each node contains a single digit, the digits together represent a number.

Add `1` to the number and return the modified linked list.

---

## Example 1

### Input

```text
4 → 5 → 6
```

The number is:

```text
456
```

After adding 1:

```text
457
```

### Output

```text
4 → 5 → 7
```

---

## Example 2

### Input

```text
1 → 2 → 3
```

The number is:

```text
123
```

After adding 1:

```text
124
```

### Output

```text
1 → 2 → 4
```

---

## Example 3

### Input

```text
9 → 9 → 9
```

The number is:

```text
999
```

After adding 1:

```text
1000
```

### Output

```text
1 → 0 → 0 → 0
```

---

## Approach

The addition starts from the **last digit**, but a singly linked list can only be traversed from left to right.

So:

1. Reverse the linked list.
2. Add `1` starting from the first node.
3. Handle the carry.
4. Reverse the linked list again.

---

## Algorithm

1. Reverse the linked list.
2. Set `carry = 1`.
3. Traverse the reversed list.
4. For each node:
   - Add the carry to the digit.
   - Store `total % 10`.
   - Update carry using `total // 10`.
5. If carry remains, create a new node.
6. Reverse the linked list again.
7. Return the new head.

---

