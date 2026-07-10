# Min Chars to Add for Palindrome

## Problem Statement

Given a string `s`, find the minimum number of characters that must be added at the **front** of the string to make it a palindrome.

A palindrome is a string that reads the same forwards and backwards.

---

## Example 1

**Input**

```text
abc
```

**Output**

```text
2
```

**Explanation**

Add `"cb"` at the front:

```text
cbabc
```

---

## Example 2

**Input**

```text
aacecaaaa
```

**Output**

```text
2
```

**Explanation**

Add `"aa"` at the front:

```text
aaaacecaaaa
```

---

## Approach

- Reverse the string.
- Create a new string:

```text
original + "$" + reverse
```

- Compute the **LPS (Longest Prefix Suffix)** array using the KMP algorithm.
- The last value of the LPS array gives the length of the longest palindromic prefix.
- The answer is:

```text
length of string − longest palindromic prefix
```

---

