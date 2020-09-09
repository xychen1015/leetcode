# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 上午11:23 
# @Author : cxy 
# @File : 49.py 
# @desc:
"""
动态规划+三指针
分别用三个指针a，b，c只向×2、×3、×5之前的最小未被访问的位置
选择dp[a]*2,dp[b]*3,dp[c]*5中最小的作为dp[i]的值
相应的指针向后移动一个位置
[注意]:可能出现dp[a]*2,dp[b]*3,dp[c]*5中两个或者三个相同的值，因此应该是if if if 结构而非if elif else结构
时间：O(n)
空间：O(n)
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[0 for _ in range(n)]
        dp[0]=1
        a=b=c=0
        for i in range(1,n):
            dp[i]=min(dp[a]*2,dp[b]*3,dp[c]*5)
            if dp[i]==dp[a]*2: a+=1
            if dp[i]==dp[b]*3: b+=1
            if dp[i]==dp[c]*5: c+=1
        return dp[-1]
