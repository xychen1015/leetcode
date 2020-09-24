# -*- coding: utf-8 -*- 
# @Time : 2020/9/24 上午10:09 
# @Author : cxy 
# @File : 29.py 
# @desc:

"""
使用四个变量来存储矩阵在收缩过程中的左右上下的边界值
左->右：t+=1。如果t>b，跳出循环
上->下：l-=1。如果l>r，跳出循环
右->左：b-=1。如果t>b，跳出循环
下->上：r+=1。如果l>r，跳出循环
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix) or not len(matrix[0]): return []
        l,r,t,b=0,len(matrix[0])-1, 0, len(matrix)-1
        ans=[]
        while True:
            for i in range(l,r+1): ans.append(matrix[t][i])
            t+=1
            if t>b: break
            for i in range(t,b+1): ans.append(matrix[i][r])
            r-=1
            if l>r: break
            for i in range(r,l-1,-1): ans.append(matrix[b][i])
            b-=1
            if t>b: break
            for i in range(b,t-1,-1): ans.append(matrix[i][l])
            l+=1
            if l>r: break
        return ans