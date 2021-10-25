def checkPalindrome(X):
    l = len(X)
    if l < 2:
        return True
    elif X[0] == X[l - 1]:
        return checkPalindrome(X[1: l - 1])
    else:
        return False