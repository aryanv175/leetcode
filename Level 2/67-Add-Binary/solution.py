class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) != len(b): # make the strings equal length by adding 0s to the front of the sdmaller string
            if len(a)> len(b):
                for i in range(len(a)-len(b)):
                    b = '0' + b
            else:
                for i in range(len(b)-len(a)):
                    a = '0' + a
        res = '' # the string to store the result
        carry = '0' # this value is the carry. 
        for i in range(len(a)-1, -1, -1):
            if a[i] == b[i] == '1': # If we add 1+1. 
                if carry == '0':  # carry == 0
                    res = '0' + res     # the digit is 0 
                else:
                    res = '1' + res # carry == 1 then the digit is 1
                carry = '1' # carry in this case is always 1
            elif a[i] != b[i]: # if we have alterante digits 
                if carry == '0': # if carry is 0 then carry remains 0 and the digit is 1
                    res = '1' + res
                    carry = '0'
                else: # if carry is 1 then the carry is 1 and the digit is 0
                    res = '0' + res
                    carry = '1'
            else: # if both digits are 0, carry in the end in this case is always 0
                if carry == '0': # if the carry is 0 then the digit is 0
                    res = '0' + res
                else: # if the carry is 1 then the digit is 1
                    res = '1' + res
                carry = '0'
        if carry == '1': # we add the carry in the front of the result if it is 1
            res = carry + res
        return res # return  it! 
