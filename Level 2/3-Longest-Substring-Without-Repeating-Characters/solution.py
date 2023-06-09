class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = '' # this is the temporary variable where i will store the various possible substrings.
        max_len = len(substr) # var to store the length of the corresponding substrings
        for i in range(len(s)): # iterate through the string
            if max_len >= len(s) - i: # if the current max_len is more than or equal to he number of remaining character
                return max_len # then we dont need to run the loop anymore.
            while s[i] not in substr: # this is where i form the possible substrings for every character
                substr += s[i] # this while loop runs until we find a repeating character
                if i+1 <len(s):
                    i+= 1

            if len(substr) > max_len: # if the length of the substr is more than the current max length then we replace it
                max_len = len(substr) 
            substr = '' # after every iteration of the for loop we reset the substring to an emoty string.
            
        return max_len
