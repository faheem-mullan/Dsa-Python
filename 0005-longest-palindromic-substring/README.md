# Longest Palindromic Substring

**Problem:** [LeetCode #5](https://leetcode.com/problems/longest-palindromic-substring/)  
**Difficulty:** Medium  
**Tags:** String, Dynamic Programming, Expand Around Center

---

## 🧠 Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

---

## 🧪 Example

**Input:** `"babad"`  
**Output:** `"bab"` or `"aba"`  
**Explanation:** Both are valid palindromes of length 3.

---

## 🚀 Approach

- Use the **expand around center** technique.
- Consider each character (and the gap between characters) as the center of a palindrome.
- Expand outward while the characters on both sides are equal.
- Keep track of the longest palindrome found.

---

## 🧮 Time & Space Complexity

- **Time Complexity:** `O(n²)` – We expand from each of the `2n - 1` possible centers.
- **Space Complexity:** `O(1)` – Constant space if no dynamic programming table is used.
