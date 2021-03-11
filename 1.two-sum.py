#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.47%)
# Likes:    11667
# Dislikes: 402
# Total Accepted:    2.1M
# Total Submissions: 4.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用哈希表加速
        # Time: O(N), Space: O(N)
        table = {}
        for idx, value in enumerate(nums):
            dif = target - value
            if dif in table:
                return [table[dif], idx]
            table[value] = idx
        return []
    
    # 暴力，O(N^2), O(1)
    # 排序，再双指针
    # 排序，再辅助哈希表
        
# @lc code=end

