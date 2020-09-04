# -*- coding: utf-8 -*- 
# @Time : 2020/9/4 下午12:25 
# @Author : cxy 
# @File : 54.py 
# @desc:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
方法一：按照右根左的次序遍历二叉搜索树，将遍历的结果存储到path中
最后返回path的第k-1个元素即为第k大的元素
时间：O(nlogn)
空间：O(n)
"""
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def midSearch(root,path):
            if not root: return
            midSearch(root.right,path)
            path.append(root.val)
            midSearch(root.left,path)

        path=[]
        midSearch(root,path)
        return path[k-1]

"""
方法二：
提前返回： 若 k=0 ，代表已找到目标节点，无需继续遍历，因此直接返回；
统计序号： 执行 k=k−1（即从 k 减至 0 ）；
记录结果： 若 k=0 ，代表当前节点为第 k 大的节点，因此记录 res=root.val；
时间：O(n)
空间：O(n)
"""
class Solution:
    def __init__(self):
            self.ans=0
            self.k=0
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k==0: return
            self.k-=1
            if self.k==0: self.ans=root.val
            dfs(root.left)
        self.k=k
        dfs(root)
        return self.ans

