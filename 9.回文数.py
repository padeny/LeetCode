#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.29%)
# Likes:    653
# Dislikes: 0
# Total Accepted:    128.3K
# Total Submissions: 227.9K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
#
#
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
# ----------------------------------
# 具体做法如下：

# 每次进行取余操作 （ %10），取出最低的数字：y = x % 10
# 将最低的数字加到取出数的末尾：revertNum = revertNum * 10 + y
# 每取一个最低位数字，x 都要自除以 10
# 判断 x 是不是小于 revertNum ，当它小于的时候，说明数字已经对半或者过半了
# 最后，判断奇偶数情况：如果是偶数的话，revertNum 和 x 相等；如果是奇数的话，最中间的数字就在revertNum 的最低位上，将它除以 10 以后应该和 x 相等。

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        r = 0
        while x > r:
            r = r * 10 + x % 10
            x //= 10
        return r == x or x == r//10

