# 278. First Bad Version
""" Logic: I just used binary search here. Since it
           specifically says to reduce the amount of
           times you call the isBadVersion function,
           to do so  we need to use Binary Search.
           Giving it a time complexity of O(logn)."""


def firstBadVersion(self, n: int) -> int:
    start, end = 1, n

    while start < end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1

    return start
