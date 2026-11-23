# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/2202004432/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=flat-square)
![Language: python3](https://img.shields.io/badge/Language-python3-blue?style=flat-square)
![Runtime](https://img.shields.io/badge/Runtime-N%2FA-success?style=flat-square)
![Memory](https://img.shields.io/badge/Memory-N%2FA-informational?style=flat-square)


### Topics
`Two Pointers` `String` `String Matching` `Z Algorithm` `Knuth–Morris–Pratt Algorithm` `Boyer–Moore String-Search Algorithm`

---

### Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**

```
**Input:** haystack = "sadbutsad", needle = "sad"
**Output:** 0
**Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

**Example 2:**

```
**Input:** haystack = "leetcode", needle = "leeto"
**Output:** -1
**Explanation:** "leeto" did not occur in "leetcode", so we return -1.
```

**Constraints:**

- `1 <= haystack.length, needle.length <= 10^4`
	
- `haystack` and `needle` consist of only lowercase English characters.

---

*Solved on Nov 23, 2026 using **LeetCommit**.*
