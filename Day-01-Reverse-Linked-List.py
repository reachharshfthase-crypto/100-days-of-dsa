# Day 1 - Reverse Linked List
# LeetCode: https://leetcode.com/problems/reverse-linked-list/
# Topic: Linked List
# Approach: Iterative (Three Pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
