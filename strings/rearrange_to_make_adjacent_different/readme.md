# Rearrange To Make Adjacent Different

## Problem Statement

Given a string `s` consisting of lowercase English letters, determine whether it can be rearranged so that no two adjacent characters are the same.

Return **true** if such a rearrangement is possible; otherwise, return **false**.

---

## Example 1

**Input**

```text
aaabc
```

**Output**

```text
true
```

**Explanation**

One possible rearrangement is:

```text
abaca
```

---

## Example 2

**Input**

```text
aaabb
```

**Output**

```text
true
```

**Explanation**

One possible rearrangement is:

```text
ababa
```

---

## Example 3

**Input**

```text
aaaabc
```

**Output**

```text
false
```

**Explanation**

The character `'a'` appears too many times, so it is impossible to rearrange the string without having adjacent `'a'` characters.

---

## Approach

- Count the frequency of each character.
- Find the maximum frequency among all characters.
- A rearrangement is possible only if the maximum frequency does not exceed:

```text
(length of string + 1) // 2
```

- If the maximum frequency is greater than this value, at least two identical characters must be adjacent.

---

