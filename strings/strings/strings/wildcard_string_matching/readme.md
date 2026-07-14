# Wildcard String Matching

## Problem Statement

Given two strings:

- `wild` (may contain `*` and `?`)
- `pattern` (contains only lowercase letters)

Determine whether `wild` can be matched with `pattern`.

Rules:

- `?` matches exactly one character.
- `*` matches any sequence of characters, including an empty string.

Return `True` if the strings match, otherwise return `False`.

---

## Example 1

**Input**

```text
wild = "ge*ks"
pattern = "geeks"
```

**Output**

```text
True
```

**Explanation**

`*` matches `"e"`.

---

## Example 2

**Input**

```text
wild = "ge?ks*"
pattern = "geeksforgeeks"
```

**Output**

```text
True
```

**Explanation**

`?` matches `'e'` and `*` matches `"forgeeks"`.

---

## Example 3

**Input**

```text
wild = "a*b"
pattern = "acbd"
```

**Output**

```text
False
```

---

## Approach

Use the **Greedy Two-Pointer Algorithm**.

Maintain:

- `i` → pointer for `wild`
- `j` → pointer for `pattern`
- `star` → last position of `*`
- `match` → position in the pattern corresponding to the last `*`

Steps:

1. If characters match or `?` is encountered, move both pointers.
2. If `*` is encountered, store its position and continue.
3. On mismatch:
   - If a previous `*` exists, backtrack to it and let it match one more character.
   - Otherwise, return `False`.
4. After processing the pattern, skip any remaining `*` in the wildcard.
5. Match succeeds only if the wildcard is fully consumed.

---

