import numpy as np  
x =[46,46,48,42,40,38]  # input lists
y =[0,0,0,0,0,0]        # this program is a calculator for the mean and unbiased estimate for variance of the difference between two sets of data.
j=[]                    
for i in x:
    for k in y:
        r = i - k
        j.append(r)
jl = j[::(len(x)+1)]
#print(j)
print(jl)
print("d = " , sum(jl)/len(jl))
if len(x) == len(y):  # same thing, just to check if the first one is correct.
    z = sum(x)-sum(y)
    print("d = " , z/len(x))
St = []

for i in jl:
    st = i**2
    St.append(st)
    d = (sum(jl) / len(jl))
    q = (sum(St)-2*d*sum(jl)+len(jl)*(d**2))/(len(jl)-1)
print(q)




