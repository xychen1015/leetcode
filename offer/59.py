# -*- coding: utf-8 -*- 
# @Time : 2020/9/3 下午3:13 
# @Author : cxy 
# @File : 59.py 
# @desc:

"""
由于题目要求max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。因此不能直接使用max方法，需要使用一个暂存数组来存放当前元素之后的最大元素的值
"""
class MaxQueue:

    def __init__(self):
        from collections import deque
        self.q = deque()
        self.mx = deque()

    def max_value(self) -> int:
        return self.mx[0] if self.mx else -1

    """
    依次插入[2,5,3,4,6,6]
    q:[2], mx:[2]
    q:[2,5], mx:[5]，弹出2并插入5
    q:[2,5,3], mx:[5,3]，不弹出并插入3
    q:[2,5,3,4], mx:[5,4]，弹出3并插入4
    q:[2,5,3,4,6], mx:[6],弹出4 5并插入6
    q:[2,5,3,4,6,6], mx:[6,6],不弹出并插入6,因为6<=6
    """
    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.mx and self.mx[-1]<value: self.mx.pop()      # 当新插入的元素大于暂存数组中的末端元素时，则弹出末端
        self.mx.append(value)       # 直到大于等于value，则插入到暂存数组中


    def pop_front(self) -> int:
        if not self.q: return -1

        ans = self.q.popleft()
        if ans == self.mx[0]: self.mx.popleft()
        return ans




# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
