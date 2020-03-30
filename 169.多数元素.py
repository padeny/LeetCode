#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (62.73%)
# Likes:    533
# Dislikes: 0
# Total Accepted:    149.5K
# Total Submissions: 238K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if times == 0:
                res = nums[i]
                times = 1
            elif nums[i] == res:
                times += 1
            else:
                times -= 1
        return res
# @lc code=end

