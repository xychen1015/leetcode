# -*- coding: utf-8 -*- 
# @Time : 2020/9/3 下午2:18 
# @Author : cxy 
# @File : 60.py 
# @desc:

"""
动态规划：dp[i][j]表示i个筛子掷出j点的次数
在考虑状态转移时，可以从最后一个状态倒推前一个状态即：dp[n][i]+=dp[n-1][i-j],1<=j<=6
"""


class Solution:
    def twoSum(self, n: int) -> List[float]:
        """
        :param n: 筛子的个数
        :return:
        """
        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]  # 这里下标从1开始
        for i in range(1, 7): dp[1][i] = 1  # 1、初始化：对于只有一个筛子，每个点数出现的次数均为1

        for i in range(2, n + 1):  # 从2个筛子开始遍历
            for j in range(i, 6 * i + 1):  # 对于i个筛子，可能出现点数的范围为[i,6*i]，即全部为1（i），和全部为6（6×i）
                for k in range(1, 7):  # 状态转移
                    if j > k:
                        dp[i][j] += dp[i - 1][j - k]
                    else:
                        break
        total = 6 ** n
        return [i / total for i in dp[n] if i != 0]     # 将非0点数的概率返回
