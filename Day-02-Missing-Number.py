# Day 2 - Missing Number
# LeetCode: https://leetcode.com/problems/missing-number/
# Difficulty: Easy
# Topic: Array, Math
# Approach: Brute Force (Membership Check)
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        for num in range(len(nums) + 1):
            if num not in nums:
                return num
