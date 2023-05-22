class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = defaultdict(lambda: 0) #default dict to store the frequency of each number
        for i in nums:
            frequency[i] += 1 #calculating and storing the frequency of every number in nums

        return sorted(frequency.keys(), key= lambda x: (-frequency[x]))[:k] 
        
        # sorted(data, key function to sort in a specific way) sorts the dict
        # we want to return just the keys so we use frequency.keys()
        # lambda function, we want to sort with respect to the keys
        # we want to sort in a descending order so we used a minus sign
        # we only care about the first k elements so we used [:k] slice operation.
