class Solution:
    def isHappy(self, n: int) -> bool:
        def sq_sum(num):  # make a function that will calculate the sums of square of digits.
            res=0 
            for i in range(len(str(num))): 
                res += int(str(num)[i])**2
            return res, res

        res = 0 
        list1 = [n]
        n, res = sq_sum(n) 
        while res != 1: # if the result is 1, return true. end loop
            n, res = sq_sum(n)
            if n in list1: # in case of a non happy number we are boud to repeat values
                return False # so if we find a previously occuring value, we return False.
            list1.append(n)
        return True
        
