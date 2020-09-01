# -*- coding: utf-8 -*- 
# @Time : 2020/9/1 下午9:29 
# @Author : cxy 
# @File : 61.py 
# @desc:
"""
方法一：先排序，并统计0出现的次数，当作可以犯错的次数
然后找到最小的元素beg，看beg+1到beg+4是否在nums中
时间：排序O(nlogn)
空间：O(1)
"""
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        zero_counts=0
        i=0
        while i<len(nums) and nums[i]==0:
            zero_counts+=1
            i+=1
        if i==len(nums): return True
        beg=nums[i]
        for j in range(5):
            if (beg+j) in nums[i:]: continue
            if not zero_counts: return False
            else: zero_counts-=1
        return True

"""
方法二：能够出现顺子的情况必须同时满足以下两个条件：
1、除了0之外没有重复的元素
2、最大-最小<5
"""
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat=set()
        max_num=-1
        min_num=14
        for i in range(len(nums)):
            if not nums[i]: continue
            if nums[i] in repeat: return False
            repeat.add(nums[i])
            max_num=max(max_num,nums[i])
            min_num=min(min_num,nums[i])
        return max_num-min_num<5
