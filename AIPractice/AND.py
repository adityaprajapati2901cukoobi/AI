import numpy as np

def unitStep(v):
    if v>=0:
        return 1
    else:
        return 0
    
def perceptronModel(x,w,b):
    v=np.dot(w,x)+b
    y=unitStep(v)
    return y

def OR_logicfunction(x):
    w=np.array([1,1])
    b=-0.5
    return perceptronModel(x,w,b)

def AND_logicfunction(x):
    w=np.array([1,1])
    bAND= -1.5
    return perceptronModel(x,w,bAND)

test1=np.array([1,1])
print("OR({},{})={}".format(0,1,OR_logicfunction(test1)))
