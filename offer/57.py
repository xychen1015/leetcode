# -*- coding: utf-8 -*- 
# @Time : 2020/9/3 下午5:35 
# @Author : cxy 
# @File : 57.py 
# @desc:

"""
方法一：左右指针
当左右指针区间的数之和小于s时，右指针右移；大于s时，左指针右移
当区间数之和等于target且左右指针值不相等则将左右数值之间的数放入到结果数组中
然后将左指针右移
当左指针大于target//2时，循环停止
时间：O(target)
空间：O(1)
"""
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target<3: return []
        l,r=1,2
        ans=[]
        s=l+r
        while l<=target//2:
            while s<target:
                r+=1
                s+=r
            while s>target and l<r:
                s-=l
                l+=1
            if s==target and l!=r: ans.append([i for i in range(l,r+1)])
            s-=l
            l+=1
        return ans
