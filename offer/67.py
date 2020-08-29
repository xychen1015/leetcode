'''
时间：O(N)
空间：O(1)
'''
class Solution(object):
    def strToInt(self, s):
        """
        :type str: str
        :rtype: int
        """
        if not s: return 0
        ans=0       # 记录最终转化结果
        i=0
        flag=1      # 记录符号位，1正0负
        while i<len(s) and s[i]==" ": i+=1      # 去掉字符串前面若干空格
        if i==len(s) or (not s[i].isdigit() and s[i] not in ['-','+']): return 0        # 若s全为空格或第一位非空字符非数字和符号位，则返回0
        if s[i] in ['-','+']:       # 如果存在符号位
            if s[i]=='-': flag=0
            i+=1
        for j in range(i,len(s)):
            if not s[j].isdigit(): break        # 如果遍历到非数字，则跳出循环
            ans=ans*10+int(s[j])
        if not flag: ans=-ans
        if ans<(-2**31): return -2**31
        elif ans>2**31-1: return 2**31-1
        else: return ans