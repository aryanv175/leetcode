# 205-Isomorphic-Strings
""" Logic: Used dictionaries in this problem. 
           go through every letter in any of the
           two strings, for every unique letter in s
           assign it the first letter in that is at
           the same index and store in the dictionariy. 
           Once the letter in s is repeated check if the 
           letter in t at that index is the same one,
           if so, keep going. Otherwise, return False.
           """

def isIsomorphic(self, s: str, t: str) -> bool:
      taken = {}
      taken2 = {}
      if len(s) == len(t):
          for i in range(len(s)):
              if t[i] not in taken:
                  taken[t[i]] = s[i]
              else:
                  if taken[t[i]] != s[i]:
                      return False
              if s[i] not in taken2:
                  taken2[s[i]] = t[i]
              else:
                  if taken2[s[i]] != t[i]:
                      return False
          return True
      return False
