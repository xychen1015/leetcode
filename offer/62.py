# -*- coding: utf-8 -*- 
# @Time : 2020/9/1 下午8:56 
# @Author : cxy 
# @File : 62.py 
# @desc:
"""
约瑟夫环：假设pos为当前最后一个剩余元素的索引值index，且当只有一个元素的时候pos=0
从后往前倒推有这样的递推关系: pos=(pos+m)%i
时间：O(n)
空间：O(1)
"""
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        pos=0
        for i in range(2,n+1):      # 最后一轮剩下两个人，因此从2开始反推
            pos=(pos+m)%i
        return pos
