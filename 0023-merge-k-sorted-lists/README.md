# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/submissions/2201994605/)

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red?style=flat-square)
![Language: python3](https://img.shields.io/badge/Language-python3-blue?style=flat-square)
![Runtime](https://img.shields.io/badge/Runtime-N%2FA-success?style=flat-square)
![Memory](https://img.shields.io/badge/Memory-N%2FA-informational?style=flat-square)


### Topics
`Linked List` `Divide and Conquer` `Heap (Priority Queue)` `Merge Sort` `Tournament Sort`

---

### Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

**Example 1:**

```
**Input:** lists = [[1,4,5],[1,3,4],[2,6]]
**Output:** [1,1,2,3,4,4,5,6]
**Explanation:** The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```

**Example 2:**

```
**Input:** lists = []
**Output:** []
```

**Example 3:**

```
**Input:** lists = [[]]
**Output:** []
```

**Constraints:**

- `k == lists.length`
	
- `0 <= k <= 10^4`
	
- `0 <= lists[i].length <= 500`
	
- `-10^4 <= lists[i][j] <= 10^4`
	
- `lists[i]` is sorted in **ascending order**.
	
- The sum of `lists[i].length` will not exceed `10^4`.

---

*Solved on Nov 23, 2026 using **LeetCommit**.*
