x=[1,2,3,4,5]
def ds(x,a):
    if a>1:
        y=[]
        for i in range(0,len(x)):
            if a*i<len(x):
                 y.append(x[a*i])
    return y
y=ds(x,3)
print(y)
