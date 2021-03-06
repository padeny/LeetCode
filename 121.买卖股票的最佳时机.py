#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (50.41%)
# Likes:    515
# Dislikes: 0
# Total Accepted:    69.7K
# Total Submissions: 137.9K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#
#
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
# 我们可以维持两个变量——minprice 和 maxprofit，
# 它们分别对应迄今为止所得到的最小的谷值和最大的利润
# （卖出价格与最低价格之间的最大差值）
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices)<=1):
            return 0
        min_p=prices[0]
        max_p=0
        for p in prices:
            min_p= min(min_p, p)
            max_p= max(max_p, p - min_p)
        return max_p

