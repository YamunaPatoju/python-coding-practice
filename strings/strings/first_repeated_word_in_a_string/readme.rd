# Find the First Repeated Word in a String

## Problem Statement

Given a sentence, find the first word that repeats in the string.

If no word repeats, return **"No Repetition"**.

---

## Example 1

**Input**

```text
Ravi had been saying that he had been there
```

**Output**

```text
had
```

---

## Example 2

**Input**

```text
Ravi had been saying that
```

**Output**

```text
No Repetition
```

---

## Example 3

**Input**

```text
he had had he
```

**Output**

```text
he
```

---

## Approach

- Split the sentence into words.
- Traverse the words from right to left.
- Store visited words in a set.
- If a word is already present in the set, update it as the answer.
- After traversal, return the answer.
- If no repeated word exists, return `"No Repetition"`.

---

