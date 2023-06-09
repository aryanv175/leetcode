# 392-Is-Subsequence
""" Logic: Use a loop to go through the string
           s, store the indexes of the letters
           of s in a list, make sure the list
           is in ascending order. If that is the
           case, return True, otherwise False."""

def isSubsequence( s: str, t: str) -> bool:
      list1 = []
      last = 0
      for i in range(len(s)):
          try:
              if t.find(s[i]) >= 0:
                  list1.append(t.find(s[i], last))
                  last= t.find(s[i], last) + 1
              else:
                  return False
          except:
              pass
      for j in range(len(list1)-1):
          if list1[j]> list1[j+1]:
              return False
      return True
