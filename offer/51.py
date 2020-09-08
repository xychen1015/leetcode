# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 下午3:22 
# @Author : cxy 
# @File : 51.py 
# @desc:
"""
采用归并排序的方法
为了避免每次都创建一个tmp数组，这里全流程复用一个tmp数组
时间：O(nlogn)
空间：O(n)
"""
cnt=0
def merge(nums,start,mid,end,tmp):
    global cnt
    for i in range(start,end+1): tmp[i]=nums[i]
    k=start
    i,j=start,mid+1
    while i<=mid and j<=end:
        if tmp[i]<=tmp[j]:
            nums[k]=tmp[i]
            i,k=i+1,k+1
        else:       # 当发现排在后面的元素大于前面的元素，则cnt加上mid-i+1
            cnt+=mid-i+1
            nums[k]=tmp[j]
            j,k=j+1,k+1
    while i<=mid:
        nums[k] = tmp[i]
        i, k = i + 1, k + 1
    while j<=end:
        nums[k] = tmp[j]
        j, k = j + 1, k + 1
def merge_sort(nums,start,end,tmp):
    if start>=end: return
    mid=(start+end)//2
    merge_sort(nums,start,mid,tmp)
    merge_sort(nums,mid+1,end,tmp)
    merge(nums,start,mid,end,tmp)

if __name__=="__main__":
    nums=list(map(int,input().split()))
    n=len(nums)
    tmp=[0 for _ in range(n)]
    merge_sort(nums,0,n-1,tmp)
