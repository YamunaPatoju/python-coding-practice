# Print Anagrams Together

## Problem Statement

Given an array of strings, group together all strings that are anagrams of each other.

Two strings are anagrams if they contain the same characters with the same frequencies, possibly in a different order.

The strings within each group should appear in the same order as they occur in the input array.

Return a 2D array where each inner array represents one group of anagrams.

---

## Example 1

**Input**

```text
["act", "god", "cat", "dog", "tac"]
```

**Output**

```text
[
["act", "cat", "tac"],
["god", "dog"]
]
```

---

## Example 2

**Input**

```text
["no", "on", "is"]
```

**Output**

```text
[
["no", "on"],
["is"]
]
```

---

## Example 3

**Input**

```text
["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
```

**Output**

```text
[
["listen", "silent", "enlist"],
["abc", "cab", "bac"],
["rat", "tar", "art"]
]
```

---

## Approach

- Create a hash map where:
  - **Key** = Sorted version of the string.
  - **Value** = List of all strings having the same sorted characters.
- Traverse the input array:
  - Sort each word to create its key.
  - Append the original word to the corresponding group.
- Return all groups stored in the hash map.

Since all anagrams produce the same sorted string, they naturally belong to the same group.

---
