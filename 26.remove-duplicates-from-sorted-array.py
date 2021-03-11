#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (45.93%)
# Likes:    3131
# Dislikes: 5970
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means a
# modification to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two
# elements of nums being 1 and 2 respectively. It doesn't matter what you leave
# beyond the returned length.
#
#
# Example 2:
#
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]
# Explanation: Your function should return length = 5, with the first five
# elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't
# matter what values are set beyond the returned length.
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in ascending order.
#
#
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 快慢指针技巧
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        # print(nums[:slow+1])
        return slow+1

# @lc code=end

# for ListNone
from ds_linkedlist import ListNode

class Solution2:
    def removeDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        # 快慢指针技巧
        slow = fast = head
        while fast is not None:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
                
            fast = fast.next
        
        slow.next = None
        return head


if __name__ == "__main__":
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])==5)
    print(Solution().removeDuplicates([]))

    print(Solution2().removeDuplicates(ListNode.build([0,0,1,1,1,2,2,3,3,4])))
