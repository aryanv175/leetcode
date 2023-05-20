# 438. Find All Anagrams in a String
"""Logic: Here we will use two pointers and two hashmaps.
          The first hashmap will be used to store the characters  
          of p with the count of each alphabet. The second hashmap 
          will be used to keep the charcters and their count of the
          current substring of s. One pointer will point to the start
          of the substring and the other pointer will point to the 
          end of the substring."""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if  len(p) > len(s):
            return []
    
        pCount = defaultdict(lambda: 0)
        sCount = defaultdict(lambda: 0)
        for i in range(len(p)):
            pCount[p[i]] += 1 
            sCount[s[i]] += 1

        if sCount == pCount:
            res = [0]
        else:
            res = []
        # l is left pointer, r is right pointer
        # we are starting at len(p), because we have already compared
        # the first substring
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] += 1
            sCount[s[l]] -= 1 # removing the first alpabet of the previous substring from the hashmap
            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1

            if sCount == pCount:
                res.append(l)

        return res

            
