class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # counter to get the frequency of each task
        freq = Counter(tasks)
        # if the number of charcters are enough to satisfy the condition, we can take that
        case1 = len(tasks)

        list1 = sorted(freq.values())
        max_freq = list1[-1]
        i = list1.count(max_freq)

        case2 = (max_freq -1) * (n + 1)  + i

        return max(case1, case2)
