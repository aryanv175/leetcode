class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words) # to get the requency of each word in words
        res = middle = 0 # initialise both values to zero. 
        
        for word in freq.keys():
            if word[0] == word[1]: # for cases like 'gg'
                if freq[word] % 2 ==0: # if gg apears twice then we can add that directly to our resulting pallindrome
                    res += freq[word]
                else:
                    res += freq[word] - 1 # if it appears 3 times, we can add it 3-1 times to res and one time to our middle
                    middle = 1 # note that middle stays 1. it is not middle += 1
            
            elif word[::-1] in freq: # for a string like 'ab' we first check if 'ba' exits
                res += min(freq[word], freq[word[::-1]]) # if 'ab': 2 and 'ba' : 3 then we can only add ab ab and ba ba to the result. so only min(2, 3) times
        
        return (res + middle) * 2
