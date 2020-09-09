# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 下午3:23 
# @Author : cxy 
# @File : 46.py 
# @desc:
"""
方法一：递归。
1.1 使用额外的数组存储所有结果，最终结果为结果集的大小
时间：O(2^n)
空间：O(n)
"""
class Solution:
    def translateNum(self, num: int) -> int:
        def dfs(num,path,ans):
            if not num:
                if path not in ans: ans.append(path)
                return
            cur=int(num[0])
            dfs(num[1:],path+chr(cur),ans)
            if len(num)>=2:
                if cur==1 or (cur==2 and num[1]<='5'):
                    cur=cur*10+int(num[1])
                    dfs(num[2:],path+chr(cur),ans)
        ans=[]
        dfs(str(num),"",ans)
        return len(ans)
"""
1.2 不使用额外的数组存储结果，直接返回数量
"""
class Solution:
    def translateNum(self, num: int) -> int:
        def dfs(num, idx):
            if idx == len(num): return 1
            if idx == len(num) - 1 or num[idx] == '0' or num[idx:idx + 2] > '25':
                return dfs(num, idx + 1)
            else:
                return dfs(num, idx + 1) + dfs(num, idx + 2)

        return dfs(str(num), 0)

"""
方法二：动态规划
dp[i]表示前i个数字可以翻译成字母的个数。因此dp数组的长度应该为n+1
时间：O(n)
空间：O(n)
"""
class Solution:
    def translateNum(self, num: int) -> int:
        num=str(num)
        n=len(num)
        dp=[1 for _ in range(n+1)]
        for i in range(2,n+1):
            if num[i-2]=='0' or num[i-2:i]>'25': dp[i]=dp[i-1]
            else: dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]

