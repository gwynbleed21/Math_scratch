
def stat(X):
    import numpy as np
    """input a list"""

    n=len(X)
    print(" n = " , n)

    k = sum(X)
    print("sum = " , k)

    R=[]
    for i in X:
        r = i**2
        R.append(r)
    u=sum(R)
    print("sum2 = " , u)

    a = k/n
    print("a = " , (a))

    j = (u-2*a*k+n*(a**2))/(n-1)
    print("s^2 =" , j)
    print("s = " , np.sqrt(j) )



stat([47,51,47,50,53,51,50,45])

#stat([34,45,36,47,42,43])




