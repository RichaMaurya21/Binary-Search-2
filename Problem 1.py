## Problem 1: (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def firstIndex(l,r,target):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    if mid == 0 or nums[mid]!= nums[mid-1]:
                        return mid
                    else:
                        r = mid - 1

                elif nums[mid] < target:
                    l = mid + 1
                
                else:
                    r = mid - 1
            return -1
        
        def lastIndex(l,r,target):
            while l <= r:
                mid = (l + r)//2
                if nums[mid] == target:
                    if mid == len(nums)-1 or nums[mid]!= nums[mid+1]:
                        return mid
                    else:
                        l = mid + 1

                elif nums[mid] < target:
                    l = mid + 1
                
                else:
                    r = mid - 1
                
            return -1
        
        
        l, r = 0, len(nums) - 1
        first = firstIndex(l, r, target)
        if first == -1:
            return [-1, -1]
        last = lastIndex(l, r, target)
        return [first, last]

       