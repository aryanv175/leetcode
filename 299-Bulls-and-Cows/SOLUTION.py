# 299. Bulls and Cows
"""Logic: First we transform both strings to lists then we 
          find the bulls in the guess to do so, we just match
          the values at the same index, if they are same, we have
          found a bull. Now to find the cows, we just check if the 
          value from secret is present in the guess list. If so, we
          have a cow value as well."""

def getHint(secret, guess):
    bull, cow = 0,0 
    secret = list(secret)
    guess = list(guess)

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bull += 1
            secret[i] = '#'
            guess[i] = '#'

    for i in range(bull):
        guess.remove('#')
        secret.remove('#')

    # eg sec = [1, 8, 0, 7]
    # guess  = [7, 8, 1, 0]

    # after first loop:

    # eg sec = [1, 0, 7]
    # guess  = [7, 1, 0]

    for i in secret:
        if i in guess:
            cow += 1
            guess.remove(i)

    return str(bull) + 'A' + str(cow) + "B"
