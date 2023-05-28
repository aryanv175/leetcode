class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def convert(s: str):
            return int(s) 

        return str(convert(num1) * convert(num2))

"""class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def convert(s: str):
            num = 0
            for i in range(len(s)):
                num += int(s[-i-1]) * (10 ** i)
            return num

        return str(convert(num1) * convert(num2))"""

# i saw a few solutions online, all of them eventually, used the int() function. 
# so what makes either of these two solutions, correct or incorrect.
# This is a weird problem.
