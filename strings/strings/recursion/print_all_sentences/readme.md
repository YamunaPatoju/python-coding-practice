# Recursively Print All Sentences from Word Lists

## Problem Statement

Given a list of word lists, generate all possible sentences by selecting exactly one word from each list.

The order of the lists must remain the same.

---

## Example

**Input**

```text
[
    ["you", "we"],
    ["have", "are"],
    ["sleep", "eat", "drink"]
]
```

**Output**

```text
you have sleep
you have eat
you have drink
you are sleep
you are eat
you are drink
we have sleep
we have eat
we have drink
we are sleep
we are eat
we are drink
```

---

## Approach

This problem can be solved using **Backtracking (Depth-First Search)**.

1. Start with the first list.
2. Choose one word.
3. Recursively choose one word from the next list.
4. Continue until a word has been chosen from every list.
5. Print the completed sentence.
6. Backtrack and try the next possible word.

---

