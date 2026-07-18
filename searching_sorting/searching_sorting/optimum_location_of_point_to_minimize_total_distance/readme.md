# Optimum Location of Point to Minimize Total Distance

## Problem Statement

Given a line of the form:

```text
ax + by + c = 0
```

and a set of `N` points, find a point lying on the given line such that the **sum of Euclidean distances** from this point to all the given points is minimum.

Return the minimum total distance rounded to **2 decimal places**.

---

## Example 1

**Input**

```text
L = [1, -1, -3]

Points = [
    [-3, 2],
    [-1, 0],
    [-1, 2],
    [1, 2],
    [3, 4]
]
```

**Output**

```text
20.77
```

**Explanation**

The optimum point on the line is approximately:

```text
(2, -1)
```

The minimum possible total distance is:

```text
20.77
```

---

## Example 2

**Input**

```text
L = [2, 1, 4]

Points = [
    [-1, 2],
    [1, 3],
    [2, 4]
]
```

**Output**

```text
11.20
```

---

## Approach

The total distance function is **convex** for a point moving along a straight line.

Therefore, **Ternary Search** can efficiently find the minimum.

1. Express every point on the line using one variable.
2. Compute the total distance from this point to every given point.
3. Apply ternary search on the variable.
4. Continue until the interval becomes very small.
5. Return the minimum distance.

---

## Algorithm

1. Read coefficients `a`, `b`, and `c`.
2. Define a function to calculate the total distance from a point on the line.
3. Perform ternary search on the line.
4. Return the minimum distance rounded to two decimal places.

---

