# 746. Min Cost Climbing Stairs
""" Logic: In this problem, we make an array 'step'
           to store the cost values for every step
           that we can take. For e.g. if the cost 
           array is [1, 2, 3, 1, 5, 20] the step array
           will look like: [1, 2, 3+1, 1+2, 5+3, 20+3].
           We can see one og the terms to understand what 
           is happening. lets take step[3] = 1 + 2. Here 1
           is cost[3] and the + 2 comes from min(step[2], step[1])
           min(4, 2) = 2."""

def minCostClimbingStairs(cost):

    length = len(cost)
    step = [0] * length
    step[0] = cost[0]
    step[1] = cost[1]

    for i in range(2, length):
        step[i] = cost[i] + min(step[i-1], step[i-2])

    return min(step[-1], step[-2])
