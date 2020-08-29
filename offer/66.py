'''
方法一
思路：使用两个数组分别存储元素a[i]前、后元素的乘积（不包括元素a[i]）。最后返回两个数组相应位置上元素的乘积
时间：O(N)
空间：O(N)
'''
class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        if len(a)<2: return a
        n=len(a)
        left=[1 for _ in range(n)]
        right=[1 for _ in range(n)]
        for i in range(1,n):
            left[i]=left[i-1]*a[i-1]
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*a[i+1]
        return [left[i]*right[i] for i in range(n)]

'''
方法二：优化空间
思路：将结果集用于存储中间结果，先计算从左往右元素的乘积，再计算从右往左的乘积，使用一个变量tmp来记录右边元素依次的乘积
时间：O(N)
空间：O(1)
'''
class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        n=len(a)
        if n<2: return a
        b=[1 for _ in range(n)]
        for i in range(1,n):
            b[i]=b[i-1]*a[i-1]
        tmp=1
        for i in range(n-1,-1,-1):
            b[i]=b[i]*tmp
            tmp*=a[i]
        return b