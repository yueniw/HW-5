punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def removepunc(X):
    result = ""
    for char in X:
        if char not in punctuations:
            result = result + char
    return result


removepunc("Hello in 36-650, & other MSP courses.")