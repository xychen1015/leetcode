# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 下午6:01 
# @Author : cxy 
# @File : 44.py 
# @desc:
"""
找规律：易知对于i位数组成的序列长度为i*9*10^(i-1)，即0-9长度为9×1,10-99长度为90×2,100-999长度为900×3。
1 因此可以求出n位于第几位数的第几个--记作n
2 进而可以求出真实的数字--记作number
3 确定所求数位在 number 的哪一数位
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10: return n
        base = 9
        i = 1
        while n - base * i >= 0:        # 1
            n -= base * i
            i += 1
            base *= 10
        number = 10 ** (i - 1) + (n - 1) // i       # 2
        idx = (n - 1) % i       # 3
        return int(str(number)[idx])

