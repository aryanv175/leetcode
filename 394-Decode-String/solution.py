# 394. Decode String
"""Logic: Here we use a stack called out_str to store all
          the characters of the given string s, until we find
          a closing bracket ']'. Once that happens, we  form a 
          substring until we find an opening bracket '[' and
          store it in sub_str, similarly we find the multiplier
          and store it in 'n'. Once we have both, we append the
          multiplied substring to the stack. We then convert this 
          stack to a string which we return."""

def decodeString(s):
    out_str = []
    digit = 0
    for i in range(len(s)):
        if s[i] != "]":
            out_str.append(s[i])
            if s[i].isdigit():
                digit += 1
        else:
            sub_str = ""
            while out_str[-1] != "[":
                sub_str = out_str.pop() + sub_str
            out_str.pop()
            n = ""
            while out_str and out_str[-1].isdigit():
                n = out_str.pop() + n
            n = int(n)
            out_str.append(int(n)*sub_str)
    if digit == len(s):
        return ""
    else:
        return "".join(out_str)
