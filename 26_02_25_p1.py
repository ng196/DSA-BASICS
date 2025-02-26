'''

GitHub : https://github.com/ng196/DSA-BASICS.git

problem statement : An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
 Given an integer n, return true if n is an ugly number.
 
 '''

class Solution:
    def isUgly(self, n: int) -> bool:

        if(n<=0):
            return False
        while(n%2 == 0) : 
            n/=2
        while(n%3 == 0) : 
            n/=3
        while(n%5 == 0) : 
            n/=5
        return (n==1)    
        
'''
        
 Time Complexity: O(log n)
 Space Complexity: O(1)


Approach : remove all the factors of 2, 3 and 5 from the number. If at any point you have a zero then return false as it is not an ugly number. Otherwise if after removing all the factors of 2, 3 and 5 we are left with 1 then return true else return false.

'''
        
        
        