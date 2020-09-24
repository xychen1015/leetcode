# -*- coding: utf-8 -*- 
# @Time : 2020/9/24 下午3:41 
# @Author : cxy 
# @File : 26.py 
# @desc:

"""
isSubStructure：用于遍历A中所有节点和B进行比较。当A或B为空时返回False，表示
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            # 如果B节点全部遍历结束，返回True
            if not B: return True
            # 如果B节点还有未遍历的节点，而A已经为空，返回True
            if not A: return False
            if A.val == B.val:
                return recur(A.left, B.left) and recur(A.right, B.right)
            else:
                return False

        if not B or not A: return False
        ans = False
        if A.val == B.val:
            ans = recur(A.left, B.left) and recur(A.right, B.right)
        if not ans: ans = self.isSubStructure(A.left, B)
        if not ans: ans = self.isSubStructure(A.right, B)
        return ans


