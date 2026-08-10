# Intersection in Y Shaped Lists

## Problem Statement

Given two singly linked lists that intersect at some node, find and return the node where the two lists first intersect.

The two lists form a **Y shape** because after the intersection point, both lists share the same nodes.

---

## Example 1

### Input

```text
List 1: 10 → 15 → 30
List 2: 3 → 6 → 9 → 15 → 30
```

The common part is:

```text
15 → 30
```

### Output

```text
15
```

---

## Example 2

### Input

```text
List 1: 4 → 1 → 8 → 5
List 2: 5 → 6 → 1 → 8 → 5
```

The common part is:

```text
1 → 8 → 5
```

### Output

```text
1
```

---

## Approach

Use two pointers, `p1` and `p2`.

Both pointers traverse their respective lists.

When a pointer reaches the end of its list, move it to the head of the other list.

```text
p1: List1 → List2
p2: List2 → List1
```

Because both pointers travel the same total distance, they will meet at the intersection node.

---

## Algorithm

1. Set:
   ```text
   p1 = head1
   p2 = head2
   ```
2. Move both pointers one node at a time.
3. When `p1` reaches `None`, move it to `head2`.
4. When `p2` reaches `None`, move it to `head1`.
5. Continue until:
   ```text
   p1 == p2
   ```
6. Return `p1`.

---

