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
