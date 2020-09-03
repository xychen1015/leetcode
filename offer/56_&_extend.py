# -*- coding: utf-8 -*- 
# @Time : 2020/9/3 下午6:34 
# @Author : cxy 
# @File : 56_&_extend.py 
# @desc:
### 260：除了两个数字出现一次，其他都出现了两次，让我们找到这个两个数。

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

