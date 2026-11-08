# Day 3 - Middle of the Linked List
# LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: Easy
# Topic: Linked List, Two Pointers
# Approach: Slow and Fast Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
