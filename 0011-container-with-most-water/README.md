# 0011. Container With Most Water  
**Problem:** [LeetCode - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)  
**Difficulty:** Medium  
**Category:** Two Pointers / Greedy  
**Approach:** Two-Pointer Technique  

---

## 📘 Problem Statement  
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `iᵗʰ` line are at `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container such that the container contains the **most water**.

Return the **maximum amount of water** a container can store.

> **Note:** You may not slant the container.

---

## 🔍 Examples  

**Input:**  
`height = [1,8,6,2,5,4,8,3,7]`  
**Output:**  
`49`  
**Explanation:**  
Lines at index 1 and 8 form the container with the largest area.  
Area = `min(8, 7) * (8 - 1) = 7 * 7 = 49`

**Input:**  
`height = [1,1]`  
**Output:**  
`1`

---

## 📌 Constraints  
- `n == height.length`  
- `2 <= n <= 10⁵`  
- `0 <= height[i] <= 10⁴`

---

## 🧠 Approach  

### 🔧 Two-Pointer Technique  
- Start with two pointers at the beginning and end of the array  
- At each step, calculate the area between the two lines  
- Move the pointer pointing to the **shorter** line inward  
- Track the **maximum area** found  
- Repeat until pointers meet  

Efficient, elegant, and only one pass through the array.

---

## 📈 Time and Space Complexity  

| Metric            | Value   |
|------------------|---------|
| 🕒 Time Complexity | O(n)    |
| 🧠 Space Complexity| O(1)    |

---

## 📁 Files  
- `solution.py` — Python implementation using the two-pointer method  
- `README.md` — This file
