#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (69.13%)
# Likes:    2139
# Dislikes: 72
# Total Accepted:    305.1K
# Total Submissions: 441.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a non-empty, singly linked list with head node head, return a middle
# node of linked list.
# 
# If there are two middle nodes, return the second middle node.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is
# [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
# = NULL.
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second
# one.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given list will be between 1 and 100.
# 
# 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
        
# @lc code=end

