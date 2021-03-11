#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.41%)
# Likes:    13391
# Dislikes: 695
# Total Accepted:    2.1M
# Total Submissions: 6.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# Example 4:
# 
# 
# Input: s = ""
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        left = right = 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1

            window.setdefault(c, 0)
            window[c] += 1

            while window.get(c) > 1:
                # 重复
                d = s[left]
                window[d] -= 1
                left += 1
            
            res = max(res, right - left)
        return res


# @lc code=end

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcc")==3)
    print(Solution().lengthOfLongestSubstring("abcabcbb")==3)
    print(Solution().lengthOfLongestSubstring("bbbbb")==1)
    print(Solution().lengthOfLongestSubstring("")==0)
