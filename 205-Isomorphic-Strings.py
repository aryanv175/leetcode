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
