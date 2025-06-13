# Longest Substring Without Repeating Characters

**Problem:** [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
**Difficulty:** Medium  
**Tags:** Sliding Window, Hash Table, String

---

## 🧠 Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

---

## 🧪 Example

**Input:** `"abcabcbb"`  
**Output:** `3`  
**Explanation:** The answer is `"abc"`, with the length of 3.

---

## 🚀 Approach

- Use the **sliding window** technique with two pointers (`left`, `right`)
- Use a `set` or `dict` to track characters in the current window
- Slide the window while maintaining the constraint: no repeating characters

---

## 🧮 Time & Space Complexity

- **Time Complexity:** `O(n)` – Each character is processed at most twice.
- **Space Complexity:** `O(min(n, m))` – `m` is the size of the character set.
