'''

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        l = len(nums)-1
        high = l 
        while low < high :
            mid = (low + high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            elif nums[mid] > target :
                high = mid-1 
        if low == high :
            mid = (low+high)//2
            return mid if target < nums[mid] or target == nums[mid] else mid+1 if mid == l or nums[mid+1]>target else mid 
            
        return mid 
    
    '''
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
    
    '''
    
class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0 
        e = x 
        ans=0
        while s <= e :
            mid = (s+e)//2
            #if mid**2 == x:
                #return mid
            if mid**2 > x:
                e = mid-1
            else:
                s = mid + 1 
                ans = mid  

        return ans 
