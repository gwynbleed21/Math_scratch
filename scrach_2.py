import numpy as np
x =[46,46,48,42,40,38]
y =[0,0,0,0,0,0]
j=[]
for i in x:
    for k in y:
        r = i - k
        j.append(r)
jl = j[::(len(x)+1)]
#print(j)
print(jl)
print("d = " , sum(jl)/len(jl))
if len(x) == len(y):  # same thing
    z = sum(x)-sum(y)
    print("d = " , z/len(x))
St = []

for i in jl:
    st = i**2
    St.append(st)
    d = (sum(jl) / len(jl))
    q = (sum(St)-2*d*sum(jl)+len(jl)*(d**2))/(len(jl)-1)
print(q)




