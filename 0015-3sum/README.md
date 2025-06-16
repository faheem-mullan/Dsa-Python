0015. 3Sum
Problem: LeetCode - 3Sum
Difficulty: Medium
Category: Two Pointers / Sorting / Hashing
Approach: Two-Pointer + Duplicate Skipping

📘 Problem Statement
Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] such that:

i ≠ j, i ≠ k, and j ≠ k

nums[i] + nums[j] + nums[k] == 0

Note: The solution must not contain duplicate triplets.

🔍 Examples
Input:
nums = [-1, 0, 1, 2, -1, -4]
Output:
[[-1, -1, 2], [-1, 0, 1]]

Input:
nums = [0, 1, 1]
Output:
[]

Input:
nums = [0, 0, 0]
Output:
[[0, 0, 0]]

📌 Constraints
3 <= nums.length <= 3000

-10⁵ <= nums[i] <= 10⁵

🧠 Approach
🔧 Two-Pointer + Sorting Strategy
Sort the array

Fix one number at a time, and use a two-pointer approach for the rest

Skip duplicates to avoid repeated triplets

If the sum is less than zero, move left pointer up

If the sum is greater than zero, move right pointer down

If zero, record it and move both pointers while skipping duplicates

📈 Time and Space Complexity
Metric	Value
🕒 Time Complexity	O(n²)
🧠 Space Complexity	O(1) (ignoring output list)

📁 Files
solution.py — Python implementation using sorting + two-pointer technique

README.md — This file

