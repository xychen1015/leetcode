# -*- coding: utf-8 -*- 
# @Time : 2020/8/31 下午9:32 
# @Author : cxy 
# @File : 64.py 
# @desc:
class Solution(object):
    def __init__(self):
        self.ans=0
    def sumNums(self, n):
        """
        :param n:
        :return:
        """
        n>1 and self.sumNums(n-1)       # 利用and的短路，一旦n>1不满足，则后续的递归就不会执行，自动跳转到下一行代码执行
        self.ans+=n
        return self.ans
