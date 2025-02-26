
'''
GitHub : https://github.com/ng196/DSA-BASICS.git

Given a number x, reverse its binary form and return the answer in decimal
'''

class Solution:
    def reversedBits(self, x):
        bin_str = format(x, '032b') 
        reversed_bin_str = bin_str[::-1]  
        return int(reversed_bin_str, 2)

'''
Time and space complexity : O(1)

approach: convert the given number into a 32 bit format binary using format(x,"032b) , reversing the string , converting to int 

'''