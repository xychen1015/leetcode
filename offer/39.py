# -*- coding: utf-8 -*- 
# @Time : 2020/9/10 上午11:03 
# @Author : cxy 
# @File : 39.py 
# @desc:

"""
方法一：hashmap。统计每个数字出现的次数，返回出现次数最多的元素
时间：O(n)
空间：O(n)
"""
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=Counter(nums)
        cnt=-1
        ans=-9999999
        for k,v in hashmap.items():
            if v>cnt:
                cnt=v
                ans=k
        return ans

"""
方法二：摩尔投票。为构建正负抵消，假设数组首个元素为众数，遍历统计票数，当发生正负抵消时，剩余数组的众数一定不变
时间：O(n)
空间：O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote=0
        for n in nums:
            if not vote: pivot=n
            vote+=1 if n==pivot else -1
        return pivot

