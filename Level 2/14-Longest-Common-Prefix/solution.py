class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0] # i assumed that the first element is the substring. ideally you want this to be the smallest string.
        while pre != '': # we do a while loop until we find a common prefix
            pre_rn = pre # this is to monitor if we have found the prefix
            for i in range(1, len(strs)): # chceck every word, except the first one because the first word is already set as the prefix
                if pre not in strs[i][:len(pre)]: # [:len(pre)] this is important to make sure you are checking the first letters
                    pre = pre[:-1] # if it is not a prefix, check for a shorter common prefix
                    break # break out of the for loop
            if pre == pre_rn: # if there was no change in the pre var, then it is the longest common prefix
                return pre # return the prefix

        return pre #return! 
