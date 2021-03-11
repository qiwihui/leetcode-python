#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (35.96%)
# Likes:    6177
# Dislikes: 418
# Total Accepted:    506.2K
# Total Submissions: 1.4M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t, return the minimum window in s which will contain
# all the characters in t. If there is no such window in s that covers all
# characters in t, return the empty string "".
# 
# Note that If there is such a window, it is guaranteed that there will always
# be only one unique minimum window in s.
# 
# 
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 10^5
# s and t consist of English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(n) time?
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        for i in t:
            need.setdefault(i, 0)
            need[i] += 1

        left = right = 0
        valid = 0
        # 最小覆盖子串长度
        start = 0
        length = float("inf")
        while right < len(s):
            c = s[right]
            right += 1
            
            if c in need:
                window.setdefault(c, 0)
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # print(left, right)
                
            while valid == len(need):
                # 最小覆盖子串位置
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return  "" if length == float("inf") else s[start:start+length]
# @lc code=end

if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
