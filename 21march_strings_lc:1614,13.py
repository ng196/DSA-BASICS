# Here's a clean and concise version:  

# ---

# ## 📝 **Problem Statement**  
# Given a valid parentheses string `s`, return its **nesting depth**. The nesting depth is the maximum number of nested parentheses.  

# ### **Examples**  
# **Input:** `(1+(2*3)+((8)/4))+1`  
# **Output:** `3`  
# **Explanation:** Digit `8` is inside 3 nested parentheses.  

# **Input:** `(1)+((2))+(((3)))`  
# **Output:** `3`  

# ---

# ## 💡 **Solution Approach**  
# - Use a **counter** to track the current depth of open parentheses.  
# - For every `'('`, increment the counter.  
# - For every `')'`, decrement the counter.  
# - Track the **maximum value** of the counter as the result.  

# ---

class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        return max_depth



# ## 📊 **Complexity Analysis**  
# - **Time Complexity**: \( O(n) \) — Single pass through the string.  
# - **Space Complexity**: \( O(1) \) — Constant space for counters.






'''
oman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

time complexity is O(n) where n is the length of the string

'''

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"X":10 , "I" : 1 , "L":50 , "C" : 100 , "M" : 1000 , "V" : 5 , "D":500}
        ans = 0 
        for idx ,i in enumerate(s) :
            ans += values[i]
            if idx>= 1 and values[s[idx-1]] < values[i] :
                ans -= 2*values[s[idx-1]]

        return ans  