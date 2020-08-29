'''
思路：如果root.val介于p.val q.val之间，则说明，root为最近公共祖先，返回root
如果p.val q.val都小于root.val，则遍历root的左子树
如果p.val q.val都大于root.val，则遍历root的右子树
时间：O(N)
空间：O(1)
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or min(p.val,q.val)<=root.val<=max(p.val,q.val): return root
        elif root.val>max(p.val,q.val): return self.lowestCommonAncestor(root.left,p,q)
        else: return self.lowestCommonAncestor(root.right,p,q)