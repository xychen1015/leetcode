# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 下午12:13 
# @Author : cxy 
# @File : 48.py 
# @desc:

"""
方法一：滑动窗口
时间：O(n^2)
空间：O(1)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n=len(s)
        ans=1
        i,j=0,1     # i,j分别为滑动窗口的首和尾
        while j<n:
            while i<j and s[j] in s[i:j]: i+=1      # 当发现尾指针所指向的元素存在在s[i:j]之间时，则将首指针向后移动i+=1，直到s[j]不存在在s[i:j]中
            ans=max(ans,j-i+1)
            j+=1
        return ans

"""
方法二：哈希表优化。使用哈希表存储key在s中的最后一次出现的索引位置的后一个位置
在j向后移动时，如果发现s[j]已经存在哈希表中，则将i移动至hash[s[j]]+1的位置
时间：O(n)
空间：O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        d={}
        ans=1
        i=0
        for j in range(len(s)):
            if s[j] in d:
                i=max(d[s[j]],i)
            d[s[j]]=j+1
            ans=max(ans,j-i+1)
        return ans


