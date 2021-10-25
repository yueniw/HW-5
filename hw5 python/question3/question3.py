def oneaway(X,Y):
    a = len(X)
    b = len(Y)
    if (X==Y or abs(a-b)>1) :
        return False
    p1 = 0
    p2 = 0
    edit = False
    while p1 < a and p2 < b:
        if X[p1] == Y[p2]:
            p1+=1
            p2+=1
        elif not edit:
            edit = True
            if a==b:
                p1+=1
                p2+=1
            elif a<b:
                p2+=1
            elif a>b:
                p1+=1
        else:
            return False
    return True
