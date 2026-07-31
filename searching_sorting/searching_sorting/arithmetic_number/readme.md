# Arithmetic Number

## Problem Statement

Given three integers:

- `a` → First term of an arithmetic progression (AP)
- `c` → Common difference
- `b` → Number to search

Determine whether `b` exists in the arithmetic progression.

---

## Example 1

**Input**

```text
a = 1
b = 3
c = 2
```

**Output**

```text
true
```

**Explanation**

AP:

```text
1, 3, 5, 7, ...
```

3 is present.

---

## Example 2

**Input**

```text
a = 1
b = 2
c = 3
```

**Output**

```text
false
```

---

## Approach

A number `b` belongs to an arithmetic progression if:

1. `(b - a)` is divisible by `c`.
2. The number of steps from `a` to `b` is non-negative.
3. Handle the special case when `c = 0`.

---

## Algorithm

1. If `a == b`, return `True`.
2. If `c == 0`, return `False`.
3. Compute `diff = b - a`.
4. If `diff % c != 0`, return `False`.
5. If `diff // c >= 0`, return `True`; otherwise `False`.

---

