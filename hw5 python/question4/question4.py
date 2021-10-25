def triangle(X):
    if (not isinstance(X, int) or X < 0):
        return ("Invalid Input")
    else:
        index=1
        for i in range(1,X+1):
            for j in range(1,i+1):
                print(index,end=" ")
                index +=1
            print()