import numpy as np
X = [13.21,13.97,13.76,13.11,13.25,13.98,13.03]
Y = [12.93,13.13,12.98,13.01,12.99,13.21,13.01]
if len(X) == len(Y):
    xd = sum(X)/len(X)
    yd = sum(Y)/len(Y)

    Stx = []
    for i in X:
        st = i ** 2
        Stx.append(st)
        xv = (sum(Stx) - 2 * xd * sum(X) + len(X) * (xd ** 2)) / (len(X) - 1)

    Sty = []
    for i in Y:
        st = i ** 2
        Sty.append(st)
        yv = (sum(Sty) - 2 * yd * sum(Y) + len(Y) * (yd ** 2)) / (len(Y) - 1)

print(" xd = " , xd ," \n", "xv = " , xv ," \n", "yd = " , yd ," \n", "yv = " , yv ," \n",)

if len(X) > 30:
    z = np.float(input("z"))
    lb = xd - yd - z*(np.sqrt( (xv/len(X)) + (yv/len(Y))))   #lower boundary
    ub = xd - yd + z*(np.sqrt( (xv/len(X)) + (yv/len(Y))))    # upper boundary
    print(lb , "< µ <", ub)
if len(X) < 30:
    print("degrees of freedom: " , (len(X)+len(Y)-2))
    t = np.float64(input("t"))
    pv = (xv*(len(X)-1) + yv*(len(Y)-1))/(len(X)+len(Y)-2)             #pool variance estimate
    #print(pv, "\n" , t)   #check
    lb = xd - yd - t*(np.sqrt( pv*((1/len(X)) + (1/len(Y)))))
    ub = xd - yd + t*(np.sqrt( pv*((1/len(X)) + (1/len(Y)))))
    print(lb , "< µ <", ub)
