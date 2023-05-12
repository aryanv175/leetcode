# 409. Longest Palindrome
""" Logic: The logic for this problem is counting
           the number of times a letter comes.
           Basically, if the count is even add
           it to the final asnwer directly, if it is 
           odd we add after substracting it by 1."""

def longestPalindrome(s: str) -> int:
    count = 0
    odds = []
    letters = []
    ans = 0
    for i in s:
        if i not in letters:
            letters.append(i)


    for i in letters:
        curr, count = 0, 0
        while curr < len(s) and s.find(i, curr) != -1:
            curr = s.find(i, curr) + 1
            count += 1
        if count % 2 == 0:
            ans += count
        else:
            if count == 1 and 1 not in odds:
                odds.append(1)
            else:
                odds.append(count)
    if len(odds) != 0:
        ans += odds[0]
        del odds[0]

        for i in odds:
            ans = ans + (i -1)

    return ans
