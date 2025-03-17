'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.


time complexity , space compexity : O(log(m*n)) 



'''

class Solution:
    def searchMatrix(self , matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix) , len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            if num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False