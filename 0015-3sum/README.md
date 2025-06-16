## 0015. 3Sum  
**Problem:** [LeetCode - 3Sum](https://leetcode.com/problems/3sum/)  
**Difficulty:** Medium  
**Category:** Two Pointers / Sorting / Hashing  
**Approach:** Two-Pointer + Duplicate Skipping  

---

## 📘 Problem Statement  
Given an integer array `nums`, return *all* the **unique triplets** `[nums[i], nums[j], nums[k]]` such that:

- `i ≠ j`, `i ≠ k`, and `j ≠ k`  
- `nums[i] + nums[j] + nums[k] == 0`  

> **Note:** The solution must not contain **duplicate** triplets.

---

## 🔍 Examples  

**Input:**  
`nums = [-1, 0, 1, 2, -1, -4]`  
**Output:**  
`[[-1, -1, 2], [-1, 0, 1]]`

**Input:**  
`nums = [0, 1, 1]`  
**Output:**  
`[]`

**Input:**  
`nums = [0, 0, 0]`  
**Output:**  
`[[0, 0, 0]]`

---

## 📌 Constraints  
- `3 <= nums.length <= 3000`  
- `-10⁵ <= nums[i] <= 10⁵`

---

## 🧠 Approach  

### 🔧 Two-Pointer + Sorting Strat
