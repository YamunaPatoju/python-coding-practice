# Roman to Integer

## Problem Statement

Given a Roman numeral string, convert it into its corresponding integer value.

Roman numeral symbols:

| Symbol | Value |
|--------|------:|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Roman numerals use subtraction in specific cases:

- IV = 4
- IX = 9
- XL = 40
- XC = 90
- CD = 400
- CM = 900

---

## Example 1

**Input**

```text
IX
```

**Output**

```text
9
```

---

## Example 2

**Input**

```text
XL
```

**Output**

```text
40
```

---

## Example 3

**Input**

```text
MCMIV
```

**Output**

```text
1904
```

---

## Approach

- Create a dictionary storing the value of each Roman symbol.
- Traverse the string from left to right.
- Compare the current symbol with the next symbol:
  - If the current value is smaller than the next value, subtract it.
  - Otherwise, add it.
- Finally, add the value of the last symbol.

---
