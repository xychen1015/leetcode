# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一：暴力法
从根节点root开始遍历，判断p,q节点是否存在于根节点的左右子树中，如果存在则返回root为最近的公共祖先。否则递归遍历root的左右子树。
'''
class Solution(object):
    def find(self,root,p):
        if not root: return False
        if root==p: return True
        else: return self.find(root.left,p) or self.find(root.right,p)

    def dfs(self,root,p,q):
        if root==p or root==q or not root: return root
        if (self.find(root.right,p) and self.find(root.left,q)) or (self.find(root.right,q) and self.find(root.left,p)): return root
        if self.dfs(root.left,p,q): return self.dfs(root.left,p,q)
        else: return self.dfs(root.right,p,q)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root,p,q)
'''
方法二
思路：根据遍历左右子树的结果left、right。
1如果left和right均不为空，则节点root为最近公共祖先;
2如果left为空而right不为空，则表明p，q在右子树中，right为他们的最近公共祖先
3如果left不为空而right为空，则与2类似
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root


