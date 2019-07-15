#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (58.25%)
# Likes:    522
# Dislikes: 0
# Total Accepted:    73.7K
# Total Submissions: 126.6K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#
#
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: "III"
# 输出: 3
#
# 示例 2:
#
# 输入: "IV"
# 输出: 4
#
# 示例 3:
#
# 输入: "IX"
# 输出: 9
#
# 示例 4:
#
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
#
#
# 示例 5:
#
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# #
# 用字典存储各个罗马数字代表的阿拉伯数字
# 按顺序读取罗马数字，当前数字小于下一个数字，则是下一个数字减去当前数字，否则直接相加
# 比如IV就是*-1+5=4*，而IIV这种情况是不存在的，对于其他量级的数字也是同理。
# 实际处理的时候最后一个数字无法和它下一个数字比较，因为不存在下一个数字。
# 但是最后一个数字永远是加的而不是减的，所以就单独拎出来处理就好。

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans = 0
        for i, char in enumerate(s[:-1]):
            if dic[char] >= dic[s[i+1]]:
                ans += dic[char]
            else:
                ans -= dic[char]
        ans += dic[s[-1]]
        return ans

