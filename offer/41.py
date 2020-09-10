# -*- coding: utf-8 -*-
# @Time : 2020/9/10 上午9:29 
# @Author : cxy 
# @File : 41.py
# @desc:

"""
使用堆排序。用一个大顶堆max_heapq和一个小顶堆min_heapq存放较小和较大的元素。
[插入元素]如果max_heapq中元素个数小于等于min_heapq中元素个数，则插入到max_heapq里。具体方法：先插入到min_heapq然后弹出堆顶元素，插入到max_heapq中
        如果min_heapq元素个数小于max_heapq，则插入到min_heapq里。具体方法：先插入到max_heapq然后弹出堆顶元素，插入到max_heapq中min_heapq
[查找中位数]如果max_heapq中元素个数等于min_heapq中元素个数，则返回堆顶元素的平均数
        否则，返回元素多的堆的堆顶元素
时间：O(logn)。堆的插入和弹出操作使用 O(logN) 时间。
空间：O(n)
"""

from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heapq=[]
        self.min_heapq=[]

    def addNum(self, num: int) -> None:
        if len(self.max_heapq)<=len(self.min_heapq):
            heappush(self.min_heapq,-num)
            heappush(self.max_heapq,-heappop(self.min_heapq))
        else:
            heappush(self.max_heapq,num)
            heappush(self.min_heapq,-heappop(self.max_heapq))

    def findMedian(self) -> float:
        if len(self.max_heapq)==len(self.min_heapq):
            return (self.max_heapq[0]-self.min_heapq[0])/2
        elif len(self.max_heapq)<len(self.min_heapq):
            return -self.min_heapq[0]
        else:
            return self.max_heapq[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


