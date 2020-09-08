# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 上午11:22 
# @Author : cxy 
# @File : 52.py 
# @desc:

"""
方法一：先计算两个链表的长度，让长度长的链表指针先走，待长度相等后，再一起走
时间：O(n+m)
空间：O(1)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a=0
        cur=headA
        while cur:
            a+=1
            cur=cur.next
        b=0
        cur=headB
        while cur:
            b+=1
            cur=cur.next
        cura=headA
        while a>b:
            cura=cura.next
            a-=1
        curb=headB
        while b>a:
            curb=curb.next
            b-=1
        while cura and curb:
            if cura==curb: return cura
            cura=cura.next
            curb=curb.next
        return cura

"""
方法二：双指针。指针1 2分别指向链表A B的开头。当指针1为空时，指向链表B的开头;当指针2为空时，指向链表A的开头
时间：O(n+m)
空间：O(1)
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cura,curb=headA,headB
        while cura!=curb:       # 这样并不会造成死循环。如果不存在交点，则必定存在cura=curb=None，此时也会跳出循环
            cura=cura.next if cura else headB
            curb=curb.next if curb else headA
        return cura
