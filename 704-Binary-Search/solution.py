# 704. Binary Search
""" Logic: I just used the .index method of lists,
           which returns the index of the element that
           you want and otherwise raises a value error.
           Very quick and easy."""
def search(self, nums: List[int], target: int) -> int:
    try:
        goal = nums.index(target)
    except:
        return -1

    return goal
