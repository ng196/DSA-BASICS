# Lc : 451

'''

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

'''

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        dct = {key: value for key, value in freq.items()}
        dct = dict(sorted(dct.items() , key = lambda x :x[1], reverse=True))

        ans = ""
        for i in dct.keys():
            for n in range(0, dct[i]):
                ans = ans + str(i)

        return ans


# time complexity : N log(N)




# LC : 8 


'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

'''

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        ans = 0 
        sign = 1 
        
        if len(s) == 0:
            return 0
        
        if s[0] == '-': 
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:] 
        
        for idx, i in enumerate(s):
            if not i.isdigit(): 
                ans = idx
                break
            else: 
                ans += 1 
        
        if ans == 0:
            return 0
        
        result = int(s[0:ans]) * sign
        

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        
        return result


# time ans space complexities : O(n) and O(1)


'''

Given a string s of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 

Examples :

Input: s = "aba", k = 2
Output: 3
Explanation: The substrings are: "ab", "ba" and "aba

class Solution:
    def countSubstr(self, s, k):
        from collections import defaultdict

        def atMostK(s, k):
            if k < 0:
                return 0
            char_count = defaultdict(int)
            left = 0
            count = 0

            for right in range(len(s)):
                char_count[s[right]] += 1

                while len(char_count) > k:
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        del char_count[s[left]]
                    left += 1

                count += right - left + 1
            return count

        return atMostK(s, k) - atMostK(s, k - 1)

'''