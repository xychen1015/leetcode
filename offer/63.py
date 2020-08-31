# -*- coding: utf-8 -*- 
# @Time : 2020/8/31 下午10:00 
# @Author : cxy 
# @File : 63.py 
# @desc: 剑指offer63
'''
方法一：从后向前计算
时间：O(n)
空间：O(n)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :param prices:
        :return:
        """
        n=len(prices)
        if n<2: return 0
        dp=[0 for _ in range(n)]
        dp[-1]=prices[-1]
        for i in range(n-2,-1,-1):
            dp[i]=max(dp[i+1],prices[i+1])      # 计算price[i]元素之后（不包括price[i]）的最大元素的值
        for i in range(n):
            dp[i]=max(0,dp[i]-prices[i])        # 计算在第i天卖出股票能获得的最大利润
        return max(dp)

'''
方法二：从前往后
dp[i]表示第i天卖出后能获得的最大利润，进一步优化用变量cur_profit存储前i天得到的最优解
时间：O(n)
空间：O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        cur_profit=0
        for i in range(1,n):
            cur_profit=max(cur_profit,prices[i]-min(prices[:i]))
        return cur_profit
