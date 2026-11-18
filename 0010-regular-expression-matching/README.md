# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/submissions/2198866224/)

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red?style=flat-square)
![Language: python3](https://img.shields.io/badge/Language-python3-blue?style=flat-square)
![Runtime](https://img.shields.io/badge/Runtime-N%2FA-success?style=flat-square)
![Memory](https://img.shields.io/badge/Memory-N%2FA-informational?style=flat-square)


### Topics
`String` `Dynamic Programming` `Recursion`

---

### Description

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

- `'.'` Matches any single character.​​​​
	
- `'*'` Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

**Example 1:**

```
**Input:** s = "aa", p = "a"
**Output:** false
**Explanation:** "a" does not match the entire string "aa".
```

**Example 2:**

```
**Input:** s = "aa", p = "a*"
**Output:** true
**Explanation:** '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3:**

```
**Input:** s = "ab", p = ".*"
**Output:** true
**Explanation:** ".*" means "zero or more (*) of any character (.)".
```

**Constraints:**

- `1 <= s.length <= 20`
	
- `1 <= p.length <= 20`
	
- `s` contains only lowercase English letters.
	
- `p` contains only lowercase English letters, `'.'`, and `'*'`.
	
- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

---

*Solved on Nov 18, 2026 using **LeetCommit**.*
