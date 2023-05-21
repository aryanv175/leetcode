# 692. Top K Frequent Words
"""Logic: First we make a default dict to store the frequencies of each word.
          Next we use the sorted method to sort it. The sorted method here, is taking
          two arguments: frequency.keys(), those are the words that we are concerned about.
          Then comes the lambda function used here, here x is the key, so the first sorting 
          method is -frequency[x] which means sort in a descending order by the value of frequency[x].
          The next part is just x, which will sort x in alphabetical order. The [:k] represents that 
          we only need the top k values from the sorted method. Keep in mind the sorted method, returns
          a list by default."""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        frequency = defaultdict(lambda: 0) # use default dict for ease of use

        for i in words:
            frequency[i] += 1 # get the grequency of each word in the dict frequency

        return (sorted(frequency.keys(), key = lambda x: (-frequency[x], x))[:k])
