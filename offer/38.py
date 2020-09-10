# -*- coding: utf-8 -*- 
# @Time : 2020/9/10 上午11:33 
# @Author : cxy 
# @File : 38.py 
# @desc:

"""
递归+减枝
对于同一位置，如果出现同一字母则不进行递归。因此需要一个set来存储当前已经递归的字母
时间：O(n!)
空间：O(n^2),全排列的递归深度为 N ，系统累计使用栈空间大小为 O(N) ；
递归中辅助 Set 累计存储的字符数量最多为 N+(N−1)+...+2+1=(N+1)N/2N  ，即占用 O(N^2) 的额外空间。
"""
class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(s, path, visited, ans):
            if len(path) == len(s):
                if path not in ans: ans.append(path)
                return
            st = set()
            for i in range(len(s)):
                if i not in visited and s[i] not in st:
                    st.add(s[i])
                    dfs(s, path + s[i], visited + [i], ans)

        if len(s) < 2: return [s]
        ans = []
        dfs(s, "", [], ans)
        return ans


