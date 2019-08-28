#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (62.55%)
# Likes:    811
# Dislikes: 0
# Total Accepted:    94.4K
# Total Submissions: 149.6K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
#
#
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4
#
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # single_n = 0
        # for i in nums:
        #     single_n = single_n ^ i
        # return single_n
        return 2 * sum(set(nums)) - sum(nums)
