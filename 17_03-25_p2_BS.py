'''
Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.


'''
class Solution:

    def kthElement(self, a, b, k):
        m = sorted(a+b)
        return m[k-1]