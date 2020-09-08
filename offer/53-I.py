# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 上午11:07 
# @Author : cxy 
# @File : 53-I.py 
# @desc:

"""
运用两次二分查找，找到第一次出现和最后一次出现的位置。
时间：O(logn)
空间：O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:     # 当找到相等位置时，不返回，应该继续向左寻找到第一次出现的位置
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            # 循环结束后，l r的位置关系是[r,l]。需要判断是否找到
            if l != len(nums) and nums[l] == target: return l
            return -1

        def find_right(nums, target):
            l, r = 0, len(nums) - 1
            left = False
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:     # 当找到相等位置时，不返回，应该继续向右寻找到最后一次出现的位置
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            if r != len(nums) and nums[r] == target: return r
            return -1

        if not nums: return [-1, -1]
        l, r = find_left(nums, target), find_right(nums, target)
        return [l, r]
