# 1046. Last Stone Weight
"""Logic: Here, we will make use of the data structure Heap.
          The default heap in python is a MinHeap, so to get a 
          max heap, we will make all the current values negative.
          Then we use heappop to get the max values, once we have those
          we heappush the -1*(difference). Then we heapify again because
          heappush inserts it at the end of the heap. Then we return the 
          remaining value in the heap after making it positive."""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s  for s in stones] # making the values negative
        heapify(stones) #result is a maxHeap

        while len(stones) > 1: # because in the end we only want one value
            max1 = heappop(stones) * -1 # make sure to make the value +ve again
            max2 = heappop(stones) * -1 # second max value

            heappush(stones, -1 *(max1 -max2)) # add the difference to the heap
            heapify(stones) # need to heapify again to make sure it is a max heap 
            

        return heappop(stones)*-1 # make sure to make the end result positive again
