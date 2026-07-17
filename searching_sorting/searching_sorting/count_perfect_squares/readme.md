# Count Perfect Squares

## Problem Statement

Given a positive integer `n`, count the number of perfect squares that are **strictly less than** `n`.

A perfect square is a number that can be expressed as the square of an integer.

---

## Example 1

**Input**

```text
n = 9
```

**Output**

```text
2
```

**Explanation**

The perfect squares less than `9` are:

```text
1, 4
```

So, the answer is:

```text
2
```

---

## Example 2

**Input**

```text
n = 3
```

**Output**

```text
1
```

**Explanation**

The only perfect square less than `3` is:

```text
1
```

---

## Approach

The largest perfect square less than `n` is obtained by taking the integer square root of `n - 1`.

Use `math.isqrt()` to directly compute this value.

For example:

```text
n = 26

Perfect squares:
1, 4, 9, 16, 25

Answer = isqrt(25) = 5
```

---

## Algorithm

1. Compute `n - 1`.
2. Find the integer square root using `math.isqrt()`.
3. Return the result.

---

