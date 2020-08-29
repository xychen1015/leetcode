'''
思路：由于不能使用+-×/，因此只能使用*位运算*实现加法
通过异或和与运算，分别记录非进位之和和进位，并赋值给a b
a,b=a^b,(a^b)<<1
'''
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x=0xffffffff
        a,b=a&x,b&x
        while b:
            a,b=a^b,(a&b)<<1&x
        return a if a<=0x7fffffff else ~(a^x)