def pyramid2(X):
    s=X-1
    for num in range(1,X):
        print(" "*s,"* "*num)
        s-=1