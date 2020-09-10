# -*- coding: utf-8 -*- 
# @Time : 2020/9/10 下午12:08 
# @Author : cxy 
# @File : 37.py 
# @desc:

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            cur = q.popleft()
            if not cur:
                ans.append(None)
                continue
            ans.append(cur.val)
            q.append(cur.left)
            q.append(cur.right)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        root = TreeNode(data.pop(0))
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            l, r = data.pop(0), data.pop(0)
            if l != None:
                left = TreeNode(l)
                cur.left = left
                q.append(cur.left)

            if r != None:
                right = TreeNode(r)
                cur.right = right
                q.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))