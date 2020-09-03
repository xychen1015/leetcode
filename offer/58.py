# -*- coding: utf-8 -*- 
# @Time : 2020/9/3 下午3:46 
# @Author : cxy 
# @File : 58.py 
# @desc:

"""
方法一：暴力法
时间：O(kn)
空间：O(1)
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not n: return []
        ans = []
        for i in range(n-k+1):
            ans.append(max(nums[i:i+k]))
        return ans

"""
方法二：构建单调递减队列，队首元素即为长度为k的窗口中的最大值
时间：O(n)
空间：O(k)
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if not n: return []
        from collections import deque
        q = deque()
        ans = []

        for i in range(k):      # 没有形成窗口
            value = nums[i]
            while q and q[-1] < value: q.pop()
            q.append(value)
        ans.append(q[0])

        for i in range(k, n):       # 形成窗口
            if q[0]==nums[i-k]: q.popleft()     # 缩小窗口，等同于删除队首元素
            value = nums[i]
            while q and q[-1] < value: q.pop()      # 构建非严格单调递减队列
            q.append(value)
            ans.append(q[0])        # 队首元素为当前窗口中的最大值
        return ans
