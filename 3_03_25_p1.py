
# GitHub : https://github.com/ng196/DSA-BASICS.git

'''
In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'. Here, '?' can be replaced by any of the lowercase alphabets. Now you have to classify the given String on the basis of following rules:

If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD". A String is considered "GOOD" only if it is not “BAD”.

NOTE: String is considered as "BAD" if the above condition is satisfied even once. Else it is "GOOD" and the task is to make the string "BAD". '''


class Solution:
    def isGoodorBad(self, S):
        v = "aeiou"
        vowel = 0 
        conso = 0
        for i in S :
            if i in v :
                conso =0 
                vowel+=1
                
                
                
            elif i == '?':
                conso += 1 
                vowel += 1 
                    
                
                    
            elif i not in v :
                vowel = 0 
                conso+=1 
            
                
            if vowel>5 or conso > 3 :
                return 0 
            
        return 1 
            



'''
Approach : transversing the string once , and increasing consecutive vowel and conso counts while other is 0 , ? is considered as both conso and vowel 

'''

# time and soace complexity : O(|S|)  and O(1)




