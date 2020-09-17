# -*- coding: utf-8 -*- 
# @Time : 2020/9/17 下午6:57 
# @Author : cxy 
# @File : 34.py 
# @desc:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        def dfs(root, path, target, ans):
            if not root: return
            target -= root.val      # 先减，再遍历
            if target == 0 and not root.left and not root.right:
                ans.append(path + [root.val])
            dfs(root.left, path + [root.val], target, ans)
            dfs(root.right, path + [root.val], target, ans)

        ans = []
        if not root: return ans
        dfs(root, [], s, ans)
        return ans

