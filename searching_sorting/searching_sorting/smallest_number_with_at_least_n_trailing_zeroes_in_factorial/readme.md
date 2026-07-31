# Smallest Number with At Least N Trailing Zeroes in Factorial

## Problem Statement

Given an integer `n`, find the smallest positive integer `x` such that `x!` contains **at least `n` trailing zeroes**.

---

## Example 1

**Input**

```text
n = 6
```

**Output**

```text
25
```

**Explanation**

```text
25! ends with 6 trailing zeroes.
```

It is the smallest such number.

---

## Example 2

**Input**

```text
n = 1
```

**Output**

```text
5
```

---

## Approach

The number of trailing zeroes in a factorial depends on the number of factors of **5**.

Trailing zeroes in `x!` are calculated as:

```text
x/5 + x/25 + x/125 + ...
```

Since the number of trailing zeroes increases monotonically with `x`, we can use **Binary Search**.

---

## Algorithm

1. Set:
   - `low = 1`
   - `high = 5 × n`
2. Perform Binary Search.
3. For each middle value:
   - Count trailing zeroes in `mid!`.
4. If trailing zeroes are at least `n`:
   - Search on the left.
5. Otherwise:
   - Search on the right.
6. Return the smallest valid number.

---

