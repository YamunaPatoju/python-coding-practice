# Unoccupied Computers

## Problem Statement

A café has `n` computers. A string `s` represents customer events using uppercase English letters.

- The **first occurrence** of a character represents the customer's arrival.
- The **second occurrence** represents the customer's departure.

When a customer arrives:

- If a computer is available, they are assigned one.
- Otherwise, they are rejected and never use a computer.

Return the number of customers who could not get a computer.

---

## Example 1

**Input**

```text
n = 3
s = "GACCBDDBAGEE"
```

**Output**

```text
1
```

**Explanation**

Customer **D** arrives when all computers are occupied and is rejected.

---

## Example 2

**Input**

```text
n = 1
s = "ABCBAC"
```

**Output**

```text
2
```

**Explanation**

Customers **B** and **C** cannot get a computer.

---

## Approach

Maintain two sets:

- **inside** → Customers currently using a computer.
- **rejected** → Customers who were rejected.

Also maintain:

- `free` → Number of available computers.
- `ans` → Number of rejected customers.

For every event:

1. If it is the customer's first occurrence:
   - Assign a computer if available.
   - Otherwise, mark the customer as rejected.
2. If the customer is currently inside:
   - Free the computer.
3. If the customer was rejected:
   - Ignore their departure by removing them from the rejected set.

---
