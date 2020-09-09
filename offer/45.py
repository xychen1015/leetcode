# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 下午3:56 
# @Author : cxy 
# @File : 45.py 
# @desc:
"""
本质是对数组中的元素进行排序。而排序的准则则是需要想一下的。现在假设数组中的元素都是字符串类型的，对于元素a,b
如果a+b>b+a，则b应该排在a前面
否则，a应该排在b前面
对于实现这样特定的排序可以采用快速排序、内置函数来实现
"""
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def my_sort(a,b):
            if a+b>b+a: return 1        # a排在b后面
            elif a+b<b+a: return -1     # a排在b前面
            else: return 0      # 相等
        from functools import cmp_to_key
        nums=[str(n) for n in nums]
        nums.sort(key=cmp_to_key(my_sort))      # 使用自定义排序函数
        return ''.join(nums)

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(nums,low,high):
            if low>=high: return
            pivot=nums[low]
            i,j=low,high
            while i<j:
                while i<j and nums[j]+pivot>=pivot+nums[j]: j-=1
                while i<j and nums[i]+pivot<=pivot+nums[i]: i+=1
                nums[i],nums[j]=nums[j],nums[i]
            nums[i],nums[low]=nums[low],nums[i]
            quick_sort(nums,low,i-1)
            quick_sort(nums,i+1,high)
        tmp=[str(n) for n in nums]
        quick_sort(tmp,0,len(nums)-1)       # 注意这里是长度-1
        return ''.join(tmp)
