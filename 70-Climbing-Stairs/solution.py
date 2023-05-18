# 70. Climbing Stairs
""" Logic: In this problem you are basically 
           meant to figure out, in how many 
           ways can you add up one or two to 
           get to the required number."""
           
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    a1 = 1
    a2 = 1
    num = 0
    for i in range(n-1):
        num = a1 + a2
        a1 = a2 
        a2 = num
    return num    
