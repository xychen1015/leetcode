# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 下午4:02 
# @Author : cxy 
# @File : 50.py 
# @desc:
"""
方法一： 统计每个字符出现的次数和第一次出现的位置
时间：O(n)
空间：O(n)
"""
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s: return " "
        cnt=[[0,-1] for _ in range(26)]
        for i in range(len(s)):
            index=ord(s[i])-97
            cnt[index][0]+=1
            if cnt[index][1]==-1: cnt[index][1]=i
        ans=len(s)
        for i in range(26):
            if cnt[i][0]==1: ans=min(ans,cnt[i][1])
        if ans==len(s): return " "
        return s[ans]

"""
方法二：使用字典。对于s中的字符如果出现在字典中，则将对应的value改为False，表示不止出现了一次
"""
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s: return " "
        d={}
        for c in s:
            if c not in d: d[c]=True
            else: d[c]=False
        for k,v in d.items():
            if v==True: return k
        return " "
