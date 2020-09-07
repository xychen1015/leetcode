# -*- coding: utf-8 -*- 
# @Time : 2020/9/7 下午12:04 
# @Author : cxy 
# @File : 53.py 
# @desc:

"""
方法一：遍历
时间：O(n)
空间：O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n+1):
            if i not in nums: return i
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        if nums[0]!=0: return 0
        i=1
        while i<n and nums[i]==nums[i-1]+1: i+=1
        return i

"""
方法二：二分查找.排序数组中的搜索问题，首先想到 二分法 解决。
时间：O(logn)
空间：O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==mid: l=mid+1      # 如果下标等于元素本身，则在右边数组中找
            else: r=mid-1       # 否则在左边数组中找
        return l