#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (35.44%)
# Likes:    11053
# Dislikes: 2656
# Total Accepted:    1.8M
# Total Submissions: 5.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
# 
#
from ds_linkedlist import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        root = item = ListNode()
        r = 0
        while l1 or l2 or r:
            if l1:
                r += l1.val
                l1 = l1.next
            if l2:
                r += l2.val
                l2 = l2.next
            val = r % 10
            r = r // 10
            item.next = ListNode(val)
            item = item.next
        return root.next

    def naive(self, l1, l2):
        res = None
        head = None
        r = 0
        while l1 is not None and l2 is not None:
            if res:
                res.next = ListNode((l1.val+l2.val+r) % 10)
                res = res.next
            else:
                res = ListNode((l1.val+l2.val+r) % 10)
                head = res
            r = (l1.val+l2.val+r) // 10
            l1 = l1.next
            l2 = l2.next
            
        while l1 is not None:
            res.next = ListNode((l1.val+r) % 10)
            res = res.next
            r = (l1.val+r) // 10
            l1 = l1.next
        
        while l2 is not None:
            res.next = ListNode((l2.val+r) % 10)
            res = res.next
            r = (l2.val + r) // 10
            l2 = l2.next
        
        if r != 0:
            res.next = ListNode(r)
        
        return head
# @lc code=end

if __name__ == "__main__":
    a = ListNode.build([9,9,9,9,9,9,9])
    b = ListNode.build([9,9,9,9])
    print(Solution().addTwoNumbers(a, b))
