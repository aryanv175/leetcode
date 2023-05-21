# 844. Backspace String Compare
"""Logic: Here I made two new strings, to store the
          strings after I implemented the backspace
          functionality, which is quite easy. Every
          time you encounter a '#', simply remove the
          previous element from the new string using
          the new_string  = new_string[:-1] slice notation."""

def backspaceCompare(s, t):

    new_s = ''
    new_t = ''

    for i in range(len(s)):
        if s[i] == '#':
            new_s = new_s[:-1]
        else:
            new_s += s[i]

    for i in range(len(t)):
        if t[i] == '#':
            new_t = new_t[:-1]
        else:
            new_t += t[i]
    return new_s == new_t

