# -*- coding: utf-8 -*- 
# @Time : 2020/9/24 上午11:36 
# @Author : cxy 
# @File : 27.py 
# @desc:
"""
方法一：递归。不需要使用额外的变量存储结果，直接就地进行翻转。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        root.left,root.right=self.mirrorTree(root.right),self.mirrorTree(root.left)
        return root

"""
方法二：使用栈.先把cur的左右子节点放入到栈中，然后交换cur的左右子节点
"""
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        stack=[root]
        while stack:
            cur=stack.pop()
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
            cur.left,cur.right=cur.right,cur.left
        return root
