#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (47.76%)
# Likes:    400
# Dislikes: 0
# Total Accepted:    45.3K
# Total Submissions: 94.8K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def preorder(root, reverse=False):
            if not root:
                return [None]
            if reverse:
                return [root.val] +preorder(root.right,reverse=reverse)+preorder(root.left,reverse=reverse)
            else:
                return [root.val] +preorder(root.left)+preorder(root.right)
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        else:
            return preorder(root.left)==preorder(root.right, reverse=True)

