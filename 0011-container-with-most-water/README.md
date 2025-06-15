# 0009. Palindrome Number  
**Problem:** LeetCode - Palindrome Number  
**Difficulty:** Easy  
**Category:** Math  
**Approach:** Integer Reversal / String Conversion  

---

## 📘 Problem Statement  
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.  

A palindrome is a number that reads the same forward and backward.

---

## 🔍 Examples  

**Input:**  
`x = 121`  
**Output:**  
`true`  
**Explanation:**  
121 reads the same forward and backward.

**Input:**  
`x = -121`  
**Output:**  
`false`  
**Explanation:**  
From left to right, it reads -121. From right to left, it becomes 121-. Not the same.

---

## 📌 Constraints  
- `-2³¹ <= x <= 2³¹ - 1`

---

## 🧠 Approach  

### 🔄 Method 1: String Conversion  
- Convert integer to string  
- Compare string with its reverse  

### 🔁 Method 2: Integer Reversal (No string usage)  
- Reverse half of the digits and compare  
- More optimal for low-level performance, avoids type conversion

---

## 📈 Time and Space Complexity  

| Method         | Time Complexity | Space Complexity |
|----------------|------------------|-------------------|
| String Method  | O(n)             | O(n)              |
| Int Reversal   | O(log₁₀n)        | O(1)              |

---

## 📁 Files  
- `solution.py` — Contains both string-based and optimized integer-based solution  
- `README.md` — This file
