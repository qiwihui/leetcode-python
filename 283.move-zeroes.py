#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (58.54%)
# Likes:    5172
# Dislikes: 162
# Total Accepted:    1.1M
# Total Submissions: 1.8M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#

from typing import List
# @lc code=start
class Solution:

    # no order
    
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     left = 0
    #     right = len(nums)-1
    #     while left < right:
    #         print(left, right)
    #         while nums[right] == 0:
    #             right -= 1
    #         if nums[left] == 0:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             right -= 1
    #         left += 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = self.removeElement(nums, 0)
        while p < len(nums):
            nums[p] = 0
            p += 1

    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# @lc code=end
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)
    print(nums == [1,3,12,0,0])
