# Multiply Two Linked Lists

## Problem Statement

Given two singly linked lists where each node contains a single digit, find the product of the two numbers represented by the linked lists.

The digits are stored from most significant digit to least significant digit.

Since the result can be very large, return the answer modulo `10^9 + 7`.

## Example

### Input

```text
L1 = 3 -> 2
L2 = 2
```

### Output

```text
64
```

### Explanation

```text
32 × 2 = 64
```

## Approach

- Traverse the first linked list and construct its number digit by digit.
- Traverse the second linked list and construct its number digit by digit.
- Apply modulo `10^9 + 7` during construction to prevent the numbers from becoming extremely large.
- Multiply the two resulting values.
- Return the product modulo `10^9 + 7`.

## Algorithm

1. Initialize `num1 = 0` and `num2 = 0`.
2. Traverse the first linked list:
   - Update the number using `num1 = num1 * 10 + data`.
   - Apply modulo.
3. Traverse the second linked list similarly.
4. Calculate the product of `num1` and `num2`.
5. Return the product modulo `10^9 + 7`.

