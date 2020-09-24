# -*- coding: utf-8 -*- 
# @Time : 2020/9/24 上午10:38 
# @Author : cxy 
# @File : 28.py 
# @desc:

"""
方法一：将层序遍历的结果按层存储起来，然后判断每一层遍历结果是否左右对称
时间：O(n)
空间：O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right): return True
        order=[]
        stack=[(root,0)]
        while stack:
            cur,level=stack.pop()
            if len(order)==level: order.append([])
            if not cur:
                order[level].append(None)
                continue
            order[level].append(cur.val)
            stack.append((cur.right,level+1))
            stack.append((cur.left,level+1))
        for l in order:
            if len(l)<2: continue
            pre,pos=l[:len(l)//2],l[len(l)//2:]
            if pre[::-1]!=pos: return False
        return True

"""
方法二：递归。如果一个二叉树是对称二叉树，则1 2 3同时满足：
1 L.val=R.val ：即此两对称节点值相等。
2 L.left.val=R.right.val ：即 L 的 左子节点 和 R 的 右子节点 对称；
3 L.right.val=R.left.val ：即 L 的 右子节点 和 R 的 左子节点 对称。
时间：O(n)
空间：O(n)
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(l, r):
            if not l and not r: return True
            if not l or not r: return False
            if l.val != r.val: return False
            return recur(l.left, r.right) and recur(l.right, r.left)

        if not root: return True
        return recur(root.left, root.right)

