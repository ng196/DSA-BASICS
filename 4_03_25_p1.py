
'''
Problem statement : Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]


'''

'''
Approach : did what was asked to do and then returned the resulting image.

'''


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in image:
            i.reverse()
            for idx in range(0,len(i)):
                i[idx] = (i[idx]+1)%2
        return image
        
        
'''
Time Complexity: O(MN)
Space Complexity: O(1)
'''

