#424. Longest Repeating Character Replacement
"""Logic: Here we will use a hashmap count which will store the 
        occurrences of the characters in a substring. We can then substract 
        the max count with the length of the substring at that will give us 
        the number of characters we have to replace. Then we can confirm that 
        that value is less than k. Then we will use two pointers, left and right 
        to determine the length of the max substring we can take."""
def characterReplacement(s, k) -> int:
    count = {}
    res = 0
    left = 0
    for right  in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)

        while right-left + 1 - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, right-left + 1)
    return res
