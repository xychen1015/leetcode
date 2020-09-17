# -*- coding: utf-8 -*- 
# @Time : 2020/9/17 上午11:47 
# @Author : cxy 
# @File : 36.py 
# @desc:

"""
方法一：先中序遍历存储节点到列表中，然后改变指针指向
时间：O(n)
空间：O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        root_lst = []

        def dfs(root):
            if not root: return
            if root.left: dfs(root.left)
            root_lst.append(root)
            if root.right: dfs(root.right)

        if not root: return root
        dfs(root)
        for i in range(len(root_lst)):
            if i == 0:
                root_lst[i].left = root_lst[-1]
            else:
                root_lst[i].left = root_lst[i - 1]
            if i == len(root_lst) - 1:
                root_lst[i].right = root_lst[0]
            else:
                root_lst[i].right = root_lst[i + 1]
        return root_lst[0]

"""
方法二：在中序遍历的同时改变指针指向，因此需要一个指针pre来指向前一个节点
时间：O(n)
空间：O(n)
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root):
            if not root: return
            if root.left: dfs(root.left)
            if self.pre:
                self.pre.right, root.left = root, self.pre
            else:
                self.head = root
            self.pre = root
            if root.right: dfs(root.right)

        if not root: return root
        self.head = self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head






