# Day 4 - Add Digits
# LeetCode: https://leetcode.com/problems/add-digits/
# Difficulty: Easy
# Topic: Math
# Approach: Repeated Digit Extraction
# Time Complexity: O(log n) per digit-summing round
# Space Complexity: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0

            while num > 0:
                digit = num % 10
                total = total + digit
                num = num // 10

            num = total

        return num
