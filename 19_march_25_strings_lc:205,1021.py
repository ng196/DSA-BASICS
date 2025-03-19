'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

'''
from collections import defaultdict 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lst_int = [x for x in range(0, 26)]
        ls = len(s)
        lt = len(t)
        s_dict = defaultdict(list)
        t_dict = defaultdict(list)
        if ls != lt:return False 


        for idx, i in enumerate(s):
            s_dict[i].append(idx)  

        for idx, i in enumerate(t):
            t_dict[i+'23'].append(idx)  

        if list(s_dict.values()) == list(t_dict.values()):
            return True 
        return False
    
    
'''
TIME AND SPEACE COMPLEXITY : O(N)
'''
      
      
      
        
'''
leetcode : 1021 , 
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


'''

from collections import defaultdict

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        flst = []
        left = 0 
        right = 0 
        
        for idx, i in enumerate(s):
            if i == '(':
                left += 1 
            elif i == ')':
                right += 1 
            
            if left == right:
                flst.append(idx)  

        res = []  
        prev = 0  

        for i in flst:
            res.append(s[prev + 1 : i])  
            prev = i + 1  

        return "".join(res) 
    
    
# TIME AND SPACE COMPLEXITY : O(N)