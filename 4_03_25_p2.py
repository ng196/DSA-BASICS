'''
Problem Statement : Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
'''

from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]):
        count_map = defaultdict(int) 
        pair_count = 0 
        for a, b in dominoes:
            key = (min(a, b), max(a, b))  
            pair_count += count_map[key]  
            count_map[key] += 1  
    
        return pair_count
    
    
'''
hash table , frequency 

Time Complexity: O(n)
Space Complexity: O(n)

Approach : made a defaultdict , that will count frequency of each pair , iterate over given list after sorting it , and if there already exists the key , then add it , and increase the frequency by 1 


'''
