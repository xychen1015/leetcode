# -*- coding: utf-8 -*- 
# @Time : 2020/9/18 下午12:12 
# @Author : cxy 
# @File : 33.py 
# @desc:

"""
方法一：递归。根据二叉搜索树后序遍历的性质，数组最后一个元素一定是根节点元素。
通过判断之前元素是否小于根节点的元素全部在前，大于根节点元素的全部在后，来判断是否符合题意
时间：O(n^2)
空间：O(n)
"""
# 写法一：是用两个数组分别存储
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder)<2: return True
        root=postorder[-1]
        i=0
        left=[]
        while i<len(postorder)-1 and postorder[i]<root:
            left.append(postorder[i])
            i+=1
        right=[]
        while i<len(postorder)-1:
            if postorder[i]<root: return False
            right.append(postorder[i])
            i+=1
        return self.verifyPostorder(left) and self.verifyPostorder(right)

# 写法二：两个指针
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def func(nums, beg, end):
            if beg >= end: return True
            root = nums[end]
            i = beg
            while i < end and nums[i] < root: i += 1
            low = i - 1
            while i < end and nums[i] > root: i += 1
            return i == end and func(nums, beg, low) and func(nums, low + 1, end - 1)

        return func(postorder, 0, len(postorder) - 1)