# Generate IP Addresses

## Problem Statement

Given a string containing only digits, generate all possible valid IP addresses.

A valid IP address:

- Consists of exactly **4 parts** separated by dots (`.`).
- Each part is an integer between **0** and **255**.
- A part cannot have leading zeros unless it is exactly `"0"`.

Return all possible valid IP addresses. If no valid IP address can be formed, return an empty list.

---

## Example 1

**Input**

```text
255678166
```

**Output**

```text
[
"25.56.78.166",
"255.6.78.166",
"255.67.8.166",
"255.67.81.66"
]
```

---

## Example 2

**Input**

```text
25505011535
```

**Output**

```text
[]
```

No valid IP address can be formed.

---

## Approach

- Use **Backtracking** to divide the string into **4 parts**.
- Each part can contain **1 to 3 digits**.
- Before selecting a part, verify:
  - Value is between **0 and 255**.
  - No leading zeros (except `"0"`).
- If exactly four valid parts consume the entire string, join them using dots and store the result.

---
