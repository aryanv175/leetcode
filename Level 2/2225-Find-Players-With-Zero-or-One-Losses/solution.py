class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # logic behind this problem is  to count the number of losses. 
        res = [[], []] 
        losses = defaultdict(lambda: 0)
        for  i in matches:
            losses[i[0]] += 0  # if the person wins they the number of losses increases by 0.
            losses[i[1]] += 1  # if the person loses then the number of losses increases by 1.
        
        for i in losses.keys():
            if losses[i] == 0: # if they have 0 losses, they have only won!
                res[0].append(i)
            elif losses[i] == 1: # if they have 1 loss, we add it to res[1]
                res[1].append(i)
        res[0].sort() # we have to sort them
        res[1].sort()
        return res # return it!
        
