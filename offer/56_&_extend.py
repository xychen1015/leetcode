# -*- coding: utf-8 -*- 
# @Time : 2020/9/3 下午6:34 
# @Author : cxy 
# @File : 56_&_extend.py 
# @desc:

"""
136：除了一个数字出现一次，其他都出现了两次，让我们找到出现一次的数。
全员异或即可
"""
def func(nums):
    ans=0
    for n in nums:
        ans^=n
    return ans

"""
137：除了一个数字出现一次，其他都出现了三次，让我们找到出现一次的数。 
"""
# 方法一：求和+set()
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=sum(nums)
        s_set=sum(set(nums))
        return (3*s_set-s)//2

# 方法二：二进制+位运算。统计32位各个位的1的个数上能被3整除的位置
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(32):
            cnt=0
            cur=1<<i
            for n in nums:
                if n&cur: cnt+=1
            if cnt%3: ans|=cur
        return ans if ans<2**32 else ans-2**32

"""
# 260：除了两个数字出现一次，其他都出现了两次，让我们找到这个两个数。
分组做异或，如果两组得到的结果都不为0,则最后结果就是两组异或的结果
如果有一组为0,另一组不为0,则两个数字出现在不为0的那一组
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        zero_counts = 0
        ans = 0
        for n in nums:
            ans ^= n
            if not n: zero_counts += 1
        if zero_counts == 1: return [ans, 0]
        l, r = min(nums), max(nums)     # 按数值的大小分为两组，大于等于mid的为一组，小于mid的为一组
        while l <= r:
            mid = (l + r) // 2
            left = right = 0
            for n in nums:
                if n < mid:
                    left ^= n
                else:
                    right ^= n
            if right and left:
                return [left, right]
            elif not left and right:
                l = mid + 1
            else:
                r = mid - 1


