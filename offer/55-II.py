# -*- coding: utf-8 -*- 
# @Time : 2020/9/4 上午10:46 
# @Author : cxy 
# @File : 55-II.py 
# @desc:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
方法一：自底向上计算每个节点的树的高度，判断以各节点为根的树是否为平衡二叉树
时间：O(nlogn)
空间：O(n)，退化为链表
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):  # 计算以root为根基点树的高度
            if not root: return 0
            left = height(root.left)
            right = height(root.right)
            return 1 + max(left, right)

        if not root: return True
        left = height(root.left)
        right = height(root.right)
        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

"""
方法二：减枝，在计算树的高度的时候，如果当前节点的左右子树高度之差大于1时，则返回-1
并且在计算过程中 如果发现高度为-1,则直接返回-1
时间：O(n)
空间：O(n)
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root: return 0
            left=dfs(root.left)
            if left==-1: return -1
            right=dfs(root.right)
            if right==-1: return -1
            if abs(left-right)>1: return -1
            else: return 1+max(left,right)
        return dfs(root)!=-1

