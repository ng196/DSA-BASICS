'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

time ans apace complexity : O(n+m) , O(k)
'''
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if Counter(s) == Counter(t) else False 
            
'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example : 
  Input: `strs = ["flower","flow","flight"]`
  Output: `"fl"`
- Input: `strs = ["dog","racecar","car"]`
  Output: `""`

## Solution
'''
from typing import List 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        first, last = strs[0], strs[-1]
        ans = 0
        min_len = min(len(first), len(last))
        
        while ans < min_len and first[ans] == last[ans]:
            ans += 1
        
        return first[:ans]
    
'''
## Approach
1. **Sorting the Strings:**
    - After sorting, the first and last strings in the sorted list will have the maximum lexicographical difference.
    - The common prefix of these two will also be the common prefix of all the strings.
2. **Character Comparison:**
    - Compare characters of the first and last strings until a mismatch is found.
    - Return the substring from the beginning to the mismatch index.

## Complexity Analysis
- **Time Complexity:**
  - Sorting the array takes **O(n log n)**, where **n** is the number of strings.
  - The character comparison step takes **O(m)** time, where **m** is the length of the shortest string.
  - **Overall:**
  
  \[
  O(n \log n + m)
  \]

- **Space Complexity:**
  - Sorting modifies the input array in-place, requiring **O(1)** extra space.
  - However, if Python uses Timsort (which can create temporary copies during sorting), the worst-case space complexity could be **O(n)**.

## Notes
- While this approach is simple and effective for small inputs, it may not be the most memory-efficient for large datasets.
- Alternative methods like Vertical or Horizontal Scanning can achieve better space complexity without sorting.



'''