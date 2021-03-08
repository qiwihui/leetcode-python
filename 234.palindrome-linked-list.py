#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (40.44%)
# Likes:    4739
# Dislikes: 428
# Total Accepted:    567.9K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

from ds_linkedlist import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head: ListNode):
    pre, cur = None, head
    while cur is not None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # return self._reverse_linkedlist(head)

        return self._slow_fast_pointer(head)

        # self.left = head
        # return self._traverse(head)
    
    def _reverse_linkedlist(self, head: ListNode) -> bool:
        # FIXME not working
        right = reverse(head)
        while right is not None and head is not None:
            if right.val != head.val:
                return False
            right = right.next
            head = head.next
        return True

    def _slow_fast_pointer(self, head: ListNode) -> bool:
        """快慢指针"""
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # odd or even
        if fast is not None:
            slow = slow.next
        
        # reverse and compare
        left = head
        right = reverse(slow)
        # p and q are used to reverse back original linked list
        # q = right
        while right is not None:
            # p = left
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        # p.next = reverse(q)
        return True
        
    def _traverse(self, head: ListNode) -> bool:
        """递归"""
        if head is None:
            return True
        res = self._traverse(head.next)
        res = res and self.left.val == head.val
        self.left = self.left.next
        return res

# @lc code=end
def make_linkedlist(array: list) -> ListNode:
    tail = None
    for item in array[::-1]:
        node = ListNode(item, tail)
        tail = node
    return node

if __name__ == "__main__":
    linkedlist = [1,1,2,1]
    head = make_linkedlist(linkedlist)
    print(Solution().isPalindrome(head))
