# -*- coding: utf-8 -*- 
# @Time : 2020/9/23 上午10:25 
# @Author : cxy 
# @File : 124.py 
# @desc:
# 给定一个非空二叉树，返回其最大路径和。 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
# 该路径至少包含一个节点，且不一定经过根节点。
"""
时间：O(n)
空间：O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def pos_order(root):
            if not root: return 0
            l, r = pos_order(root.left), pos_order(root.right)      # 递归计算左右子树最大路径之和
            l, r = max(l, 0), max(r, 0)     # 当最大路径为正时才考虑这条路经
            cur = root.val + l + r      # 计算当前节点的最大路径之和
            self.ans = max(self.ans, cur)       # 更新结果
            return root.val + max(l, r)        # 返回当前节点的贡献值

        self.ans = -sys.maxsize
        pos_order(root)
        return self.ans

