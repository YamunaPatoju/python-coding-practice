# Transform String

## Problem Statement

Given two strings `s1` and `s2`, find the minimum number of operations required to transform `s1` into `s2`.

The only allowed operation is:

- Pick any character from `s1` and insert it at the beginning of the string.

If the transformation is not possible, return `-1`.

---

## Example 1

**Input**

```text
s1 = "abd"
s2 = "bad"
```

**Output**

```text
1
```

**Explanation**

Move `'b'` to the front.

```text
abd → bad
```

---

## Example 2

**Input**

```text
s1 = "GeeksForGeeks"
s2 = "ForGeeksGeeks"
```

**Output**

```text
3
```

**Explanation**

Move:

```text
r → front
o → front
F → front
```

Total operations = **3**

---

## Approach

1. If the lengths of the strings are different, return `-1`.
2. Check whether both strings contain the same characters with the same frequencies.
   - If not, transformation is impossible.
3. Traverse both strings from the end.
4. If characters match, move both pointers.
5. Otherwise, move only the pointer of `s1` and increment the operation count.
6. Return the total number of operations.

---

